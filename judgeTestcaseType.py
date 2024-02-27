import json
from typing import List

from data.sourceCode.buggyFunction.Rating_Increase import rating_increase as Buggy_Rating_Increase
from data.sourceCode.buggyFunction.Swap_and_Delete import swap_and_delete as Buggy_Swap_and_Delete
from data.sourceCode.buggyFunction.Game_with_Multiset import game_with_multiset as Buggy_Game_with_Multiset
from data.sourceCode.buggyFunction.Array_Collapse import array_collapse as Buggy_Array_Collapse
from data.sourceCode.buggyFunction.Matrix_Problem import matrix_problem as Buggy_Matrix_Problem
from data.sourceCode.correctFunction.Rating_Increase import rating_increase as Correct_Rating_Increase
from data.sourceCode.correctFunction.Swap_and_Delete import swap_and_delete as Correct_Swap_and_Delete
from data.sourceCode.correctFunction.Game_with_Multiset import game_with_multiset as Correct_Game_with_Multiset
from data.sourceCode.correctFunction.Array_Collapse import array_collapse as Correct_Array_Collapse
from data.sourceCode.correctFunction.Matrix_Problem import matrix_problem as Correct_Matrix_Problem

# 检查input是否符合IT
def judge_it_rating_increase(input: List[str]) -> bool:
    # 尝试将第一行转换为整数，并检查其是否在1到10000之间
    try:
        t = int(input[0])
        if not 1 <= t <= 10000:
            return False
    except ValueError:
        return False  # 如果转换失败或不在范围内，返回False
    if len(input) != 1 + t:
        return False
    # 检查每个测试用例
    for testcase in input[1:]:
        # 检查长度
        if not 2 <= len(testcase) <= 8:
            return False
        # 检查是否只包含数字
        if not testcase.isdigit():
            return False
        # 检查是否不以零开头
        if testcase[0] == '0':
            return False
    # 如果所有检查都通过，则返回True
    return True


def judge_it_swap_and_delete(input: List[str]) -> bool:
    # 尝试将第一行转换为整数，并检查其是否在1到10000之间
    try:
        t = int(input[0])
        if not 1 <= t <= 10 ** 4:
            return False
    except ValueError:
        return False  # 如果转换失败或不在范围内，返回False
    if len(input) != 1 + t:
        return False
    # 检查总长度是否不超过2 * 10^5
    total_length = sum(len(testcase) for testcase in input[1:])
    if total_length > 2 * 10 ** 5:
        return False

    # 检查每个测试用例
    for testcase in input[1:]:
        # 检查长度
        if not 1 <= len(testcase) <= 2 * 10 ** 5:
            return False
        # 检查是否为二进制字符串
        if not set(testcase).issubset({'0', '1'}):
            return False

    # 如果所有检查都通过，则返回True
    return True


def judge_it_game_with_multiset(input: List[str]) -> bool:
    # 尝试将第一行转换为整数，并检查其是否在1到10^5之间
    try:
        m = int(input[0])
        if not 1 <= m <= 10 ** 5:
            return False
    except ValueError:
        return False  # 如果转换失败或不在范围内，返回False
    if len(input) != 1 + m:
        return False
    # 检查每一行查询是否符合要求
    for line in input[1:]:
        try:
            t_i, v_i = map(int, line.split())
            # 如果 t_i = 1，则检查 0 ≤ v_i <= 29
            if t_i == 1 and not (0 <= v_i <= 29):
                return False
            # 如果 t_i = 2，则检查 0 ≤ v_i ≤ 10^9
            if t_i == 2 and not (0 <= v_i <= 10 ** 9):
                return False
            # 如果 t_i 不是 1 或 2，则返回False
            if t_i not in [1, 2]:
                return False
        except ValueError:
            return False  # 如果转换失败或者行中没有两个整数，返回False

    # 如果所有检查都通过，则返回True
    return True


def judge_it_array_collapse(input: List[str]) -> bool:
    # 尝试将第一行转换为整数，并检查其是否在1到10^4之间
    try:
        t = int(input[0])
        if not 1 <= t <= 10 ** 4:
            return False
    except ValueError:
        return False  # 如果转换失败或不在范围内，返回False
    if len(input) != 1 + t * 2:
        return False
    # 初始化n的总和计数器
    total_n = 0

    # 索引从1开始，因为第0个元素是t
    index = 1
    for _ in range(t):
        # 检查是否有足够的行
        if index >= len(input):
            return False

        # 尝试将当前行转换为整数n，并检查其是否在1到3 * 10^5之间
        try:
            n = int(input[index])
            if not 1 <= n <= 3 * 10 ** 5:
                return False
        except ValueError:
            return False  # 如果转换失败或不在范围内，返回False

        # 增加n的总和
        total_n += n

        # 检查n的总和是否超过了3 * 10^5
        if total_n > 3 * 10 ** 5:
            return False

        # 移动到包含n个整数的行
        index += 1

        # 检查是否有足够的行
        if index >= len(input):
            return False

        # 获取该行的整数，并检查它们是否互不相同
        integers = input[index].split()
        if len(integers) != n:
            return False  # 如果整数的数量不等于n，返回False

        # 尝试将整数转换为int，并检查范围
        try:
            integer_values = [int(value) for value in integers]
            if not all(1 <= value <= 10 ** 9 for value in integer_values):
                return False
            if len(set(integer_values)) != n:
                return False  # 如果整数不是互不相同的，返回False
        except ValueError:
            return False  # 如果转换失败，返回False

        # 移动到下一个测试用例的第一行
        index += 1

    # 如果所有检查都通过，则返回True
    return True


