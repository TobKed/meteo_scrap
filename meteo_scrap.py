# -*- coding: utf-8 -*-
""" Display meteogram from meteo.pl.

You just have to adjust few constants at the beginning of the script:

    UM = True / False
    COAMPS = True / False
    LEGENDS = True / False
    MODEL_UM_URL = url to meteogram webpage of the UM model
    MODEL_COAMPS_URL = url to meteogram webpage of the COAMPS model

    LEGEND_UM_URL = direct url to image of the legend of the UM model
    LEGEND_COAMPS_URL = direct url to image of the legend of the COAMPS model

    CHROMEDRIVER_PATH = path to ChromeDriver, the WebDriver for Chrome
        available on http://chromedriver.chromium.org/
"""

from selenium import webdriver
from PIL import Image, ImageTk
from urllib.request import urlopen
import tkinter as tk
import io

UM = True
COAMPS = True
LEGENDS = True
MODEL_UM_URL = 'http://www.meteo.pl/um/php/meteorogram_id_um.php?ntype=0u&id=689'
MODEL_COAMPS_URL = 'http://www.meteo.pl/php/meteorogram_id_coamps.php?ntype=2n&id=689'

LEGEND_UM_URL = 'http://www.meteo.pl/um/metco/leg_um_pl_cbase_256.png'
LEGEND_COAMPS_URL = 'http://www.meteo.pl/metco/leg4_pl.png'

CHROMEDRIVER_PATH = './chromedriver'


def get_meteogram_img_link(meteo_url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    driver.get(meteo_url)
    img = driver.find_element_by_id('meteorogram')
    meteo = img.get_attribute('src')
    driver.quit()
    print('link to meteogram image retrieved from {}'.format(meteo_url))
    return meteo


def save_meteo(direct_link, file_name):
    urllib.request.urlretrieve(get_meteogram_img_link(direct_link), file_name)


class label_with_picture():
    def __init__(self, img_url):
        self.tk_image = self.photoimage_from_url(img_url)
        self.label = tk.Label(app, image=self.tk_image, bg='#FFFBF0')

    @staticmethod
    def photoimage_from_url(img_url):
        pic_url = img_url
        image_bytes = urlopen(pic_url).read()
        data_stream = io.BytesIO(image_bytes)
        pil_image = Image.open(data_stream)
        return ImageTk.PhotoImage(pil_image)


if __name__ == '__main__':
    app = tk.Tk()
    app.title('METEO')
    app.configure(background='#FFFBF0')
    app.resizable(width=False, height=False)

    if UM:
        um = label_with_picture(img_url=get_meteogram_img_link(MODEL_UM_URL))
        um.label.grid(row=0, column=1)

    if COAMPS:
        coamps = label_with_picture(img_url=get_meteogram_img_link(MODEL_COAMPS_URL))
        coamps.label.grid(row=0, column=3)

    if UM and LEGENDS:
        um_legend = label_with_picture(img_url=LEGEND_UM_URL)
        um_legend.label.grid(row=0, column=0)

    if COAMPS and LEGENDS:
        coamps_legend = label_with_picture(img_url=LEGEND_COAMPS_URL)
        coamps_legend.label.grid(row=0, column=2)

    app.mainloop()
