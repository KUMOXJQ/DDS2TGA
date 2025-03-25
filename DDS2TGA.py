import os
from PIL import Image
import imageio.v2 as imageio

def convert_dds_to_tga(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.dds'):
            dds_path = os.path.join(input_folder, filename)
            tga_path = os.path.join(output_folder, filename.replace('.dds', '.tga'))

            # 使用 imageio 读取 DDS 文件
            image = imageio.imread(dds_path)

            # 使用 Pillow 保存为 TGA 文件
            img = Image.fromarray(image)
            img.save(tga_path, format='TGA')

            print(f'Converted: {dds_path} to {tga_path}')

if __name__ == '__main__':
    input_folder = 'path/input/dds'  # 输入 DDS 文件夹路径
    output_folder = 'path/output/dds2tga'  # 输出 TGA 文件夹路径
    convert_dds_to_tga(input_folder, output_folder)
