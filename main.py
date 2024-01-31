# Tokenizing
# Membagi text kedalam sebuah token (word, symbol)
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('')

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
print(removed_punctuation_list)
