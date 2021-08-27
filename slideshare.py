from src.fetch import Fetch
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--Output", default = 'downloads', help="Directory to store the slides")
parser.add_argument("-j", "--Jpeg", default = False, help="Save the Images")
parser.add_argument("-t", "--Txt", default = False, help='Download single presentation file')
parser.add_argument("-i", "--Input", default="https://www.slideshare.net/Slideshare/what-to-upload", help="Input link or file")
args = parser.parse_args()

class Slideshare():
    def __init__(self):
        self.output_dir = args.Output
        self.save_jpg = args.Jpeg
        self.from_txt = args.Txt
        self.input_files = args.Input
        self.arguments = [self.output_dir, self.save_jpg, self.from_txt, self.input_files]
    
    def download(self):
        start_fetching = Fetch(self.arguments)
        start_fetching.start()


if __name__=='__main__':
    slide = Slideshare()
    slide.download()