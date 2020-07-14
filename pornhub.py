# -*- coding: utf-8 -*-
import os
import re

import requests


class Pornhub():
    def __init__(self, url):
        self.url = url
        self.rootpath = down_path + "/"

    def parse_html(self, url):
        resp = requests.get(url, headers=random_header(), timeout=0.1)
        return resp.text

    def save_mp4(self, item):
        if item["quality_720p"]:
            url = item["quality_720p"]
        else:
            url = item["quality_480p"]
        file_path = self.rootpath + re.sub(r"[/\\:*?\"<>|]", "_", item["video_title"]) + ".mp4"
        self.download_from_url(url, file_path, random_header())

    def download_from_url(self, url, filepath, headers):
        print("开始下载:", filepath)
        with open(filepath, 'wb') as f:
            f.write(requests.get(url, headers,timeout=0.1).content)

    def run(self):
        try:
            url = self.url
            html_str = self.parse_html(url)
            item = {}
            item["video_title"] = re.findall('"video_title":"(.*?)",', html_str)[0]
            item["quality_720p"] = re.findall('"quality_720p":"(.*?)",', html_str)
            if item['quality_720p']:
                item["quality_720p"] = item["quality_720p"][0].replace('\\', '')
            item["quality_480p"] = re.findall('"quality_480p":"(.*?)",', html_str)
            if item['quality_480p']:
                item["quality_480p"] = item["quality_480p"][0].replace('\\', '')

            self.save_mp4(item)
        except Exception as e:
            pass


down_path = "D:/ph/other"


def random_header():
    return {
        'cookie': "ua=237aa6249591b6a7ad6962bc73492c77; platform_cookie_reset=pc; platform=pc; bs=kkfbi66h9zevjeq5bt27j0rvno182xdl; ss=205462885846193616; RNLBSERVERID=ded6699",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }


download_urls = [
    "https://cn.pornhub.com/view_video.php?viewkey=ph5ebbe3985a3fd",
    "https://cn.pornhub.com/view_video.php?viewkey=ph5dc135a0b5f78",
    "https://cn.pornhub.com/view_video.php?viewkey=ph5c33a2296e92d",
    "https://cn.pornhubpremium.com/view_video.php?viewkey=ph5d55ac31a7682",
]

if __name__ == '__main__':
    if not os.path.exists(down_path):
        os.makedirs(down_path)
    print("读取存放目录为:", down_path)
    try:
        print("将要爬取的链接为:")
        for url in download_urls:
            print(url)
        for url in download_urls:
            p = Pornhub(url)
            p.run()

    except Exception as e:
        print("\n*" * 20)
        print("程序运行错误:", e)
        print("*" * 20, "\n")
    finally:
        print("QQ: 2416447718")
        print("QQ: 2470571458")
        print("TG: @porsms")
