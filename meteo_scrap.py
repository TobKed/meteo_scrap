from selenium import webdriver
from PIL import Image
import urllib.request
import tkinter

UM = True
COAMPS = True
LEGENDS = True
MODEL_UM = 'http://www.meteo.pl/um/php/meteorogram_id_um.php?ntype=0u&id=689'
MODEL_COAMPS = 'http://www.meteo.pl/php/meteorogram_id_coamps.php?ntype=2n&id=689'

METEOGRAM_UM_PATH = 'files//meteogram_um.png'
METEOGRAM_COAMPS_PATH = 'files//meteogram_coamps.png'
LEGEND_UM_PATH = 'files//static//legend_um.png'
LEGEND_COAMPS_PATH = 'files//static//legend_coamps.png'


def get_meteogram_img_link(direct_link):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path='/home/tobias/PycharmProjects/meteo_scrap/chromedriver',
                              chrome_options=chrome_options)
    driver.get(direct_link)
    img = driver.find_element_by_id('meteorogram')
    meteo = img.get_attribute('src')
    driver.quit()
    print(meteo)
    return meteo


def save_meteo(direct_link, file_name):
    urllib.request.urlretrieve(get_meteogram_img_link(direct_link), file_name)


class frame_with_picture():
    def __init__(self, pic_path):
        pic_width, pic_height = Image.open(pic_path).size
        self.frame = tkinter.Canvas(bg='black', width=pic_width, height=pic_height)
        self.image = tkinter.PhotoImage(file=pic_path)
        image_ = self.frame.create_image(0, 0, anchor=tkinter.NW, image=self.image)


if __name__ == '__main__':
    app = tkinter.Tk()
    app.title('METEO')
    app.configure(background='white')
    app.resizable(width=False, height=False)

    if UM:
        um = frame_with_picture(pic_path=METEOGRAM_UM_PATH)
        um.frame.grid(row=0, column=1)

    if COAMPS:
        coamps = frame_with_picture(pic_path=METEOGRAM_COAMPS_PATH)
        coamps.frame.grid(row=0, column=3)

    if UM and LEGENDS:
        um_legend = frame_with_picture(pic_path=LEGEND_UM_PATH)
        um_legend.frame.grid(row=0, column=0)

    if COAMPS and LEGENDS:
        coamps_legend = frame_with_picture(pic_path=LEGEND_COAMPS_PATH)
        coamps_legend.frame.grid(row=0, column=2)

    app.mainloop()
