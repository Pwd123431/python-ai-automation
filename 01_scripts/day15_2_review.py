import requests,json,time

#1.注册平台地址
api_url = "https://api.deepseek.com/chat/completions"

#2.填写api密钥
api_key="sk-"

# 3. 设置 Headers（告诉服务器：我要发 JSON 数据，这是我的钥匙）
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

#4.设置Payload(请求体)
Payload= {
    "model":"deepseek-chat", # 选择模型（deepseek-chat 是通用对话模型）
    "messages": [
        {"role":"system","content":"你是一位资深且幽默的Python导师!"},
        {"role":"user","content":"请用一句话告诉我,Python中列表和字典的区别,并举个例子。"}
    ],
    "temperature":0.7,
    #"n":2
}

#5.记录开始时间
start_time=time.time()
print("正在呼叫Deepseek请稍等......")

#6.发送post请求
res=requests.post(api_url,headers=headers,json=Payload)

#7.记录结束时间及思考时间
end_time=time.time()
cost_time=round(end_time-start_time,2)

#8.检查是否成功（200表示成功）
if res.status_code==200:
    #把返回的字符串转化为Python字典
    result=res.json()
    print(result)
    #9.剥洋葱，提取ai答案
    ai_answers=result["choices"][0]["message"]["content"]

    print("-----AI的回答-----")
    print(ai_answers)
    print(f"本次调用共计{cost_time}秒!")
else:
    print(f"请求失败，状态码：{res.status_code}")
    print("错误信息：", res.text)    
