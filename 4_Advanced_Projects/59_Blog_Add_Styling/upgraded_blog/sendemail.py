from email.message import EmailMessage
import ssl
import smtplib

# def send_email(name, email, phone, message):
#         email_sender = "h92952845@gmail.com"
#         email_password = 'onof bpku kzhy ktpa'
#         email_receiver = "19hhowton@gmail.com"

#         subject = f"Check out the new message from {name}"

#         email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"       
#         em = EmailMessage()
#         em["From"] = email_sender
#         em["To"] = email_receiver
#         em["Subject"] = subject
#         em.set_content = email_message

#         context = ssl.create_default_context()

#         with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#                 smtp.login(email_sender, email_password)
#                 smtp.sendmail(email_sender, email_receiver, em.as_string())

def send_email(name, email, phone, message):
        email_sender = "h92952845@gmail.com"
        email_password = 'onof bpku kzhy ktpa'
        email_receiver = "19hhowton@gmail.com"

        email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(email_sender, email_password)
                connection.sendmail(email_sender, email_receiver, email_message)
        