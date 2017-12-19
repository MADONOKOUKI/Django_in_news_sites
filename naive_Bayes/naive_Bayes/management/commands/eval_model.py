# -*- coding:utf-8 -*-


from django.core.management.base import BaseCommand
import numpy as np
from ...management.model.naive_bayes import NaiveBayes
from ...management.utils.evaluate import train_and_evaluate_model
from sklearn.cross_validation import KFold
from sklearn.cross_validation import StratifiedKFold
import pickle
# BaseCommandを継承して作成


class Command(BaseCommand):

    # python manage.py help make_naive_Bayes_model で表示されるメッセージ
    help = 'Make NaiveBayes model by '

    # コマンドが実行された際に呼ばれるメソッド
    x_train = []
    y_train = []

    def train_and_evaluate_model(train,test):
      nb = NaiveBayes()
      cnt = 0
      for i in train:
        nb.train(x_train[i],y_train[i])
      for i in test:
        if(nb.classify(x_train[i]) == y_train[i]):
          cnt+=1;
          # print(nb.classify(x_train[i]))
          # print(y_train[i])

      return cnt / len(test)

    def handle(self, *args, **options):
        with open('x_train_2.pkl', 'rb') as f:
          # print(f)
          x_train = pickle.load(f)
          # print(x_train)
        with open('y_train_2.pkl', 'rb') as f:
          # print(f)
          y_train = pickle.load(f)
          # print(y_train)

        pop = len(x_train)
        label = np.r_[np.repeat(0,pop-100), np.repeat(1,1)]
        skf = StratifiedKFold(label, n_folds=30, shuffle=True)
        total_score = 0
        rep = 0

        for i, (train, test) in enumerate(skf):
            # print("TRAIN:", train, "TEST:", test)
            total_score += train_and_evaluate_model(NaiveBayes(),x_train,y_train,train,test);
            rep+=1
        print("%.10f" % (total_score/rep))


