import os
from PIL import Image
import imageio
import numpy as np

def flip_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.tga') or filename.endswith('.dds') or filename.endswith('.png') or filename.endswith('.hdr'):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 使用 imageio 读取图片文件
            if filename.endswith('.dds'):
                image = imageio.imread(image_path)
                image = np.array(image)  # 转换为 NumPy 数组
            else:
                image = Image.open(image_path)

            # 使用 Pillow 进行翻转
            if isinstance(image, np.ndarray):
                flipped_image = Image.fromarray(image).transpose(method=Image.FLIP_TOP_BOTTOM)
            else:
                flipped_image = image.transpose(method=Image.FLIP_TOP_BOTTOM)

            # 保存翻转后的图片
            flipped_image.save(output_path)

            print(f'Flipped: {image_path} to {output_path}')

if __name__ == '__main__':
    input_folder = 'path/output/flipY'  # 输入文件夹路径
    output_folder = 'path/output/flipYed'  # 输出文件夹路径
    flip_images(input_folder, output_folder)
