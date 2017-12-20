

def train_and_evaluate_model(nb,x_train,y_train,train,test):
      cnt = 0
      for i in train:
        nb.train(x_train[i],y_train[i])
      for i in train:
        nb.train(x_train[i],y_train[i])
      for i in train:
        nb.train(x_train[i],y_train[i])
      for i in test:
        if(nb.classify(x_train[i]) == y_train[i]):
          cnt+=1;
      return cnt / len(test)
