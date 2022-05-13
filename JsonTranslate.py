import json
import googletrans
from googletrans import Translator

# Use translator class from Googletrans python library - will handle the translation
translator = Translator()

# Open the necessary file using absolute path notation and force encoding UTF8
with open("X:\\English.json", encoding='utf8') as jsonFile:
    # Load JSON file to a dictionary
    # Check file before translation
    jsonData = json.load(jsonFile)
    print("BEFORE TRANSLATION:------------------")
    print("-------------------------------------")
    # JSON prettify
    print(json.dumps(jsonData, indent=4))
    print("-------------------------------------")

    # Iterate all items of dictionary and translate ONLY the values of the nested dictionaries.
    # Used here: source lang english / destination lang greek
    # To retrieve the valid notation for the respective languages, please uncomment and execute
    # the following part of code:
    # ---------------------------------------
    # langList = googletrans.LANGUAGES
    # print(json.dumps(langList, indent=4))
    # ---------------------------------------
    for level1, level2 in jsonData.items():
        for key in level2:
            greek = translator.translate(level2[key], src='en', dest='el')
            level2[key] = greek.text

    greektxt = json.dumps(jsonData, ensure_ascii=False)
    greektxt = greektxt.replace("\\","")
    greektxt = greektxt.replace("\'","\"")
    greektxt = greektxt.replace("\"{","{")
    greektxt = greektxt.replace("}\"","}")

    print("AFTER TRANSLATION:-------------------")
    print("-------------------------------------")
    print(greektxt)
    print("-------------------------------------")
