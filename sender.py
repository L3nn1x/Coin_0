import smtplib, ssl


def send(message, passwd, senderGmail, reciverGmail):
    try:




        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = senderGmail
        receiver_email = reciverGmail
        password = passwd
        message = message

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
