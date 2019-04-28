import pandas as pd
import numpy as np
import nltk
import re
#from sklearn import 
from nltk.stem import PorterStemmer
data = pd.read_csv("C://Users/hp/Documents/Prep2019ML/headlines_sarcasm_data.csv")
print(data.head(10))

data['headlines'] = data['headlines'].apply(lambda x : re.sub(r"'s", '', x))
data['headlines'] = data['headlines'].apply(lambda x : re.sub(r"[^0-9a-zA-Z ]", '', x))
print(data.head(10))



stopwords = nltk.corpus.stopwords.words('english')
stemmer = PorterStemmer()
def remove_sw(line):
    line = line.split(" ");
    #new_line = "";stemmer.stem(word)
    line = [word for word in line if word not in stopwords]
    return " ".join(line)

data['headlines'] = data['headlines'].apply(remove_sw)

print(data.head(10))



from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(ngram_range = (1,3), max_features = 300)
x = tfidf.fit_transform(data['headlines']).toarray()
print(x)




from sklearn.model_selection import train_test_split as tts
y = data['is_sarcastic']
x_train, x_test, y_train, y_test = tts(x, y, test_size=0.2, random_state = 42)



from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB();
gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)




from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))



from sklearn.svm import SVC
svc = SVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

