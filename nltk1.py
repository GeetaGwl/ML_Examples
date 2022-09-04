from nltk import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
sen="hello i am from kanishka IT . intrested in Machine learning"
s=sent_tokenize(sen)
w=word_tokenize(sen)
print(s)
print(w[0])
stop_words = set(stopwords.words("english"))
for word in w:
    if word not in stop_words:
        print(word)
