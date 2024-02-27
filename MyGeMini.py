import base64
import requests
import json

# 模型参数
API_KEY = 'AIzaSyA5sC_73x_0zsbUfqZJnET_m3z1jsCF9hQ'
# 设置模型参数和过滤规则 https://ai.google.dev/api/rest/v1beta/SafetySetting?hl=zh-cn#HarmBlockThreshold
safetySettings = {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"  # 默认BLOCK_ONLY_HIGH，屏蔽高危险的生成
}
generationConfig = {
    "stopSequences": [
        "Title"
    ],
    "temperature": 0.5,
    "maxOutputTokens": 4096,
    "topP": 0.8,
    "topK": 10
}
# 提问大模型所需program文件
buggy_code_file_path = "data/sourceCode/json/buggy.json"
# 保存大模型回复数据文件名
target_file = "data/GeMiniProReply/GeMiniProReply.json"
# 提问大模型所需暂时program文件、用于补充替换不理想的大模型回复
buffer_buggy_code_file_path = "data/sourceCode/json/Rating_Increase.json"
# 保存大模型回复数据暂时文件名
buffer_target_file = "data/GeMiniProReply/bufferReply.json"
# 模型对话数据
def get_data_stage1(program):
    data_stage1 = {
        'safetySettings': safetySettings,  # 假设safetySettings已经定义
        'generationConfig': generationConfig,  # 假设generationConfig已经定义
        "contents": [
            {
                'role': 'user',
                "parts": [
                    {
                        "text": "Does the following program have bug(s)?Directly answer yes or no, do not provide unnecessary explanations.'program':"
                                + program
                    }
                ]
            }
        ]
    }
    return data_stage1


def get_data_stage2(program):
    data_stage2 = {
        'safetySettings': safetySettings,
        'generationConfig': generationConfig,
        "contents": [
            {
                'role': 'user',
                "parts": [
                    {
                        "text": "Does the following program have bug(s)?Directly answer yes or no, do not provide unnecessary explanations.'program':"
                                + program}
                ]
            },
            {
                'role': 'model',
                "parts": [
                    {"text": "yes"}
                ]
            },
            {
                'role': 'user',
                "parts": [
                    {
                        "text": "Generate a test case that triggers the bug(s),Directly provide the input and expected output of the test case that triggers the program defect, without unnecessary explanation"}
                ]
            },
        ]
    }
    return data_stage2


def gemini_pro_stream(API_KEY, data):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:streamGenerateContent?key={API_KEY}"
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
    if response.status_code != 200:
        raise ValueError("Failed to generate response: " + response.text)
    # print(response.text)
    for line in response.iter_lines():
        if b"text" in line:
            # print(line.decode('utf-8'))
            # 使用split(':', 1)将字符串分割成两部分，只在第一个冒号处分割
            parts = line.decode('utf-8').split(':', 1)
            if len(parts) > 1:  # 确保字符串中存在冒号
                # parts[1]包含第一个冒号之后的所有内容
                yield json.loads(parts[1])


def getGeMiniResult(data_stage):
    # 多轮对话（聊天）
    result = ""
    for i in gemini_pro_stream(API_KEY, data_stage):
        result = result + i
    return result


# 保存记录大模型回复
def append_to_json_file(new_data,target_file):
    try:
        # 第一步：以读写模式打开文件
        with open(target_file, 'r+') as file:
            # 第二步：加载现有数据
            data = json.load(file)

            # 第三步：追加新的内容
            data.append(new_data)

            # 移动文件指针到文件的开头
            file.seek(0)

            # 第四步：写回修改后的数据到文件
            json.dump(data, file, indent=4)

            # 截断文件，移除追加数据前的残余数据
            file.truncate()

    except Exception as e:
        print(f"Error updating JSON file: {e}")


def processing(source_file,target_file,loop_num):
    # 读取遍历源buggy代码json文件
    with open(source_file, 'r') as file:
        data = json.load(file)
        for item in data:
            filename = item.get("filename", "")
            program = item.get("program", "")
            for i in range(1, loop_num+1):
                iteration = i
                data_stage1 = get_data_stage1(program)
                replyStage1 = getGeMiniResult(data_stage1)
                replyStage2 = ""
                if replyStage1 == "yes":
                    data_stage2 = get_data_stage2(program)
                    replyStage2 = getGeMiniResult(data_stage2)
                new_data = {
                    "filename": filename,
                    "iteration": iteration,
                    "replyStage1": replyStage1,
                    "replyStage2": replyStage2
                }
                append_to_json_file(new_data,target_file)
                print(new_data)


processing(buggy_code_file_path,target_file,10)
