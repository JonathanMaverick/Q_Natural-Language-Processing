# Tokenizing
# Membagi text kedalam sebuah token (word, symbol)
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
# nltk.download('wordnet')

sentence = "Hello, can you play at 07 PM? I'm busy at 08 PM. How about 09 PM?"

list_word = word_tokenize(sentence)
list_sentence = sent_tokenize(sentence)
# print(list_word)
# print(list_sentence)

# Stop Words
# Menghilangkan kata yang tidak penting
from nltk.corpus import stopwords

eng_stopwords = stopwords.words('english')

# List Comprehension
removed_stopword_list = [word for word in list_word if word.lower() not in eng_stopwords] # .lower() untuk case insensitive
# print(removed_stopword_list)

# Kedua hal ini sama saja seperti yang ada di atas
# for word in list_word:
#     if word not in eng_stopwords:
#         removed_stopword_list.append(word)

import string
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
removed_punctuation_list = [word for word in removed_stopword_list if word not in string.punctuation]
# print(removed_punctuation_list)

# Stemming
# Menghilangkan imbuhan kata

from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer

porter_stemmer = PorterStemmer()
# Algoritmnya lambat, akurasi bagus (dalam bahasa inggris)
snowball_stemmer = SnowballStemmer('english')
# PorterStemmer V2 (dalam beberapa bahasa)
lancaster_stemmer = LancasterStemmer()
# Algoritmanya cepat, akurasi kurang bagus

words = ['program', 'programs', 'programer', 'programing', 'programers']
# for word in words:
#     print(f"{word}")
#     print(f"Stemmer : {porter_stemmer.stem(word)}")
#     print(f"Snowball : {snowball_stemmer.stem(word)}")
#     print(f"Lancaster : {lancaster_stemmer.stem(word)}")
#     print("=====================================")
    
# Lemmatizing
# Bisa menentukan konteks dari kata tersebut dan mengubah susuai konteks
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
word = "crying"

# a = adjective, r = adverb, n = noun, v = verb
adjective = wnl.lemmatize(word, pos='a') 
adverb = wnl.lemmatize(word, pos='r')
noun = wnl.lemmatize(word, pos='n')
verb = wnl.lemmatize(word, pos='v')

# print(adjective, adverb, noun, verb)

# Part of Speech Tagging (POS Tagging)
# Membagi kata kedalam kategori
from nltk.tag import pos_tag
# NNP = Proper Noun, NN = Noun, VB = Verb, RB = Adverb, JJ = Adjective
# CD = Cardinal Digit, IN = Preposition, MD = Modal, DT = Determiner
# pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/
tagged = pos_tag(removed_punctuation_list)
# print(tagged)

# Named Entity Recognition (NER)
from nltk.chunk import ne_chunk

ner = ne_chunk(tagged)
# ner.draw()

# Frequency Distribution
# Menghitung seberapa sering suatu kata pada dalam kalimat
from nltk.probability import FreqDist
sentence = "I order a bowl of chicken rice and a bowl of ramen, but I hate the chicken rice."
fd = FreqDist(word_tokenize(sentence))
# for word, count in fd.most_common(3):
#     print(f"{word} : {count}")
    
    
# Corpora -> Collection dari text atau audio data yang dibuat oleh native speaker dari bahasa tersebut

from nltk.corpus import gutenberg
# print(sent_tokenize(gutenberg.raw('austen-emma.txt')))

# Load corpora from web
from urllib import request
url = "https://www.gutenberg.org/files/63919/63919.txt"
corpus = request.urlopen(url).read().decode('utf-8')

# Wordnet
from nltk.corpus import wordnet
word = "good"
synsets = wordnet.synsets(word)
# Lemmas = kata dasar
# Synset = kumpulan dari lemmas
# n = noun, v = verb, a = adjective, r = adverb, s = adjective satellite

# for synset in synsets:
#     print(f"{synset} : {synset.definition()}")
#     for lemma in synset.lemmas():
#         print(f"Synonim - {lemma.name()}")
#         for antonym in lemma.antonyms():
#             print(f"Antonym - {antonym.name()}")
            
# Naive Bayes
# Supervised Learning -> Metode dalam machine learning yang menggunakan data yang sudah dilabeli (Classification, Regression)
# Unsupervised Learning -> Metode dalam machine learning yang menggunakan data yang belum dilabeli (Clustering, Association, Dimensionality Reduction)

# Naive Bayes 
with open("positive.txt", "r", encoding="latin-1") as positive_file:
    positive = positive_file.read()

with open("negative.txt", "r", encoding="latin-1") as negative_file:
    negative = negative_file.read()

list_words = word_tokenize(positive) + word_tokenize(negative)
list_words = [word for word in list_words if word.lower() not in eng_stopwords]
list_words = [word for word in list_words if word not in string.punctuation]
list_words = [word for word in list_words if word.isalpha()]

fd = FreqDist(list_words)
list_words = [word for word, count in fd.most_common(100)]
# print(list_words)

# Labelling sentence
labeled_sentence = []
for sentence in positive.split("\n"):
    labeled_sentence.append((sentence, "pos"))
for sentence in negative.split("\n"):
    labeled_sentence.append((sentence, "neg"))
    
dataset = []
for sent, label in labeled_sentence:
    dict = {"key":"value"}
    word = word_tokenize(sent)
    for feature in list_words:
        key = feature
        value = feature in words
        dict[key] = value
    dataset.append((dict, label))
    
import random
random.shuffle(dataset)
counter = int(len(dataset) * 0.7)
training_data = dataset[:counter]
testing_data = dataset[counter:]

from nltk.classify import NaiveBayesClassifier,accuracy
# classifier = NaiveBayesClassifier.train(training_data)
# accuracy = accuracy(classifier, testing_data)
# print(accuracy)

import pickle
# file = open("model.pickle", "wb")
# pickle.dump(classifier, file)
# file.close()

file = open("model.pickle", "rb")
classifier = pickle.load(file)
file.close()
# accuracy = accuracy(classifier, testing_data)
# print(accuracy)

review = input("Input Review : ")
words = word_tokenize(review)
result = classifier.classify(FreqDist(words))
print(result)