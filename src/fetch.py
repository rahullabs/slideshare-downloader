import requests
from bs4 import BeautifulSoup
import src.helpers as hp
import datetime as dt

class Fetch():
    def __init__(self, arguments):
        super(Fetch, self).__init__()
        self.args = arguments
    
    def extractSlides(self):
        pass

    def saveImages(self, save_image = True):
        pass

    def savePdf(self):
        pass

    def start(self):
        print(self.args)
        
