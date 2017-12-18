import math
import sys
import MeCab

class NaiveBayes():
    def __init__(self):
        self.vocabularies = set()
        self.word_count = {}  # {'花粉症対策': {'スギ花粉': 4, '薬': 2,...} }
        self.category_count = {}  # {'花粉症対策': 16, ...}
    def to_words(self, sentence):
        # 学習文書を形態素解析(Taggerに「mecabrc」使用)
        tagger = MeCab.Tagger('mecabrc')
        mecab_result = tagger.parse(sentence)
        info_of_words = mecab_result.split('\n')
        words = []

        for info in info_of_words:
            # macabで分けると、文の最後に’’が、その手前に'EOS'が来る
            if info == 'EOS' or info == '':
                break
                # info => 'な\t助詞,終助詞,*,*,*,*,な,ナ,ナ'
            info_elems = info.split(',')
            # 6番目に、無活用系の単語が入る。もし6番目が'*'だったら0番目を入れる
            if info_elems[6] == '*':
                # info_elems[0] => 'ヴァンロッサム\t名詞'
                words.append(info_elems[0][:-3])
                continue
            words.append(info_elems[6])
        return tuple(words)

    def word_count_up(self, word, category):
        self.word_count.setdefault(category, {})
        self.word_count[category].setdefault(word, 0)
        self.word_count[category][word] += 1
        self.vocabularies.add(word)

    def category_count_up(self, category):
        self.category_count.setdefault(category, 0)
        self.category_count[category] += 1

    def train(self, doc, category):
        #形態素解析
        words = self.to_words(doc)
        for word in words:
            #カテゴリー内の単語の数え上げ
            self.word_count_up(word, category)
        #カテゴリーの文章を数え上げ
        self.category_count_up(category)

    def prior_prob(self, category):
        num_of_categories = sum(self.category_count.values())
        num_of_docs_of_the_category = self.category_count[category]
        return float(num_of_docs_of_the_category / num_of_categories)

    def num_of_appearance(self, word, category):
        if word in self.word_count[category]:
            return self.word_count[category][word]
        return 0

    def word_prob(self, word, category):
        # ベイズの法則の計算。通常、非常に0に近い小数になる。
        numerator = self.num_of_appearance(word, category) + 1  # +1は加算スムージングのラプラス法
        denominator = sum(self.word_count[category].values()) + len(self.vocabularies)

        # Python3では、割り算は自動的にfloatになる
        prob = numerator / denominator
        return prob

    def score(self, words, category):
        # logを取るのは、word_probが0.000....01くらいの小数になったりするため
        score = math.log(self.prior_prob(category))
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

    # logを取らないと値が小さすぎてunderflowするかも。
    def score_without_log(self, words, category):
        score = self.prior_prob(category)
        for word in words:
            score *= self.word_prob(word, category)
        return score

    def classify(self, doc):
        best_guessed_category = None
        max_prob_before = -sys.maxsize
        words = self.to_words(doc)

        for category in self.category_count.keys():
            prob = self.score(words, category)
            if prob > max_prob_before:
                max_prob_before = prob
                best_guessed_category = category
        return best_guessed_category
