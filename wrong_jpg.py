import os
from PIL import Image


def main():
    files = os.listdir('wrong_img/')
    for pix in files:
        image_name = 'wrong_img/' + pix
        print(image_name)
        image = Image.open(image_name)
        image = image.convert('RGB')
        image.save(('normal_img/' + pix), 'JPEG', quality="web_low")


if __name__ == '__main__':
    main()