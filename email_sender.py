from email.message import EmailMessage
import ssl
import smtplib
def sendEmail(subject, body):
    email_sender = "meliscem01@gmail.com"
    password = "yivexwhuvukssygw"
    email_receiver = "sandgodmand@gmail.com"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context() 

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
