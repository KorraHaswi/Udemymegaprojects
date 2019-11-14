import json
import codecs
from difflib import get_close_matches

data = json.load(codecs.open("data.json", "r", 'utf-8-sig'))

'''jog={'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Kansas City': 'Royals'}'''
def translate():

    while True:
        word=input("Enter the word: ")
        word=word.lower()
        if word.lower() in data.keys():
            return data[word]
        elif len(get_close_matches(word, data.keys()))>0:
            print("did you mean %s ?" %(get_close_matches(word, data.keys()))[0])
            yn=input()
            if yn == 'Y':
                return data[get_close_matches(word, data.keys())[0]]
            else:
                print('there is no such word in the dictionary')


        else:
            print("the word does not exist. please double check")



res = translate()
#if type(res) == list:
for item in res:
    print(item)

#print(get_close_matches('rain', data.keys())[0])