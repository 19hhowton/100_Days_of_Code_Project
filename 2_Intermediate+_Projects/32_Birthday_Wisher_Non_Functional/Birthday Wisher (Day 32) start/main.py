import smtplib

my_email = "h92952845@gmail.com"
# password = "uTLM#KBxm+82~u"
# tekj njki nngp mpcp
password = "tekjnjkinngpmpcp"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_address="19hhowton@gmail.com", msg="Hello")
connection.close()