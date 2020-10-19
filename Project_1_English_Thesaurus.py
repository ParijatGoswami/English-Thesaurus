import json
from difflib import get_close_matches


data = json.load(open("Python/1.1.1 Python Basics/Basic Projects/Project 1 English Thesaurus/data.json"))



def get_meaning(w):
    w = w.lower()
    if w in data:
        return data[w]  
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        corr_w = get_close_matches(w, data.keys())[0]
        yn = input("Did you mean %s instead? ENter Y if yes or N if no: " %corr_w)
        if yn == "Y":
            return data[corr_w]
        elif yn == "N":
            return "This word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "This word doesn't exist. Please double check it"


input_word = input("Enter Word to get the meaning: ")
x = get_meaning(input_word)

if isinstance(x,list):
    for i in x:
        print(i)
else:
    print(x)