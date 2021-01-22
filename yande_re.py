"""
작성자	: chaos7ds
작성일	: 2021.01.22 ~
version : 1.0.0
"""
import os
import getpass

import urllib.request
from bs4 import BeautifulSoup


class Web:
    def __init__(self):
        # 변수 설정
        self.site = "yande.re"
        self.class_ = "directlink largeimg"
        self.page_num = 0
        self.tag = input("Tag :\t")

        if self.tag == '':
            print("Wrong tag")
        else:
            self.check_dir()
            self.execute()

    def check_dir(self):
        self.dir = 'C://Users/' + getpass.getuser() + f"/Desktop/downloaded_img/{self.site}/{self.tag}/"
        if not os.path.isdir(self.dir):
            os.makedirs(os.path.join(self.dir))

    def get_url(self, p, t):
        return f"https://{self.site}/post?page={p}&tags={t}"

    def execute(self):
        while True:
            self.page_num += 1

            # 웹페이지의 소스 가져오기
            url = self.get_url(self.page_num, self.tag)
            fp = urllib.request.urlopen(url)
            source = fp.read()
            fp.close()

            # 소스 분석
            soup = BeautifulSoup(source, 'html.parser')
            soup = soup.findAll("a", class_=self.class_)

            if len(soup) < 1:
                break

            # 이미지 경로를 받아 저장한다.
            imageNum = 0
            for i in soup:
                imageNum += 1
                print(f"page:\t{self.page_num:>5}\t\tnum:\t{imageNum:>5}")

                imgURL = i.attrs["href"]
                d = self.dir + f"{str(self.page_num):>05}_{str(imageNum):>05}.jpg"
                urllib.request.urlretrieve(imgURL, d)


"""
test tag : na_wa_holangi-nim
"""

if __name__ == "__main__":
    Web()
