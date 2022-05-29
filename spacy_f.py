from  mytools  import Analyze
import spacy
import nltk
from nltk.corpus import stopwords 

str = "Take Me To Bathroom"
stop_words = set(stopwords.words("english"))


tokens = nltk.word_tokenize(str)


print(tokens)




filtered_list = []

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
# print(doc)

# for word in stop_words :
