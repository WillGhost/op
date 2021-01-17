#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header



host_smtp = 'smtp-mail.outlook.com'
host_port = 587


login_user = 'gre178@live.com'
password = 'erg23423m'


def send_mail(to, subject, message):
    msg = MIMEText(message)
    msg["Subject"] = Header(subject)
    msg["From"] = login_user
    msg["To"] = to
    message = msg.as_string()

    sm = smtplib.SMTP(host=host_smtp, port=host_port)
    sm.starttls()
    sm.login(login_user, password)
    sm.sendmail(login_user, to, message)
    sm.close()


if __name__ == '__main__':
    subject = 'ni niu b!!1 qing hao de 你好33336633哈哈'
    message = 'haha22333 go go谢谢2226633太好了'
    to = '54wef2@qq.com'

    send_mail(to, subject, message)



