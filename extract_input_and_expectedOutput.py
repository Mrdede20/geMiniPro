import json
import re


# 提取出大模型回复中的input和expectedOutput
def extract_input_and_expectedOutput(source_file, target_file):
    # 打开并读取JSON文件
    with open(source_file, 'r') as file:
        data = json.load(file)

    # 遍历每个JSON对象
    for item in data:
        # 获取replyStage2字段
        reply_stage2 = item.get('replyStage2', '')

        # 使用正则表达式找到由```包围的文本块
        matches = re.findall(r'```([\s\S]*?)```', reply_stage2)
        item['input'] = []
        item['expectedOutput'] = []
        # 检查是否有足够的匹配项来提取input和expectedOutput
        if len(matches) >= 2:
            # 假设第一个匹配项是input，第二个是expectedOutput
            item['input'] = matches[0].strip().split('\n')
            item['expectedOutput'] = matches[1].strip().split('\n')
        else:
            # 如果没有足够的匹配项，提示提取数据出错的位置
            print(f"Warning: Not enough matches in item: {item.get('filename', '')} {item.get('iteration', '')}")
    try:
        # 将更新后的数据写回到新的JSON文件中
        with open(target_file, 'w') as outfile:
            json.dump(data, outfile, indent=4)
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

# 保存大模型回复数据的JSON文件路径
source_file = 'data/GeMiniProReply/GeMiniProReply.json'
# 输出文件路径
target_file = 'data/GeMiniProReply/TestcaseType.json'
extract_input_and_expectedOutput(source_file, target_file)
