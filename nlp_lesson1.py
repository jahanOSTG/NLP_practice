import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

text= "I am Janie"
sentencrs=nltk.sent_tokenize(text)
words=nltk.word_tokenize(text)

print("Sentence :",sentencrs)
print("Word",words)