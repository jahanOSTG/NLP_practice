import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('stopwords')      # for sentence tokenization
nltk.download('wordnet')

text= "I am learning NLP and I am loving it because it is very interesting!. Besides I have many hobbies.Like fishing,gardening,watching animation etc"

# word tokenization
words=nltk.word_tokenize(text)
print("Word Tokenization",words)
# output: Word Tokenization ['I', 'am', 'learning', 'NLP', 'and', 'I', 'am', 'loving', 'it', 'because', 'it', 'is', 'very', 'interesting', '!', '.', 'Besides', 'I', 'have', 'many', 'hobbies.Like', 'fishing', ',', 'gardening', ',', 'watching', 'animation', 'etc']

# stopwords remove
stop_words= set(stopwords.words('english'))
filtered_words=[w for w in words if w.lower() not in stop_words]
print("After Stopword Removal:" ,filtered_words)
# output: After Stopword Removal: ['learning', 'NLP', 'loving', 'interesting', '!', '.', 'Besides', 'many', 'hobbies.Like', 'fishing', ',', 'gardening', ',', 'watching', 'animation', 'etc']

# Stemming( cut word )
stemmer= PorterStemmer()
stemmed_words= [stemmer.stem(w) for w in filtered_words]
print("After Stemming:" ,stemmed_words)
# output: After Stemming: ['learn', 'nlp', 'love', 'interest', '!', '.', 'besid', 'mani', 'hobbies.lik', 'fish', ',', 'garden', ',', 'watch', 'anim', 'etc']

# Lemmatizing (Grammatical word)
lematizer= WordNetLemmatizer()
lematized_words=[lematizer.lemmatize(w) for w in filtered_words]
print("After Lemmatization: ",lematized_words)
#output: After Lemmatization:  ['learning', 'NLP', 'loving', 'interesting', '!', '.', 'Besides', 'many', 'hobbies.Like', 'fishing', ',', 'gardening', ',', 'watching', 'animation', 'etc']
