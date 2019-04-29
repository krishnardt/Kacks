import json
import pandas as pd


def converter(file):
    df = []
    for line in file:
        df.append(json.loads(line))

    headlines = pd.DataFrame(df)
    return headlines;


PATH = "FILE_PATH";
FILE = "FILE_NAME"
file = open(PATH+FILE, encoding='utf-8', mode='r')
headlines = converter(file)

headlines = headlines[['headline', 'is_sarcastic']]
print(headlines)
