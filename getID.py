import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import base64
def GetUUID():
    cmd = 'wmic csproduct get UUID'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n")+2
    uuid = uuid[pos1:-15]
    return uuid
#加密
def enctry(s):
    k =  '+d=d5u6ebp&_0%1lt%0$!-qmw%ceal-49ere*^yaat&_u3-$d!'
    encry_str = ""
    for i,j in zip(s,k):
        # i為字元，j為祕鑰字元
        temp = str(ord(i)+ord(j))+'.' # 加密字元 = 字元的Unicode碼 + 祕鑰的Unicode碼
        encry_str = encry_str + temp
    return encry_str
#解密
def dectry(p):
    k = '+d=d5u6ebp&_0%1lt%0$!-qmw%ceal-49ere*^yaat&_u3-$d!'
    dec_str = ""
    for i,j in zip(p.split(".")[:-1],k):
        # i 為加密字元，j為祕鑰字元
        temp = chr(int(i) - ord(j)) # 解密字元 = (加密Unicode碼字元 - 祕鑰字元的Unicode碼)的單位元組字元
        dec_str = dec_str+temp
    return dec_str
txt = "Save to clipboard!"
subprocess.run(['clip.exe'], input=txt.strip().encode('utf-16'), check=True)

#send email
'''
content = MIMEMultipart()
content["subject"] = "0623test"
content["from"] = "2835jifu.6@gmail.com"
content["to"] = "2835jifu.6@gmail.com"
content.attach(MIMEText("demo"))
with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("2835jifu.6@gmail.com", "usdqgwhhqijlxjfn")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)
'''