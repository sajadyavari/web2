import smtplib
import ssl,os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    user_name = "sajadyavari.ir@gmail.com"
    password = os.getenv("GMAIL")
    receiver_email = "sajad2ser@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver_email, message)
