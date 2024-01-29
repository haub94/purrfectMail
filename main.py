import os

from mailer import Emailer

from dotenv import load_dotenv

load_dotenv()



sender = Emailer()

sendTo = os.getenv('SEND_TO')
emailSubject = "Hello World"
emailContent = "This is a test of my Emailer Class"

#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.

sender.sendmail(sendTo, emailSubject, emailContent)
print("email sent")