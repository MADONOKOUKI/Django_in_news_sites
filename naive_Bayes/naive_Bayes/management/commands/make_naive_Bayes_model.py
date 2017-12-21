# -*- coding:utf-8 -*-

from django.core.management.base import BaseCommand
from ..model import naive_bayes
from ...management.model.naive_bayes import NaiveBayes
import pickle

class Command(BaseCommand):
    # python manage.py help make_naive_Bayes_model で表示されるメッセージ
    help = 'Make NaiveBayes model'
    """
        ・ナイーブベイズモデルインスタンス生成
        ・記事データのロード
        ・訓練（同じデータで3度）
        ・モデルを保存
    """
    def handle(self, *args, **options):
        nb = NaiveBayes()
        with open('x_train_4.pkl', 'rb') as f:
          x_train = pickle.load(f)
        with open('y_train_4.pkl', 'rb') as f:
          y_train = pickle.load(f)
        for i in range(0,len(x_train)):
          nb.train(x_train[i],y_train[i])
        for i in range(0,len(x_train)):
          nb.train(x_train[i],y_train[i])
        for i in range(0,len(x_train)):
          nb.train(x_train[i],y_train[i])
        with open('naive_bayes_model.pkl','wb') as f:
          pickle.dump(nb,f)

