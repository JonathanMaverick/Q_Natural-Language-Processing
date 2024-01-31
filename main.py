# Tokenizing
# Membagi text kedalam sebuah token (word, symbol)
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('punkt')

sentence = "Hello, can you play at 07 PM? I'm busy at 08 PM. How about 09 PM?"

list_word = word_tokenize(sentence)
list_sentence = sent_tokenize(sentence)
print(list_word)
print(list_sentence)

# Stop Words
# Menghilangkan kata yang tidak penting
