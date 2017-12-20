from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from datetime import datetime
import pickle
from bs4 import BeautifulSoup
import requests
import time
def hello_template(request):
    d = {
        'hour': datetime.now().hour,
        'message': 'Sample message',
    }
    return render(request, 'index.html', d)

def hello_world(request):
    return HttpResponse('Hello World!')

def hello_if(request):
    d = {
        'is_visible': False,
        'empty_str': '',
    }
    return render(request, 'if.html', d)

def hello_for(request):
    d = {
        'objects': range(10),
    }
    return render(request, 'for.html', d)

def hello_get_query(request):
    # d = {
    #     'your_name': request.GET.get('your_name')
    # }
    with open('naive_bayes_model.pkl', 'rb') as f:
          nb = pickle.load(f)
    url = request.GET.get('your_name')
    if(url):
        r = requests.get(url)         #requestsを使って、webから取得
        time.sleep(1)
        soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
        text = ""
        for div in soup.find_all("div",class_="article_list gtm-click"):
            for _div in div.find_all("div",class_="list_title"):
              for a in _div.find_all("a"):
                url = a.get('href')
                r = requests.get(url)
                time.sleep(1)
                soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
                for div in soup.find_all("div",class_="article gtm-click"):
                  for p in div.find_all("p"):
                    text += p.text
        show_text = nb.classify(text)
        d = {
            'your_name': show_text
        }
    else:
        d = {
            'your_name': url
        }
    return render(request, 'get_query.html',d)
