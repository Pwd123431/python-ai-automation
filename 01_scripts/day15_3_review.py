import time,json,requests

#让 AI 拥有记忆（多轮对话）

api_url="https://api.deepseek.com/chat/completions"
api_key="sk-c7ffe0af2a9048fcb3930a8e1e622750"

headers={
    "Content-Type":"application/json",
    "Authorization": f"Bearer {api_key}"
}

# 【关键点1】准备一个空列表，这就是 AI 的记忆！
messages = [
    {"role": "system", "content": "你是一个极其聪明的AI助手。"}
]

print("你的AI助手已就绪,输入'q'退出!")

while True:
    u_input=input("你：")
    if u_input.lower()=='q':
        print("退出成功!")
        break

    messages.append({"role":"user","content":u_input})
    Payload = {
        "model": "deepseek-chat",
        # 【关键点3】把带着历史记录的 messages 整个发过去！
        "messages": messages,
        "temperature": 0.7
    }

    print("正在思考......")
    s_time=time.time()
    res=requests.post(api_url,headers=headers,json=Payload)
    e_time=time.time()
    c_time=round(e_time-s_time,2)

    if res.status_code==200:
        result=res.json()
        a_answers=result['choices'][0]['message']['content']
        print(f"AI:{a_answers}")
        print(f"本次思考{c_time}秒!")

        # 【关键点4】把 AI 的回答也追加到记忆列表里！
        messages.append({"role":"assistant","content":a_answers})
    else:
        print("报错了!",res.text)