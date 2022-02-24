import emoji
import regex
import csv 
from collections import Counter
import pandas as pd
import json
def split_count(text):
    emoji_list = []
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
            emoji_list.append(word)
    
    return emoji_list



# Ouvrir le fichier csv
with open('Cristiano-tweets.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f)
    emoji_list= []
    df =pd.DataFrame(obj)
    text = df[1]
    emoji_list= [] 
    for t in text:
        emoji_list=emoji_list+split_count(t)
    f = open("{}.json".format("listeEmojisCristiano"),"w")
    j = json.dumps(Counter(emoji_list))
    f.write(j)
    f.close
    print(Counter(emoji_list))


