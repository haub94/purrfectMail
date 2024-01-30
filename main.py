import os
import random
from SensibleDataHandler import SensibleDataHandler
from Emailer import Emailer

PATH_TO_IMAGE_GALLERY = 'catGallery/' #add here the images from your cat

sdh = SensibleDataHandler()
emailer = Emailer()

image = ''

try:
    # Get a list of all the image files in the folder
    allImagesFromGallery = [f for f in os.listdir(PATH_TO_IMAGE_GALLERY) if os.path.isfile(os.path.join(PATH_TO_IMAGE_GALLERY, f))]

    # Select a random image from the list
    randomImageFromGallery = random.choice(allImagesFromGallery)

    image = PATH_TO_IMAGE_GALLERY + randomImageFromGallery

except:
    print("It seems that your catGallery-folder is empty! By default Minka will be send")
    image = "minka.jpeg" #use default

recipient = sdh.getRecipient1()

emailSubject = "meow..."
emailContent = "Minki of the day."

#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.


print("image: ", image);


#send the mail 
emailer.sendmail(recipient, emailSubject, emailContent, image)