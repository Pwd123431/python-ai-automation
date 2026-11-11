import smtplib
from email.mime.text import MIMEText

# 1. 你的邮箱账号信息
smtp_server = "smtp.qq.com"       # 👈 这里必须是纯域名！
sender_email = "3506226650@qq.com"   
auth_code = "bnsnnnvxiwzxdbjg"  # 👈 别填汉字，要真实的授权码！
receiver_email = "pwt1379@outlook.com" 

# 2. 构造邮件内容
msg = MIMEText("你的AI程序已经成功跑完了1000条数据提取!", 'plain', 'utf-8')
msg['Subject'] = '【自动化通知】AI任务完成'
msg['From'] = sender_email
msg['To'] = receiver_email

# 3. 登录服务器并发送
print("正在连接邮箱服务器...")
try:
    # QQ邮箱使用 465 端口，开启 SSL 加密
    server = smtplib.SMTP_SSL(smtp_server, 465)
    
    # 登录
    server.login(sender_email, auth_code)
    
    # 发送
    server.sendmail(sender_email, [receiver_email], msg.as_string())
    print("邮件发送成功！快去查收吧。")
    
except Exception as e:
    print("发送失败，报错信息：", e)