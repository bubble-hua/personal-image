#!/usr/bin/env python3
"""
16:9 裁剪脚本 v1：
将正方形图片（1024x1024）裁剪为 16:9 横版（1024x576）。
裁剪策略：保留画面中心区域，从上下各裁掉 (1024-576)/2 = 224 像素。
"""
from PIL import Image
import sys
import os


def crop_to_16_9(input_path, output_path):
    """
    将图片裁剪为 16:9 横版比例。
    - 如果图片是正方形（如 1024x1024），裁剪为中心 16:9 区域（1024x576）
    - 如果图片已经是 16:9 或更宽，保持不变
    - 如果图片比 16:9 更高，按比例裁剪上下
    """
    img = Image.open(input_path).convert('RGB')
    w, h = img.size

    # 目标比例 16:9
    target_ratio = 16 / 9
    current_ratio = w / h

    if abs(current_ratio - target_ratio) < 0.01:
        # 已经是 16:9，直接保存
        img.save(output_path)
        print(f"Already 16:9 ({w}x{h}), saved as-is.")
        return

    if current_ratio > target_ratio:
        # 图片太宽（宽高比 > 16:9），裁剪左右
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        right = left + new_w
        cropped = img.crop((left, 0, right, h))
    else:
        # 图片太高（宽高比 < 16:9），裁剪上下 —— 这是最常见的情况
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        bottom = top + new_h
        cropped = img.crop((0, top, w, bottom))

    cropped.save(output_path)
    print(f"Cropped to 16:9: {w}x{h} -> {cropped.size[0]}x{cropped.size[1]}")


if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    if not input_file or not output_file:
        print("Usage: python3 crop_16_9.py <input> <output>")
        sys.exit(1)

    crop_to_16_9(input_file, output_file)
