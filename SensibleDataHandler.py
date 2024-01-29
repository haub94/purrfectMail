import os
from dotenv import load_dotenv

load_dotenv()

class SensibleDataHandler:
    def __init__(self):
        self.GMAIL_USERNAME = os.getenv('GMAIL_USERNAME')
        self.GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')
        self.RECIPIENT1 = os.getenv('RECIPIENT1')
        
    def getSenderName(self):
        return self.GMAIL_USERNAME
    
    def getSenderAppPassword(self):
        return self.GMAIL_APP_PASSWORD
    
    def getRecipient1(self):
        return self.RECIPIENT1