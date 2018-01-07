# vim*:fileencoding=utf8
from django.core.management.base import BaseCommand
import pickle
import requests
from bs4 import BeautifulSoup
import time
import math
import sys
import MeCab

x_train = []
y_train = []

"""
type_list:
 ・ 各カテゴリの記事のindex
 ・ 左から「エンタメ],「スポーツ」,「おもしろ」,「国内」,「海外」,
 「コラム」,「IT・科学」,「グルメ」
"""
type_list = [[1, 9, 10, 11, 12, 13, 14, 15, 17],
             [2, 18, 51, 19, 21, 22, 43, 44, 47, 48, 54],
             [23, 24, 25],
             [26, 27, 28],
             [29, 30],
             [6, 31, 32, 33, 42],
             [7, 34, 35, 36, 37, 52],
             [38,39,40,41]]

"""
  スクレイピングのプロセス
  ・urlの右に番号を付け加える
  ・BeautifulSoupを使用してアクセス・要素抽出
  ・記事のカテゴリと全テキストを書き込み
  ・(記事の全文章,カテゴリ)となるようにx_train、y_trainに文字列を保存する
  ・pickleファイルに保存する
"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('start scrapying gunosy news')
        for type in type_list:
            for i in type:
                print(i)
                target_url = "https://gunosy.com/categories/"
                target_url += str(i)
                # page数が1 ~ 5のため
                for j in range(1, 6):
                    check_url = target_url + "?page=" + str(j)
                    r = requests.get(check_url)  # requestsを使って、webから取得
                    time.sleep(1)
                    soup = BeautifulSoup(r.text, 'lxml')  # 要素を抽出
                    categories = []
                    for a in soup.find_all("a"):
                        for span in a.find_all("span", itemprop="title"):
                            categories.append(span.text)
                    for div in soup.find_all(
                      "div", class_="article_list gtm-click"):
                        for _div in div.find_all("div", class_="list_title"):
                            for a in _div.find_all("a"):
                                url = a.get('href')
                                r = requests.get(url)
                                time.sleep(1)
                                soup = BeautifulSoup(r.text, 'lxml')  # 要素を抽出
                                for div in soup.find_all(
                                  "div", class_="article gtm-click"):
                                    text = ""
                                    for p in div.find_all("p"):
                                        text += p.text
                                    x_train.append(text)
                                    y_train.append(categories[1])
        # save scrapied data as pkl file
        with open('x_train_5.pkl', 'wb') as f:
            pickle.dump(x_train, f)
        with open('y_train_5.pkl', 'wb') as f:
            pickle.dump(y_train, f)
