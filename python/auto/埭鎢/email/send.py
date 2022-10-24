# coding:utf-8

import time
import smtplib  # python 自帶
import schedule  # pip install schedule

from email.mime.text import MIMEText  # python自帶
from email.header import Header
from email.mime.multipart import MIMEMultipart  # 使用MIMEMultipart 對象


# 第三方的smtp
mail_host = 'ssl://smtp.gmail.com:465'  # 設置服務器
mail_user = 'husenior11123@gmail.com'  # SMTP 帳號：[你的gmail帳號]
mail_password = 'wdycjpatwlswsqdo'  # SMTP 密碼：[google應用程式密碼]
# smtp 开通， 授权码

sender = 'husenior11123@gmail.com'
receivers = 's1041026@gm.ncue.edu.tw'

#  MIMEText(email_content, email_type, encoding_type) -定義郵件發送內容的對象
# message =MIMEText('這是一個測試', 'plain', 'utf-8')  # 內容, 格式, 編碼格式
# message = MIMEText('<p style="color:red;">这是一个测试</p>', 'html', 'utf-8')  # 發送html 類型文件

message = MIMEMultipart()  # 實例化對象

message['From'] = Header(sender)
message['Subject'] = Header('python脚本测试', 'utf-8')  # subject -> Title
# print(message.as_string())

# 定義發送的內容 -使用附件先將內容讀取 -> 定義附件類型(流類型) -> 對附件進行名稱定義 -> 把附件附加到message內 ->
attr = MIMEText(open('send.py', 'rb').read(), 'base64', 'utf-8')
attr['Content-Type'] = 'application/octet-stream'  # 流的協議
attr['Content-Disposition'] = 'attachment;filename="send.py"'

message.attach(attr)  # 郵件附件添加完成
message.attach(MIMEText('这是一个带附件的邮件', 'plain', 'utf-8'))  # 加入郵件主內容

# 郵件發送
def send():
    try:  # 使用try-catch來捕獲發送失敗
        smtobj = smtplib.SMTP()  # 實例化協議對象
        smtobj.connect(mail_host, 465)  # SMTP 埠號：465
        smtobj.login(mail_user, mail_pass)
        smtobj.sendmail(sender, receivers, message.as_string())  # message.as_string() 加密字符串
    except smtplib.SMTPException as e:
        print('error: %s' % e)


if __name__ == '__main__':
    schedule.every(10).seconds.do(send)
    print('send start')
    while 1:  # 為何要用while loop, 及time.sleep() -> 當使用run_pending()時, 它會監測是否有任務要執行, if not, finish
        # 所以要用while loop, 使其不斷的監測是否有任務要執行
        schedule.run_pending()
        time.sleep(1)  # 因為不停地監測, 頻率太高 -> 為了減少cpu消耗, 提高性能, 需要sleep
'''
#message = MIMEText('<p style="color:red;">这是一个测试</p>', 'html', 'utf-8')

message['From'] = Header(sender)
message['Subject'] = Header('python脚本测试', 'utf-8')

'''
