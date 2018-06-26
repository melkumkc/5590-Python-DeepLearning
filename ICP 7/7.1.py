from bs4 import BeautifulSoup
import urllib.request
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk import ne_chunk
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

# Extracting using Beautiful soup ...................................................

html = ("https://en.wikipedia.org/wiki/Python_(programming_language)") # web scraping
input = urllib.request.urlopen(html)
soup = BeautifulSoup(input,'html.parser')
input_text = soup.get_text() # saving the text in the url into a variable



#Tokenization.........................................................

words = word_tokenize(input_text) # word tokenizing
sentences = sent_tokenize(input_text)# sentence tokenizing
filterd_words = [] # to find unique words and sentences
filterd_sentences = []

for w in words:
    if w not in filterd_words:
        filterd_words.append(w)
for s in sentences:
    if s not in filterd_sentences:
        filterd_sentences.append(s)
print ("Tokenization...............")
print (filterd_sentences)
print (filterd_words)

#Stemming ....................................................................

ps = PorterStemmer() # creating object for stemming
stemen = [] # list for storing stemmed words
for w in filterd_words:
    stemen.append(ps.stem(w))
print ("stemming............")
print (stemen)

# POS...........................................................................

pos = nltk.pos_tag(words) # part of speech tagging
print ("POS..........")
print (pos)

#Lemmatization...................................................................

lemmatizer = WordNetLemmatizer ()
lemma =[] # List to store lemmatized words
for w in words:
    lemma.append(lemmatizer.lemmatize(w))
print ("Lemmatization.......")
print (lemma)

# Trigram............................................................................

trigrams=ngrams(words,3)
tri = [] # list to store tuples of three elements
for i in trigrams:
    tri.append (i)
print ("Trigram.......")
print (tri)

# named entity recognision..........................................................

namEnt = nltk.ne_chunk(pos)
print ("Named entity recognition........")
print (namEnt)

