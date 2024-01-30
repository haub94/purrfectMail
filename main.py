from SensibleDataHandler import SensibleDataHandler
from Emailer import Emailer

sdh = SensibleDataHandler()
emailer = Emailer()

sendTo = sdh.getRecipient1()
emailSubject = "meow...meow"
emailContent = " <!DOCTYPE html <html> <head> <title>Your Email Title</title> </head> <body> <h1>Hello, This is Your Email Content</h1> <p>This is a paragraph in the email.</p> </body> </html>"

#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.

emailer.sendmail(sendTo, emailSubject, emailContent)