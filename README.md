# DDS/HDR to TGA 格式转换工具

这是一个用于将 DDS 和 HDR 格式图像文件转换为 TGA/PNG 格式的 Python 工具。

## 功能特性

- **DDS 转 TGA**: 将 DirectDraw Surface (.dds) 文件转换为 Truevision TGA (.tga) 格式
- **HDR 转 PNG**: 将高动态范围 (.hdr) 图像转换为 PNG 格式，支持色调映射
- **批量转换**: 支持文件夹内所有文件的批量处理
- **Y轴翻转**: 可选的 Y轴翻转功能
- **命令行界面**: 灵活的命令行参数配置

## 安装依赖

```bash
pip install Pillow imageio numpy
```

## 使用方法

### 方法1: 使用统一转换器 (推荐)

```bash
python converter.py -i path/input -o path/output
```

#### 命令行参数

- `-i, --input`: 输入文件夹路径 (默认: path/input)
- `-o, --output`: 输出文件夹路径 (默认: path/output)  
- `-f, --flip`: 是否翻转Y轴

#### 使用示例

```bash
# 基础转换
python converter.py

# 指定输入输出路径
python converter.py -i ./images -o ./converted

# 启用Y轴翻转
python converter.py -i ./images -o ./converted -f
```

### 方法2: 单独使用转换脚本

#### DDS 转 TGA

```bash
python DDS2TGA.py
```

编辑脚本中的路径配置：
```python
input_folder = 'path/input/dds'     # DDS文件输入路径
output_folder = 'path/output/dds2tga'  # TGA文件输出路径
```

#### HDR 转 PNG/TGA

```bash
python HDR2TGA.py
```

编辑脚本中的路径配置：
```python
input_folder = 'path/input/hdr'        # HDR文件输入路径
output_folder = 'path/output/hdr2tgaPng'  # 输出路径
```

## 文件结构

```
DDS2TGA/
├── converter.py    # 统一转换器 (推荐使用)
├── DDS2TGA.py     # DDS专用转换器
├── HDR2TGA.py     # HDR专用转换器
├── path/
│   ├── input/     # 输入文件夹
│   └── output/    # 输出文件夹
└── README.md      # 说明文档
```

## 转换规则

- **DDS 文件**: 转换为 .tga 格式
- **HDR 文件**: 转换为 .png 格式，应用伽马校正 (gamma=2.2)
- **其他格式**: 自动跳过，不进行处理

## HDR 处理说明

HDR (高动态范围) 图像转换时会进行以下处理：
1. 去除负值数据
2. 数据归一化到 0-1 范围
3. 应用伽马校正 (gamma = 2.2)
4. 转换为 8位 图像数据

## 错误处理

- 自动创建输出文件夹
- 跳过无法处理的文件格式
- 显示转换成功/失败的详细信息
- 输出转换统计报告

## 依赖库

- **Pillow (PIL)**: 图像处理和格式转换
- **imageio**: 读取 DDS/HDR 格式文件
- **numpy**: 数值计算和数组操作

## 注意事项

- 确保输入文件夹存在且包含支持的格式文件
- 输出文件夹会自动创建
- 转换过程中会显示详细的进度信息
- 建议使用 `converter.py` 获得最佳的使用体验