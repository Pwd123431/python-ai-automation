import requests, json

api_url = "https://api.deepseek.com/chat/completions"
api_key = "sk-fde4e297a9064baab0292addeeb9404c" # 👈 这里必须是新的

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "请用 json 格式回复我一句你好"}],
    "response_format": {"type": "json_object"}
}

print("正在测试 API...")
res = requests.post(api_url, headers=headers, json=payload)
if res.status_code == 200:
    print("API 正常！回答是：", res.json()["choices"][0]["message"]["content"])
else:
    print("API 报错，状态码：", res.status_code, res.text)