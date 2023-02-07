import smtplib,ssl,os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")

    receiver = os.environ.get("RECEIVER")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

