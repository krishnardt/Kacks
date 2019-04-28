import json
import sys
import pandas as pd

file = open("C://Users/hp/Documents/Prep2019ML/news-headlines-dataset-for-sarcasm-detection/Sarcasm_Headlines_Dataset.json", encoding='utf-8', mode='r')
# for line in file:
# 	print(line)
# 	line[10]
# 	sys.exit(0);
# data = json.loads(file.read())
# print(data)\


data = []
for line in file:
	data.append(json.loads(line))

#print(data)
#print(reviews)
headlines = []
sarcastic = []
for i in data:
	#print(i['headline'])
	headlines.append(i['headline'])
	sarcastic.append(i['is_sarcastic'])
	#sys.exit(0)
#print(headlines)
#print(sarcastic)
#data = {'headlines':headlines, 'sarcastic':sarcastic}
#print(data)
data = pd.DataFrame(headlines, columns = ['headlines'])
data['is_sarcastic'] = sarcastic
print(data)

data.to_csv("C://Users/hp/Documents/Prep2019ML/headlines_sarcasm_data.csv", index = False)
