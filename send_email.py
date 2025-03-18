import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "python.dev.bishwash@gmail.com"
    password = "ftvu graa nvdx kwyt"

    receiver = "python.dev.bishwash@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)