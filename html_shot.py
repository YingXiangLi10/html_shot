from selenium import webdriver
import os
import requests
from lxml import etree
from PIL import Image

def generateHTML():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    url = 'https://www.liaoxuefeng.com/wiki/896043488029600/900004590234208'
    xpath = '//*[@id="x-content"]'
    response = requests.get(url, headers = headers)
    html = response.text
    html = etree.HTML(html)
    html_data = etree.tostring(html.xpath(xpath)[0], encoding='utf-8')
    # print(html_data)
    with open(r'C:\Users\lyx\Desktop\picture.html', 'wb') as f:
        f.write(html_data)

def screenShot():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--dns-prefetch-disable')
    options.add_argument('--no-referrers')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-audio')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')

    driver = webdriver.Chrome(options=options)
    driver.get(r'C:\Users\lyx\Desktop\picture.html')
    width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
    height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    driver.set_window_size(width + 100, height + 100)
    driver.save_screenshot(r'C:\Users\lyx\Desktop\image.png')
    driver.close()


def pictureCrop(piece):
    img = Image.open(r'C:\Users\lyx\Desktop\image.png')
    size = img.size
    print(size)

    weight = size[0]
    height = int(size[1] / piece)

    for i in range(piece):
        box = (0, height * i, weight, height*(i+1))
        region = img.crop(box)
        region.save('C:\\Users\\lyx\\Desktop\\image%s.png'%(i))




if __name__ == '__main__':
    generateHTML()
    screenShot()
    os.remove(r'C:\Users\lyx\Desktop\picture.html')
    pictureCrop(0)
