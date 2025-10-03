import nltk
nltk.download('punkt')      # for sentence tokenization
nltk.download('punkt_tab')

text= "I am Faria Jahan Janie.I don't love coding"
sentence=nltk.sent_tokenize(text)
words=nltk.word_tokenize(text)

print("Sentence Tokenization :",sentence)
print("Word Tokenization",words)