import json
from difflib import get_close_matches

data = json.load(open("data.json",'r'))

def lookup(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]    
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes, N for no: " %get_close_matches(w, data.keys())[0]).upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Sorry, we don't hold %s in our dictionary. Please double check the word." %w
        else:
            return "Invalid input"
    else:
        return "Please double check the spelling and word. We don't hold %s in our dictionary" %w

word = input("Enter a word: ")
output = lookup(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
