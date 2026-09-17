import os
import sys
import shutil
from PIL import Image
import imageio.v2 as imageio

# 修复 Windows 控制台中文乱码：强制以 UTF-8 输出
if sys.stdout is not None and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr is not None and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


def clear_output_folder(output_folder):
    """
    清空输出文件夹中的所有内容（文件与子文件夹）

    Args:
        output_folder: 输出文件夹路径

    Returns:
        int: 删除的顶层条目数量；若路径不存在或不安全则返回 0
    """
    if not os.path.isdir(output_folder):
        return 0

    # 安全保护：拒绝驱动器根目录等危险路径，避免误删
    abs_out = os.path.abspath(output_folder)
    if os.path.dirname(abs_out) == abs_out:
        print(f"警告：输出路径为磁盘根目录，已跳过清空：{abs_out}")
        return 0

    removed = 0
    for name in os.listdir(output_folder):
        target = os.path.join(output_folder, name)
        try:
            if os.path.isdir(target):
                shutil.rmtree(target)
            else:
                os.remove(target)
            removed += 1
        except Exception as e:
            print(f"清理 '{name}' 失败: {str(e)}")
    return removed


def convert_dds_to_tga(input_folder, output_folder):
    # 运行前清空输出文件夹，避免残留旧文件
    removed = clear_output_folder(output_folder)
    print(f"已清空输出文件夹: 删除 {removed} 个旧文件")

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
