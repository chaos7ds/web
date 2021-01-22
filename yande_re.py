"""
작성자	: chaos7ds
작성일	: 2021.01.22 ~
version : 1.0.0
"""
import urllib.request
from bs4 import BeautifulSoup


def get_url(p):
    return f"https://yande.re/post?page={p}&tags=yuuki_mikan"


page_num = 0
while True:
    page_num += 1
    # 웹페이지의 소스를 가져온다.
    url = get_url(page_num)
    fp = urllib.request.urlopen(url)
    source = fp.read()
    fp.close()

    # 소스에서 img_area 클래스 하위의 소스를 가져온다.
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("a", class_="directlink largeimg")

    if len(soup) < 1:
        break

    # 이미지 경로를 받아 로컬에 저장한다.
    imageNum = 0
    for i in soup:
        imageNum += 1
        imgURL = i.attrs["href"]
        urllib.request.urlretrieve(imgURL, f"C:/Users/chaos/Desktop/새 폴더/{str(page_num):>05}_{str(imageNum):>05}.jpg")
        print(imageNum)
        print(imgURL)

print("Done")
