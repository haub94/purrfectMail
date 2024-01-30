from SensibleDataHandler import SensibleDataHandler
from Emailer import Emailer

sdh = SensibleDataHandler()
emailer = Emailer()

image = "minka.jpeg"
recipient = sdh.getRecipient1()

emailSubject = "meow...meow"
emailContent = "Minki of the day."

#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.

emailer.sendmail(recipient, emailSubject, emailContent, image)