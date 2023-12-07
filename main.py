import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
#print(stopwords.words("english"))

userInput = input("Enter a sentence: ")

tokens = word_tokenize(userInput)

sentence = [word for word in tokens if not word in stopwords.words("english")]

print(tokens)
print(sentence)