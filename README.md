# sendMail
python smtp发送邮件 带文本附件和图片附件

# 基本信息
smtp_server = 'smtp.mxhichina.com'  #smtp服务地址  
from_mail = 'your email'   #邮箱账号  
mail_passwd = 'your password'  #密码 有的邮箱比如qq|163需要填的是客户端授权码  
to_mail = ['email1@qq.com', 'email2@qq.com']  #发送目标  
subject = '任务' + getnow() #发送邮件主题  

content变量的内容为邮件正文内容  

# 文本附件
见attach注释下内容

# 图片附件
见picture注释下内容 这里需要注意乱码问题

# 使用方法
需要发送文本或者图片附件 讲对应open的文件路径换为需要替换的文件路径即可  
更改邮件发送内容 只需要更改 content变量内容即可  
基于python3 直接cmd执行> python sendemail.py既可以看到发送信息  
