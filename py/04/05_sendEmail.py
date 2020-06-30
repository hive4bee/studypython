import smtplib
from email.mime.text import MIMEText
from email.header import Header

#MIMEText 객체로 메일을 생성한다.
msg=MIMEText("메일 본문입니다.")

#제목에 한글이 포함될 경우 Header 객체를 사용한다.
msg['Subject']=Header("메일 제목입니다.","utf-8")
msg['From']="sender@gmail.com"
msg['To']="receiver@naver.com"

#SMTP()의 첫 번째 매개변수에 SMTP 서버의 호스트 이름을 지정한다.
with smtplib.SMTP_SSL("smtp.gmail.com") as smtp:
    #smtp.starttls()
    smtp.login("sender@gmail.com","account_pwd")
    #메일을 전송한다.
    smtp.send_message(msg)