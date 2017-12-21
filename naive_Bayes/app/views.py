from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from datetime import datetime
import pickle
from bs4 import BeautifulSoup
import requests
import time

def get_category(request):
    with open('naive_bayes_model.pkl', 'rb') as f:
          nb = pickle.load(f)
    url = request.GET.get('result')
    if(url):
        r = requests.get(url)         #requestsを使って、webから取得
        soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
        text = ""
        for div in soup.find_all("div",class_="article gtm-click"):
          for p in div.find_all("p"):
            text += p.text
        show_text = nb.classify(text)
        d = {
            'result': show_text
        }
    else:
        d = {
            'result': "ここに入力したGunosyの記事のカテゴリが表示されます"
        }
    return render(request, 'get_query.html',d)
