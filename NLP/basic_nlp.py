import nltk
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
s1 = "Earth is the third planet from the sun"
s2 = "Jupiter is the largest planet"

nltk.download('stopwords')
nltk.download('punkt_tab')
#Tokenizaion
tokens1 = nltk.word_tokenize(s1.lower())
tokens2 = nltk.word_tokenize(s2.lower())
print(tokens1,tokens2)
#Removing stopwords
stopwords = set(stopwords.words('english'))
filter1 = [i for i in tokens1 if i not in stopwords]
filter2 = [i for i in tokens2 if i not in stopwords]

from sklearn.feature_extraction.text import TfidfVectorizer
print(f"{filter1} and {filter2}")#text after the stopwordv 

s1_new = " ".join(filter1)
s2_new = " ".join(filter2)

vector  = TfidfVectorizer()
tf = vector.fit_transform([s1_new,s2_new])
print(tf.toarray())

similarity = cosine_similarity(tf[0:1],tf[1:2][0][0])
print(similarity)
#if the similarity is above 0.6 is good if it is less than 0.3 or something it is not good