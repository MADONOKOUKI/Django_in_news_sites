# Naive Bayes classifier

Welcome to my Naive Bayes classifier! In this directory, you'll find the files you need to be able to study regarding classification task, especially naive bayes classification with Django .
Put your Python3 code. To experiment with that code, input url of gunosy news.

TODO: Delete this and the text above, and describe your gem

## Installation

Add this line to your application:

```Python3
sudo pip install virtualenv
```

And execute:

    $　source activate virtualenv


And then execute:

    $　pip install -r requirements.txt

## Usage
This tree's data size is dynamic variable.
If you want to use this library to programming contests, you can copy and paste from lib/union_find_tree.rb

example1
```Python3
python3 manage.py runserver
```

and access [Test site](http://127.0.0.1:8000/app/get/)

you can input URL and check category

example2
```Python3
python3 manage.py make_naive_Bayes_model
```

you can create naive Bayes model which is vital for checking category on the website

example3
```Python3
python3 manage.py eval_model
```

on your terminal, you can check accuracy rate (highest rate : 0.9351626368)
The accuracy rate was checked by cross validation methods.See this link[cross validation](https://qiita.com/kenmatsu4/items/0a862a42ceb178ba7155)

example4
```Python3
python3 manage.py scrapy_gunosy_learning_data
```

You can scrapy news data (Time : about 1h30min)

## Development

Please clone and setup using above commands.



## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/MADONOKOUKI/guno_project. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

