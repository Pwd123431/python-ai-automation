from fastapi import FastAPI
import sqlite3

app = FastAPI()

# 把之前的 API Key 和地址写在这
api_url = "https://api.deepseek.com/chat/completions"
api_key = "sk-c7ffe0af2a9048fcb3930a8e1e622750"

# 1. 这里用 @app.post，因为我们要给 AI 发送数据
@app.post("/chat")
def chat_with_ai(user_message: str):
    # 组装请求头
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # 组装请求体（注意，我们直接把网页传进来的 user_message 放进去）
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个AI助手。"},
            {"role": "user", "content": user_message}
        ]
    }
    
    # 发送请求给 DeepSeek
    res = requests.post(api_url, headers=headers, json=payload)
    
    if res.status_code == 200:
        result = res.json()
        ai_answer = result["choices"][0]["message"]["content"]
        # 把 AI 的回答打包成字典返回给网页
        return {"reply": ai_answer}
    else:
        return {"error": "AI 呼叫失败"}