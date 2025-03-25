import os
import argparse
import imageio.v2 as imageio
import numpy as np
from PIL import Image

def process_files(input_folder, output_folder, flip_y):
    """
    处理输入文件夹中的DDS/HDR文件，转换为TGA/PNG格式
    
    Args:
        input_folder: 输入文件夹路径
        output_folder: 输出文件夹路径
        flip_y: 是否翻转Y轴
        
    Returns:
        tuple: (已转换文件列表, 转换失败文件列表)
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 初始化结果列表
    converted_files = []
    failed_files = []
    
    # 判断输入文件夹是否存在
    if not os.path.exists(input_folder):
        print(f"错误：输入文件夹 '{input_folder}' 不存在")
        return converted_files, failed_files
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        # 跳过目录
        if os.path.isdir(input_path):
            continue
        
        # 检查文件扩展名
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext not in ['.dds', '.hdr']:
            continue
        
        try:
            # 读取输入文件
            img = imageio.imread(input_path)
            
            # 如果需要翻转Y轴
            if flip_y:
                img = np.flipud(img)
            
            # 确定输出格式和文件名
            basename = os.path.splitext(filename)[0]
            if file_ext == '.dds':
                output_filename = f"{basename}.tga"
                output_format = 'tga'
            else:  # .hdr
                output_filename = f"{basename}.png"
                output_format = 'png'
            
            output_path = os.path.join(output_folder, output_filename)
            
            # 保存转换后的图像
            imageio.imwrite(output_path, img, format=output_format)
            
            # 添加到成功列表
            converted_files.append((input_path, output_path))
            
        except Exception as e:
            print(f"处理文件 '{filename}' 时出错: {str(e)}")
            failed_files.append(input_path)
    
    return converted_files, failed_files

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='将DDS/HDR文件转换为TGA/PNG格式，可选择是否翻转Y轴')
    parser.add_argument('-i', '--input', default='path/input', help='输入文件夹路径 (默认: path/input)')
    parser.add_argument('-o', '--output', default='path/output', help='输出文件夹路径 (默认: path/output)')
    parser.add_argument('-f', '--flip', action='store_true', help='是否翻转Y轴')
    
    args = parser.parse_args()
    
    # 使用固定的默认路径
    input_folder = args.input  # 默认为 'path/input'
    output_folder = args.output  # 默认为 'path/output'
    
    print("===== DDS/HDR 转换器 =====")
    print(f"输入文件夹: {input_folder}")
    print(f"输出文件夹: {output_folder}")
    print(f"翻转Y轴: {'是' if args.flip else '否'}")
    print("========================")
    
    # 处理文件
    converted_files, failed_files = process_files(input_folder, output_folder, args.flip)
    
    # 输出结果
    print("\n===== 转换结果 =====")
    print(f"成功转换: {len(converted_files)} 个文件")
    for input_file, output_file in converted_files:
        print(f"  {os.path.basename(input_file)} -> {os.path.basename(output_file)}")
    
    if failed_files:
        print(f"\n转换失败: {len(failed_files)} 个文件")
        for failed_file in failed_files:
            print(f"  {os.path.basename(failed_file)}")
    
    print("==================")

if __name__ == '__main__':
    main()
