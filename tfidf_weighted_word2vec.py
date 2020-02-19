# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 3:03:23 2020

@author: hp
"""

import gensim
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from eda_nlp  import clean_data, remove_nans
import numpy as np

'''
IIn thIs code, I explained how the weights are generated and updated. And aso, how we use tfidf to improve scores.
Here I assumed model as unsupervised learning.
If we assume mode as supervised learning, It is slightly different case, but will be helpful.


Lets imagine I have every word regarding stcokmarket in my corpus.
I will create a vector of that corpus.

Let us take 10 examples of records
will filter out the unwanted tokens from the string.


1. will apply the tfidf for each record
2. will read the word2vec weights file.
3. will check the date of the last update,
4. if the date is yesterday's, will proceed with finding the embeddings or the given tweets
5. if date is not yesterday's, wil update/train the weights of the word2vec till yesterday.
6. The same way we do for tfidf word scores and save them. We already have the words and their scores based upon tfidf.
7. We already have the updated word2vec weights till yesterday.
8. for each word in a tweet, we will find its score with both weights in tidf and word2vec.
Here I used tfidf score of a word which was stored.We are not generating tidf score for the current tweets dataset as it is irrevelant.
9. Therefore now, we will get the score of the tweet. It may contain negative or positive value. It is
called polarity of the tweet lies between (-1 to 1).
10. we wil take the average  all the polarities of the tweets of a stock.
10. Using this sentiment of each tweet, will generate 10 scores for each stock.
11. We arenot depending on 1 vaue here, but depending on 10 values/decisions.(10 wise man instance).
11. if the stock is newly added we wil intialize them as zero.
12. else, will do consecutive sum of each of 10 values with yesterday's respective value and their average of resective value.
This is where we apply moving averages formula.
13. We will divide them into 3 group of pointers.[10, 20; 50; 80, 90]
14. 10, 50 ,90; 20, 50, 90; 10, 50, 80; 20, 50, 80. are 4 sets/combinations
15. we will get the score of each set by summing up and ohlc data of yesterday..
16. We will feed it into technical indicators.
17. I can't remember the remaining part how it will be feeded. But the stock price of a given stock high low open close
will be used to predict the fina scores of each set.
18. if sell comes >=3: stock will be sold
19. if buy comes >=3; stock will be bought
20. if buy/sell == 2; stock wil be on hold and the decision willbe of clients.
21. With the proper research on 90 days backtesting period, we can clearly fill the black spots. 


Explanation of moving averages in the test case.
22. lets take p1 among 10 values. we have p1(t-1). we want to have rdays value p1 value i.e., p1(t).
23. we will low weight to yesterday's vaue and high weight to today's value during summation.
24. we wil average it will get today's p1 value.
25. Similarly remaining 9 values happens and this is how we use moving aerages. to be precise weighted moving average.
'''






path = 'C://Users/hp/Videos/'
data = pd.read_csv(path+'women_clothing_reviews.csv')
data = remove_nans(data, 'Class Name')
data = remove_nans(data, 'Title')
data = remove_nans(data, 'Positive Feedback Count')
data = remove_nans(data, 'Review Text')

#data = data[['Review Text']]
data = data[data['Review Text'].notnull() == True]
data = clean_data(data)
#data = data['Review Text']
print(type(data))

tfidf = TfidfVectorizer(max_features = 800, use_idf=True, smooth_idf=True, sublinear_tf=True)
text = tfidf.fit_transform(data['Review Text'])
text = text.toarray().tolist()



model = gensim.models.Word2Vec(data['tokens'], size=800, window=5, workers=4)
model.save("w2v.model")

wvlist = list(model.wv.vocab)
dictionary = dict(zip(tfidf.get_feature_names(), list(tfidf.idf_)))
tfidf_feat = tfidf.get_feature_names()
tfidf_vectors = []
row=0
for sent in (data['tokens']):
    sent_vec = np.zeros(800)
    weight_sum = 0
    count = 0;
    for word in sent:
        if word in wvlist and word in tfidf_feat:
            vec = model.wv[word]
            print(vec)
            print(len(vec))
            tf_idf = dictionary[word]#*(sent.count(word)/len(sent))
            print(tf_idf)
            print(sent_vec)
            sent_vec += (vec*tf_idf)
            
            print(sent_vec)
            print(weight_sum)
            weight_sum += tf_idf
            print(weight_sum)
            if count == 2:
                break;
            else:
                count = count+1
    if weight_sum!=0:
        sent_vec/=weight_sum
    tfidf_vectors.append(sent_vec)
    row = row+1
    break;

#data = data.values
#print(type(data))


