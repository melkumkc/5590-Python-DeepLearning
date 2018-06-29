
import nltk
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

myfile = open ("sms") # reading a file and storing it to input_txt
input_txt = myfile.read()
words = input_txt.split() # storing each word in the txt file as a list

#Lemmatization...................................................................

lemmatizer = WordNetLemmatizer ()
lemma =[] # List to store lemmatized words
for w in words:
    lemma.append(lemmatizer.lemmatize(w))
print ("Lemmatization.......")
print (lemma)

# Bigram............................................................................
bigrams=ngrams(words,2)
bi = [] # list to store tuples of three elements
for i in bigrams:
    bi.append (i)
print ("bigram.......")
print (bi)
dic = {} # creating a dictonary to find the frequency of bigram
for t in bi:
    if t in dic:
        dic[t] +=1
    else:
        dic[t] = 1


lis2 =[] # list to store tuple of the dictionary (dic) value and key
for k,v in dic.items():
    lis2.append ((v,k))

lis2.sort() # sorting the list in increasing order
top5_bigrams = lis2[-1:-6:-1] # to find the top five repeated bigrams

sentences = sent_tokenize(input_txt)# sentence tokenizing

fin_sent = " " # string variable to store the sentences with top5_bigrams
fin_lis = []
""" to find the sentences from the original file and to concatnate them"""
for i in sentences:
    for j in top5_bigrams:
        if j[1][0] in i and j[1][1] in i:
            fin_sent += i
            fin_sent += " "

print (fin_sent)

