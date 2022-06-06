from mail_config import app
from flask_mail import Mail, Message

mail = Mail(app)

msg = Message("测试邮件", sender='1362536452@qq.com',
              recipients=["dyk2021@mail.ustc.edu.cn", ])

msg.body = "Hello!"
msg.html = '<h1> 你好！ </h1> 这是一封测试邮件。from 董董。'

with app.app_context():
    mail.send(msg)
