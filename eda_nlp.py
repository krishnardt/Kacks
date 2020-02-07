import time
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
stopwords = set(stopwords.words('english'))


def remove_nans(data, column):
    data= data[data[column].notnull() == True]
    #data = data[data[column].notnull()]
    #data = data.dropna(subset=[column], how='all', inplace=True)#, inplace=True)
    return data

def add_len_column(data, source, new_column):
    data[new_column] = data[source].str.len()
    #data[new_column] = data[source].apply(lambda x:len(x))
    return data

def get_nulls_columns(data):
    columns = data.columns[data.isnull().any()]
    return list(columns)

def remove_stop_words(string):
    return [word for word in string if word not in stopwords]


def clean_data(data):
    data['Review Text'] = data['Review Text'].apply(lambda x: x.lower())
    #data['Review Text'] = data['Review Text'].apply(lambda x: x.lower())
    #data['tokens'] = data['Review Text'].apply(lambda x : x.split(' '))#word_tokenize(x))
    #data['tokens'] = data['tokens'].apply(lambda x :remove_stop_words(x))
    data['Review Text'] = data['Review Text'].apply(lambda x : ' '.join(remove_stop_words(x.split(' '))))
    #del data['tokens']
    return data





path = ''
data = pd.read_csv('women_clothing_reviews.csv', encoding='utf-8')
print(data.head(10))
print(data.columns)
print(data.shape)

del data['Unnamed: 0']
del data['Division Name']
del data['Department Name']
del data['Recommended IND']
data = remove_nans(data, 'Class Name')
data = remove_nans(data, 'Title')
data = remove_nans(data, 'Positive Feedback Count')
data = remove_nans(data, 'Review Text')




#print(len(data['Clothing ID'].unique()))


cloth_ids = data['Clothing ID'].sort_values().unique()
print(cloth_ids)


columns = get_nulls_columns(data)
print(columns)
print(data.shape)
print(data.columns)
start = time.time()
data = clean_data(data)
end = time.time()


print(data['Review Text'].head(10))
print(end-start)
#toeknize the string in all records


#print(data['tokens'])

#removing stopwords from the text
