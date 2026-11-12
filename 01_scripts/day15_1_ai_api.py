import requests
import json,time

# 1. 填写你注册平台的请求地址
# DeepSeek的地址是这个，如果你用别的，去查一下对应的API文档
api_url = "https://api.deepseek.com/chat/completions"

# 2. 填入你的真实 API Key (注意不要发给别人！)
api_key = "sk-"

# 3. 设置 Headers（告诉服务器：我要发 JSON 数据，这是我的钥匙）
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 4. 设置 Payload（请求体）
payload = {
    "model": "deepseek-chat",  # 选择模型（deepseek-chat 是通用对话模型）
    "messages": [
        {"role": "system", "content": "你是一个资深且幽默的Python导师。"},
        {"role": "user", "content": "请用一句话告诉我,Python中列表和字典的区别,并举个例子。"}
    ],
    "temperature": 0.7 # 0最严谨，1最放飞自我
}

# 5. 记录开始时间
start_time = time.time()
print("正在呼叫 DeepSeek,请稍等...\n")

# 6. 发送 POST 请求（注意：这里用 post，因为你带了一大包数据过去）
response = requests.post(api_url, headers=headers, json=payload)

# 7. 记录结束时间
cost_time = round(time.time() - start_time, 2)

# 8. 检查是否成功 (200 表示成功)
if response.status_code == 200:
    # 把返回的字符串变成 Python 字典
    result = response.json()
    
    # 9. 剥洋葱：提取 AI 的回答
    ai_answer = result["choices"][0]["message"]["content"]
    
    print("====== AI 的回答 ======")
    print(ai_answer)
    print(f"\n(本次调用耗时 {cost_time} 秒)")
else:
    print(f"请求失败，状态码：{response.status_code}")
    print("错误信息：", response.text)
