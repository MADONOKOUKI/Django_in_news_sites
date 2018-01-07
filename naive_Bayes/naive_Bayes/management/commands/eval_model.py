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
    """
      ・pickleデータのロード
      ・クロスバリデーションで精度測定
      ・精度を小数10桁まで出力
    """
    x_train = []
    y_train = []

    def handle(self, *args, **options):
        with open('article_text_data.pkl', 'rb') as f:
            x_train = pickle.load(f)
        with open('categories_data.pkl', 'rb') as f:
            y_train = pickle.load(f)

        pop = len(x_train)
        label = np.r_[np.repeat(0, pop - 100), np.repeat(1, 1)]
        skf = StratifiedKFold(label, n_folds=3, shuffle=True)
        total_score = 0
        rep = 0

        for i, (train, test) in enumerate(skf):
            total_score += train_and_evaluate_model(
                NaiveBayes(), x_train, y_train, train, test)
            rep += 1
        print("%.10f" % (total_score / rep))
