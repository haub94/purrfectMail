#TODO add buffer to store the images from the last 7 days, to avoid sending the same image during the week

import os
import random
from SensibleDataHandler import SensibleDataHandler
from Emailer import Emailer

PATH_TO_IMAGE_GALLERY = 'catGallery/' #add here the images from your cat
CAT_NAME = 'Minki' #use the name of your cat

sdh = SensibleDataHandler()
emailer = Emailer()

image = ''

try:
    # Get a list of all the images in the folder
    allImagesFromGallery = [f for f in os.listdir(PATH_TO_IMAGE_GALLERY) if os.path.isfile(os.path.join(PATH_TO_IMAGE_GALLERY, f))]

    # Select a random image from the list
    randomImageFromGallery = random.choice(allImagesFromGallery)

    image = PATH_TO_IMAGE_GALLERY + randomImageFromGallery

except:
    print("It seems that your catGallery-folder is empty! By default Minka will sent")
    image = "minka.jpeg" #use default

recipient = sdh.getRecipient1()

emailSubject = "meow..."
emailContent = f"{CAT_NAME} of the day."

#send the mail 
emailer.sendmail(recipient, emailSubject, emailContent, image)