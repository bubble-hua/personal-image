#!/usr/bin/env python3
"""
纯白背景处理 v4（智能灰度检测）：

针对 letterbox 构图的 AI 生成图片优化。
使用双重检测策略：
1. Color Key：基于与典型背景色的欧氏距离，清除边缘灰色
2. Uniform Gray：检测低饱和度的均匀灰色区域（RGB三通道接近），清除内部残留

相比 v3 (flood fill) 的优势：
- 不依赖边缘连通性，能清除被内容包围的灰色背景
- 对 letterbox 裁剪后的图片特别有效
- 更精确地保护彩色内容元素

用法：
  python3.11 scripts/smart_whiten_bg.py <input> <output> [distance_thresh] [uniform_range] [min_luminance]

参数：
  distance_thresh: Color key 距离阈值（默认 30）
  uniform_range: Uniform gray RGB 偏差范围（默认 28）
  min_luminance: 最小亮度门槛（默认 150）
"""
from PIL import Image
import numpy as np
import sys


def smart_whiten_bg(input_path, output_path, dist_thresh=30, uniform_range=28, min_lum=150):
    """
    智能灰度背景刷白：结合 color key 和 uniform gray 检测。

    算法：
    1. 从图片角落采样确定背景色基准值
    2. Phase 1 - Color Key：每个像素与背景色的欧氏距离 < dist_thresh → 刷白
    3. Phase 2 - Uniform Gray：RGB 三通道偏差 < uniform_range 且饱和度低且亮度够高 → 刷白
    """
    img = Image.open(input_path).convert('RGB')
    data = np.array(img, dtype=np.float32)
    h, w = data.shape[:2]

    r, g, b = data[:,:,0], data[:,:,1], data[:,:,2]
    luminance = 0.299 * r + 0.587 * g + 0.114 * b

    # 饱和度计算
    max_c = np.maximum(np.maximum(r, g), b)
    min_c = np.minimum(np.minimum(r, g), b)
    sat = np.where(luminance > 0, (max_c - min_c) / luminance, 0)

    # Step 1: 从角落/边缘采样确定背景色基准值
    sample_coords = [
        (5, 5), (5, max(6, w-6)), (max(6, h-6), 5), (max(6, h-6), max(6, w-6)),
        (5, w//2), (max(6, h-6), w//2),
        (h//2, 5), (h//2, max(6, w-6)),
    ]
    samples = np.array([data[y, x] for y, x in sample_coords if 0 <= y < h and 0 <= x < w])
    bg_r, bg_g, bg_b = samples.mean(axis=0)

    # Step 2: Phase 1 - Color Key（基于与背景色的距离）
    dist = np.sqrt((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)
    mask_colorkey = (dist < dist_thresh) & (luminance > min_lum - 20)

    # Step 3: Phase 2 - Uniform Gray（低饱和度 + 均匀RGB + 够亮）
    mask_uniform = (
        (np.abs(r - g) < uniform_range) &
        (np.abs(g - b) < uniform_range) &
        (np.abs(r - b) < uniform_range) &
        (luminance > min_lum) &
        (sat < 0.05)
    )

    # 合并两个 mask
    combined_mask = mask_colorkey | mask_uniform

    # 刷白
    result = data.copy()
    result[combined_mask] = 255.0

    out_img = Image.fromarray(result.astype(np.uint8))
    out_img.save(output_path)

    total_px = int(combined_mask.sum())
    new_lum_mean = (0.299 * result[:,:,0] + 0.587 * result[:,:,1] + 0.114 * result[:,:,2]).mean()

    print(f"Done: {output_path}")
    print(f"  Size: {w}x{h}")
    print(f"  Background reference: ({bg_r:.1f}, {bg_g:.1f}, {bg_b:.1f})")
    print(f"  Pixels whitened: {total_px} / {w*h} ({100*total_px/(w*h):.1f}%)")
    print(f"  New mean luminance: {new_lum_mean:.1f}")


if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    d_thresh = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    u_range = int(sys.argv[4]) if len(sys.argv) > 4 else 28
    m_lum = int(sys.argv[5]) if len(sys.argv) > 5 else 150

    if not input_file or not output_file:
        print("Usage: python3 smart_whiten_bg.py <input> <output> [dist_thresh] [uniform_range] [min_lum]")
        sys.exit(1)

    smart_whiten_bg(input_file, output_file, d_thresh, u_range, m_lum)
