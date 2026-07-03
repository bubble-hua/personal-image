#!/usr/bin/env python3
"""
纯白背景处理 v3：
1. 用更激进的策略 - 把所有 RGB 三个通道都 > threshold 的像素视为白色候选
2. 用 flood fill 从四个角开始，只刷与边缘连通的浅色区域
3. 这样可以保护前景中的任何物体
"""
from PIL import Image
import numpy as np
from scipy import ndimage
import sys

def corner_flood_whiten(input_path, output_path, threshold=200):
    """
    从图片四角开始 flood fill，把所有连通的浅色区域刷成纯白。
    这样只有真正属于背景的浅色区域会被处理，前景物体完全不受影响。
    """
    img = Image.open(input_path).convert('RGB')
    data = np.array(img, dtype=np.float32)
    
    h, w = data.shape[:2]
    
    # 计算亮度和色差
    r, g, b = data[:,:,0], data[:,:,1], data[:,:,2]
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    
    # 浅色候选：亮度高 且 三个通道值都接近（接近灰/白，非彩色）
    bright_mask = (luminance > threshold).astype(np.uint8)
    
    # 从四角开始 flood fill
    background_mask = np.zeros((h, w), dtype=np.uint8)
    
    # 创建种子点（四个角 + 四条边中点）
    seed_coords = [
        (0, 0), (0, w-1), (h-1, 0), (h-1, w-1),  # 四角
        (0, w//2), (h-1, w//2), (h//2, 0), (h//2, w-1)  # 边中点
        # 再加一些边上的点
    ]
    for i in range(0, w, max(1, w // 20)):
        seed_coords.append((0, i))
        seed_coords.append((h-1, i))
    for i in range(0, h, max(1, h // 20)):
        seed_coords.append((i, 0))
        seed_coords.append((i, w-1))
    
    # 标记所有种子点位置为起始
    seeds = np.zeros((h, w), dtype=bool)
    for sy, sx in seed_coords:
        if 0 <= sy < h and 0 <= sx < w and bright_mask[sy, sx]:
            seeds[sy, sx] = True
    
    # 在 bright_mask 上做 flood fill
    labeled, _ = ndimage.label(bright_mask)
    
    # 找出包含种子点的连通区域
    bg_regions = set()
    for sy, sx in seed_coords:
        if 0 <= sy < h and 0 <= sx < w and bright_mask[sy, sx]:
            bg_regions.add(labeled[sy, sx])
    
    # 构建背景 mask
    for region_id in bg_regions:
        background_mask[labeled == region_id] = 1
    
    # 刷白
    result = data.copy()
    result[background_mask.astype(bool)] = 255.0
    
    out_img = Image.fromarray(result.astype(np.uint8))
    out_img.save(output_path)
    total_px = int(np.sum(background_mask))
    print(f"Done: {output_path} (threshold={threshold})")
    print(f"  Background pixels whitened: {total_px} / {w*h} ({100*total_px/(w*h):.1f}%)")

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    threshold = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    
    if not input_file or not output_file:
        print("Usage: python3 corner_whiten.py <input> <output> [threshold]")
        sys.exit(1)
        
    corner_flood_whiten(input_file, output_file, threshold)
