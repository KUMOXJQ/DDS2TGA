import os
from PIL import Image
import imageio
import numpy as np
import cv2

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
            elif filename.endswith('.hdr'):
                try:
                    # 使用OpenCV读取HDR图片，保持原始色彩空间
                    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
                    if image is not None:
                        # 检查图像通道数
                        if len(image.shape) == 2:
                            # 如果是单通道，转换为3通道
                            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
                        # 垂直翻转HDR图片
                        flipped_image = cv2.flip(image, 0)
                        # 保存HDR图片，使用UNCHANGED参数保持原始色彩和位深度
                        cv2.imwrite(output_path, flipped_image, [cv2.IMWRITE_EXR_COMPRESSION, cv2.IMWRITE_EXR_COMPRESSION_PIZ])
                        print(f'Flipped HDR: {image_path} to {output_path}')
                    else:
                        print(f'Failed to read HDR image: {image_path}')
                except Exception as e:
                    print(f'Error processing HDR image {image_path}: {str(e)}')
                continue
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
