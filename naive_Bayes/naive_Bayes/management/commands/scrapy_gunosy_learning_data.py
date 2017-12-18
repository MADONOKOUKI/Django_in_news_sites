# vim*:fileencoding=utf8
from django.core.management.base import BaseCommand
mport pickle
import requests
from bs4 import BeautifulSoup
import time
import math
import sys
import MeCab

x_train = []
y_train = []

class Command(BaseCommand):
  def handle(self, *args, **options):
    print('start scrapying gunosy news')
    for i in range(1,8):
      target_url = "https://gunosy.com/categories/"
      target_url += str(i)
      for j in range(1,6):
        check_url = target_url +"?page=" + str(j)
        r = requests.get(check_url)         #requestsを使って、webから取得
        time.sleep(1)
        soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
      for div in soup.find_all("div",class_="article_list gtm-click"):
        for _div in div.find_all("div",class_="list_title"):
          for a in _div.find_all("a"):
            url = a.get('href')
            r = requests.get(url)
            time.sleep(1)
            print(url)
            soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
            for div in soup.find_all("div",class_="article gtm-click"):
              for p in div.find_all("p"):
                x_train.append(p.text)
                y_train.append(i)
    # save scrapied data as pkl file
    with open('x_train_2.pkl','wb') as f:
      pickle.dump(x_train,f)
    with open('y_train_2.pkl','wb') as f:
      pickle.dump(y_train,f)



