from SensibleDataHandler import SensibleDataHandler
from Emailer import Emailer

sdh = SensibleDataHandler()
emailer = Emailer()

sendTo = sdh.getRecipient1()
emailSubject = "meow...meow"
emailContent = "Minki is the best cat in the world!"

#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.

emailer.sendmail(sendTo, emailSubject, emailContent)