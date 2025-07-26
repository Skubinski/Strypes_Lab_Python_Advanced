from nltk import bigrams
from nltk.tokenize import word_tokenize

with open('test.txt') as file, open('words.txt', 'a') as word, open('sent.txt', 'a') as sent:
    words = []
    text = file.read()
    for w in text.split():
        word.write(w+'\n')

    for s in text.strip().split('.'):
        sent.write(s+'\n')

