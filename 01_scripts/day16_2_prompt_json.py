import requests
import json,re

api_url = "https://api.deepseek.com/chat/completions"
api_key = "sk-" # 👈 记得换成你的

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 核心就在这个 payload 里！
payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "你是一个数据提取专家。"},
        {"role": "user", "content": "请提取这句话里的信息：我叫王五，今年28岁，是个AI工程师。必须返回包含 name, age, job 三个字段的 JSON。"}
    ],
    # 👇 这就是传说中的王炸参数！
    # 告诉服务器：必须返回合法的 JSON 对象
    "response_format": {"type": "json_object"}
}

res = requests.post(api_url, headers=headers, json=payload)

if res.status_code == 200:
    # 剥洋葱，拿到大模型返回的字符串
    ai_text = res.json()["choices"][0]["message"]["content"]
    
    print("--- AI 原封不动返回的文本 ---")
    print(ai_text)
    
    # 因为咱们加了魔法参数，现在可以直接把它转成 Python 字典！
    data = json.loads(ai_text)
    print("\n--- 解析成 Python 字典后 ---")
    print("姓名:", data["name"])
    print("年龄:", data["age"])
    print("职业:", data["job"])
else:
    print("报错了：", res.text)

