import requests
from bs4 import BeautifulSoup
import src.helpers as hp
import shutil
from PIL import Image
from tqdm import tqdm
import os

class Fetch():
    def __init__(self, arguments):
        super(Fetch, self).__init__()
        self.args = arguments
        hp.imageDirectory(self.args[0])
    
    def directory_check(self, slide_name):
        self.slide_folder_name = slide_name.split('/')[-1]
        self.slide_folder = self.args[0]+"/"+ self.slide_folder_name
        hp.imageDirectory(self.slide_folder)
        self.pdf_dir = self.slide_folder+'/pdf'
        self.img_dir = self.slide_folder+'/jpg'
        hp.imageDirectory(self.pdf_dir)
        hp.imageDirectory(self.img_dir)


    def individual_link_slides(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        slides = soup.find_all("div", {"id":"slide_container"})
        img_link = []
        for img in slides[0].find_all('img', alt=True):
            if not img['src']:
                if not img['data-original']:
                    pass
                if img['data-original']:
                    img_link.append(img['data-original'])
            elif not img['data-original']:
                if not img['src']:
                    pass
                if img['src']:
                    img_link.append(img['src'])
        self.dld_img = []
        for total_slides in tqdm(range(len(img_link))):
            src_link = img_link[total_slides].split('?')[0:img_link[total_slides].find('?')-1]
            self.download_slide_images(src_link[0], self.img_dir)   
        self.savePdf(self.slide_folder_name+".pdf")

    def savePdf(self, filename):
        im_list = []
        for imgs in self.dld_img:
            im = Image.open(imgs)
            im_list.append(im)
        pdf_file = self.pdf_dir + "/" + filename
        im_list[0].save(pdf_file, "PDF", resolution=100.0, save_all=True, append_images=im_list[1:])       
        if not self.args[1]:
            for imgs in self.dld_img:
                os.remove(imgs)   

    def download_slide_images(self, image_url, output_dir):
        filename = image_url.split('/')[-1]
        r = requests.get(image_url, stream = True)
        output = output_dir+ "/" + filename
        if r.status_code == 200:
            r.raw.decode_content = True
            self.dld_img.append(output)
            with open(output,'wb') as f:
                shutil.copyfileobj(r.raw, f)


    def text_handler(self):
        file = open(self.args[-1], 'r+')
        self.tot_slide_link = file.readlines()
        file.close()

    def check_type_input(self):
        if self.args[2]:
            self.text_handler()
            for link_no in range(len(self.tot_slide_link)):
                self.directory_check(self.tot_slide_link[link_no].strip('\n'))
                self.individual_link_slides(self.tot_slide_link[link_no].strip('\n'))
        elif not self.args[2]:
            self.directory_check(self.args[-1])
            self.individual_link_slides(self.args[-1])

    def start(self):
        self.check_type_input()
        
