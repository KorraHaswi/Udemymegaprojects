import json
import codecs
from difflib import get_close_matches

data = json.load(codecs.open("data.json", "r", 'utf-8-sig'))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())[0])>0:
        yn = input("did you mean %s instead? enter Y  if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == 'Y':
            return get_close_matches(w, data.keys())[0]
        elif yn == 'N':
            return " we didn't understand your entry"
    else:
        return " the word does does not exist"
output = translate('bloww')
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)