import requests
import json

api_url = "https://api.deepseek.com/chat/completions"
api_key = "sk-c7ffe0af2a9048fcb3930a8e1e622750" # 换成你的

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# ==========================================
# 实验一：不加 response_format （自然发挥）
# ==========================================
print("=== 实验一：不加 response_format ===")
payload_1 = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "你是一个AI助手。"},
        {"role": "user", "content": "我叫王五，28岁，请提取我的姓名和年龄，用JSON格式返回。"}
    ]
}

res_1 = requests.post(api_url, headers=headers, json=payload_1)
ai_text_1 = res_1.json()["choices"][0]["message"]["content"]

print("【AI 原始回复的文本】:\n", ai_text_1)

print("\n【尝试直接解析 JSON】:")
try:
    data_1 = json.loads(ai_text_1)
    print("解析成功！", data_1)
except Exception as e:
    print("💥 解析失败！报错信息：", e)
    print("👉 原因：AI 给你加了废话或者代码块，导致不是纯净的 JSON。")


# ==========================================
# 实验二：加上 response_format （上枷锁）
# ==========================================
print("\n\n=== 实验二：加上 response_format ===")
payload_2 = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "你是一个AI助手。"},
        {"role": "user", "content":"我叫王五，28岁，是个AI工程师。请提取信息，必须返回包含 name, age, job 三个键的 JSON。"}
    ],
    # 👇 核心差异就这一行
    "response_format": {"type": "json_object"} 
}

res_2 = requests.post(api_url, headers=headers, json=payload_2)
ai_text_2 = res_2.json()["choices"][0]["message"]["content"]

print("【AI 原始回复的文本】:\n", ai_text_2)

print("\n【尝试直接解析 JSON】:")
try:
    data_2 = json.loads(ai_text_2)
    print("解析成功！拿到的数据是：", data_2)
    print("姓名:", data_2["name"], "| 年龄:", data_2["age"])
except Exception as e:
    print("💥 解析失败！报错信息：", e)