def judge_it_matrix_problem(input: List[str]) -> bool:
    # 解析第一行的n和m
    try:
        n, m = map(int, input[0].split())
        if not (2 <= n <= 50) or not (2 <= m <= 50):
            return False
    except ValueError:
        return False  # 如果转换失败或者不在范围内，返回False
    if len(input) != 1 + n + 2:
        return False
    # 检查后续的n行，每行应该有m个0或1的整数
    for i in range(1, n + 1):
        try:
            row = list(map(int, input[i].split()))
            if len(row) != m or any(a_ij < 0 or a_ij > 1 for a_ij in row):
                return False
        except ValueError:
            return False  # 如果转换失败或者不符合条件，返回False

    # 检查包含n个整数的下一行
    try:
        a_values = list(map(int, input[n + 1].split()))
        if len(a_values) != n or any(A_i < 0 or A_i > m for A_i in a_values):
            return False
    except ValueError:
        return False  # 如果转换失败或者不符合条件，返回False

    # 检查包含m个整数的下一行
    try:
        b_values = list(map(int, input[n + 2].split()))
        if len(b_values) != m or any(B_i < 0 or B_i > n for B_i in b_values):
            return False
    except ValueError:
        return False  # 如果转换失败或者不符合条件，返回False

    # 如果所有检查都通过，则返回True
    return True


# 检查是否符合FT-IA、FT-Ia、FT-ia、IncorrectPT、CorrectPT
def judge_test_case_type(buggy_output, correct_output, expected_output):
    if buggy_output != expected_output and expected_output == correct_output and buggy_output != correct_output:
        return "FT-IA"
    if buggy_output != expected_output and expected_output != correct_output and buggy_output != correct_output:
        return "FT-Ia"
    if buggy_output != expected_output and expected_output != correct_output and buggy_output == correct_output:
        return "FT-ia"
    if buggy_output == expected_output:
        if buggy_output != correct_output:
            return "IncorrectPT"
        elif buggy_output == correct_output:
            return "CorrectPT"


def processing(source_file):
    # 打开 JSON 文件并读取数据
    with open(source_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 遍历 JSON 数据中的每一项
    for item in data:
        # 提取 filename、input、replyStage1 和 expectedOutput
        filename = item.get('filename', '')
        input_data = item.get('input', [])
        replyStage1 = item.get('replyStage1', '')
        if replyStage1 == "no":
            testcaseType = "noBugs"
            item['testcaseType'] = testcaseType
        else:
            expected_output = item.get('expectedOutput', [])
            buggy_output = []
            correct_output = []
            if filename == "Rating_Increase.py":
                if judge_it_rating_increase(input_data) == False:
                    testcaseType = "IT"
                else:
                    buggy_output = Buggy_Rating_Increase(input_data)
                    correct_output = Correct_Rating_Increase(input_data)
                    testcaseType = judge_test_case_type(buggy_output, correct_output, expected_output)
            if filename == "Swap_and_Delete.py":
                if judge_it_swap_and_delete(input_data) == False:
                    testcaseType = "IT"
                else:
                    buggy_output = Buggy_Swap_and_Delete(input_data)
                    correct_output = Correct_Swap_and_Delete(input_data)
                    testcaseType = judge_test_case_type(buggy_output, correct_output, expected_output)
            if filename == "Game_with_Multiset.py":
                if judge_it_game_with_multiset(input_data) == False:
                    testcaseType = "IT"
                else:
                    buggy_output = Buggy_Game_with_Multiset(input_data)
                    correct_output = Correct_Game_with_Multiset(input_data)
                    testcaseType = judge_test_case_type(buggy_output, correct_output, expected_output)
            if filename == "Array_Collapse.py":
                if judge_it_array_collapse(input_data) == False:
                    testcaseType = "IT"
                else:
                    buggy_output = Buggy_Array_Collapse(input_data)
                    correct_output = Correct_Array_Collapse(input_data)
                    testcaseType = judge_test_case_type(buggy_output, correct_output, expected_output)
            if filename == "Matrix_Problem.py":
                if judge_it_matrix_problem(input_data) == False:
                    testcaseType = "IT"
                else:
                    buggy_output = Buggy_Matrix_Problem(input_data)
                    correct_output = Correct_Matrix_Problem(input_data)
                    testcaseType = judge_test_case_type(buggy_output, correct_output, expected_output)
            item['testcaseType'] = testcaseType
            item['buggy_output'] = buggy_output
            item['correct_output'] = correct_output
    try:
        # 将修改后的数据写回JSON文件
        with open(source_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("结果已成功写入"+source_file)
    except FileNotFoundError:
        # 文件未找到时的异常处理
        print(f"错误：找不到文件或无法打开文件 '{source_file}'。")
    except IOError:
        # 文件读写错误的异常处理
        print(f"错误：写入文件 '{source_file}' 时发生错误。")
    except Exception as e:
        # 其他异常的处理
        print(f"发生未知错误：{e}")


# 调用函数并打印结果
# 用于判断测试用例类型源文件
source_file = "data/GeMiniProReply/TestcaseType.json"
processing(source_file)
