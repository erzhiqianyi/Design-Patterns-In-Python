import smtplib
from email.mime.text import MIMEText


def send_email(subject, message, from_address, *to_address,
               host='localhost', port=1025, **headers):
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_address
    for header, value in headers.items():
        email[header] = value
    sender = smtplib.SMTP(host, port)
    for address in to_address:
        del email['To']
        email['To'] = address
        sender.sendmail(from_address, address, email.as_string())
    sender.quit()
