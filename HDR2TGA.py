import os
import imageio.v2 as imageio
import numpy as np
from PIL import Image

def convert_hdr_to_tga_png(input_folder, output_folder):
  # 创建输出文件夹（如果不存在）
  os.makedirs(output_folder, exist_ok=True)
  
  # 遍历输入文件夹中的HDR文件
  for filename in os.listdir(input_folder):
      if filename.endswith(".hdr"):
          hdr_path = os.path.join(input_folder, filename)
          
          try:
              # 使用imageio读取HDR文件
              img_data = imageio.imread(hdr_path)
              
              # HDR图像数据处理
              # 将数据归一化到0-1范围
              img_data = np.clip(img_data, 0, None)  # 去除负值
              img_data = img_data / np.max(img_data)  # 归一化
              
              # 色调映射 (简单的伽马校正)
              gamma = 2.2
              img_data = np.power(img_data, 1/gamma)
              
              # 转换为8位图像
              img = Image.fromarray(np.uint8(img_data * 255))
              
              # 生成输出文件名（TGA和PNG）
              base_filename = os.path.splitext(filename)[0]
              tga_filename = os.path.join(output_folder, f"{base_filename}.tga")
              png_filename = os.path.join(output_folder, f"{base_filename}.png")
              
              # 保存为TGA格式
              img.save(tga_filename, format='TGA')
              
              # 保存为PNG格式
              img.save(png_filename, format='PNG')
              
              print(f"成功转换 {filename} 到 TGA 和 PNG 格式")
          
          except Exception as e:
              print(f"转换 {filename} 失败: {e}")

def main():
  # 配置输入和输出文件夹路径
  input_folder = 'path/input/hdr'  # 输入 HDR 文件夹路径
  output_folder = 'path/output/hdr2tgaPng'  # 输出 TGA/PNG 文件夹路径
  
  # 执行转换
  convert_hdr_to_tga_png(input_folder, output_folder)

if __name__ == '__main__':
  main()