import emoji
import regex
import csv 
from collections import Counter
import pandas as pd

def split_count(text):
    emoji_list = []
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
            emoji_list.append(word)
    
    return emoji_list



# Ouvrir le fichier csv
with open('user-tweets.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f)
    emoji_list= []
    df =pd.DataFrame(obj)
    text = df[2]
    emoji_list= [] 
    for t in text:
        emoji_list=emoji_list+split_count(t)
    print(Counter(emoji_list))



"""


import emoji
import regex
import csv 
from collections import Counter
import pandas as pd
import numpy as np
def split_count(text):

    emoji_list = []
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
            emoji_list.append(word)
    
    return emoji_list


# Ouvrir le fichier csv
with open('user-tweets.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f)
    emoji_list= []
    for ligne in obj:
        #print(ligne[2])
        counter = split_count(ligne[2])
        #print(' '.join(emoji for emoji in counter))
        #print(Counter(counter)) Pour compter le nombre d'occurence de chaque emojis
        #print(pd.Series(emoji).value_counts())
        count = Counter(emoji for emoji in counter) # Pass the list to instantiate the Counter object
        #print(count)
        #print(sum(count.values()))
        #print(pd.value_counts(np.array(count)))
        for t in ligne:
            emoji_list=emoji_list+split_count(t)
        print(Counter(emoji_list))    
"""