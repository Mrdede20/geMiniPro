import os
import json


# 将指定目录下python文件转化为json文件
def convert_python_to_json(source_dir, target_file):
    # 确保目标目录存在
    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    # 初始化结果列表
    result = []

    # 遍历指定目录下的所有Python文件
    for filename in os.listdir(source_dir):
        if filename.endswith(".py"):
            # 构建完整的文件路径
            file_path = os.path.join(source_dir, filename)

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

                # 将文件内容中的空白符（换行、制表符等）转换为其表示字符串
                converted_content = content.replace('\n', '\\n').replace('\t', '\\t')

                # 将文件名和处理后的内容添加到结果列表
                result.append({'filename': filename, 'program': converted_content})

    try:
        # 尝试打开目标文件并写入结果
        with open(target_file, 'w', encoding='utf-8') as json_file:
            json.dump(result, json_file, ensure_ascii=False, indent=4)
        print("结果已成功写入"+target_file)
    except FileNotFoundError:
        # 文件未找到时的异常处理
        print(f"错误：找不到文件或无法打开文件 '{target_file}'。")
    except IOError:
        # 文件读写错误的异常处理
        print(f"错误：写入文件 '{target_file}' 时发生错误。")
    except Exception as e:
        # 其他异常的处理
        print(f"发生未知错误：{e}")

# 使用函数
source_dir = "data/sourceCode/buggy"
target_file = "data/sourceCode/json/buggy.json"
convert_python_to_json(source_dir, target_file)
