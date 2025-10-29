import email
import smtplib
import filetype
from email.message import EmailMessage
password = 'uuylnkhgyhazzxkf'
sender = "ramithabet31@gmail.com"
receiver = "ramithabet31@gmail.com"

def send_email_func(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = f"Camera Feed"
    email_message.set_content("Motion Detected!")
    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype='png')

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()

















