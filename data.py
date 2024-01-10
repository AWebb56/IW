import json
from langdetect import detect
import re
import os
import gzip
jptweets = []
entweets = []
enltweets  = []
jpltweets = []
for i in range(24):
    for j in range(60):
        filestr = "./20221101/20221101{:02d}{:02d}00.json.gz".format(i,j)
        with gzip.open(filestr, "r") as file:
            for line in file:
                test = json.loads(line)
                text = test['text']
                text = re.sub(r'^RT @[a-zA-Z0-9_]*: ', "", text)
                text = re.sub(r'^@[a-zA-Z0-9_]* ', '', text)
                test['text'] = text
                try:
                    lan = detect(text)
                except Exception as ex:
                    continue   
                if lan == 'ja':
                        jptweets.append([test['text'],test["id_str"]])                          
                        if re.search(r"[😂🤣💀😭]", text)  or re.search(r"[一-龠ぁ-ゔァ-ヴー々〆〤_]w+(?:[一-龠ぁ-ゔァ-ヴー々〆〤_]|(?:\s|$))", text) or "草" in text or "笑" in text:
                            jpltweets.append([test['text'],test["id_str"]])  
                if lan == 'en':
                        entweets.append([test['text'],test["id_str"]])  
                        if re.search(r"[😂🤣💀😭]", text)  or "lol" in text or "lmao" in text:
                            enltweets.append([test['text'],test["id_str"]])  
        file.close()
        print("Finished: " + "./20221101/20221101{:02d}{:02d}00.json.gz".format(i,j) + "\n")
        print("Number of jp tweets: " + str(len(jptweets)) + " \n")
        print("Number of en tweets: " + str(len(entweets)) + " \n")
for i in range(24):
    for j in range(60):
        filestr = "./20220130/20220130{:02d}{:02d}00.json.gz".format(i,j)
        try:
            with gzip.open(filestr, "r") as file:
                for line in file:
                    test = json.loads(line)
                    text = test['text']
                    text = re.sub(r'^RT @[a-zA-Z0-9_]*: ', "", text)
                    text = re.sub(r'^@[a-zA-Z0-9_]* ', '', text)
                    test['text'] = text
                    try:
                        lan = detect(text)
                    except Exception as ex:
                        continue   
                    if lan == 'ja':
                            jptweets.append([test['text'],test["id_str"]])                          
                            if re.search(r"[😂🤣💀😭]", text)  or re.search(r"[一-龠ぁ-ゔァ-ヴー々〆〤_]w+(?:[一-龠ぁ-ゔァ-ヴー々〆〤_]|(?:\s|$))", text) or "草" in text or "笑" in text:
                                jpltweets.append([test['text'],test["id_str"]])  
                    if lan == 'en':
                            entweets.append([test['text'],test["id_str"]])  
                            if re.search(r"[😂🤣💀😭]", text)  or "lol" in text or "lmao" in text:
                                enltweets.append([test['text'],test["id_str"]]) 
        except Exception as ex:
                        continue 
        file.close()
        print("Finished: " + "./20220130/20220130{:02d}{:02d}00.json.gz".format(i,j) + "\n")
        print("Number of jp tweets: " + str(len(jptweets)) + " \n")
        print("Number of en tweets: " + str(len(entweets)) + " \n")
for i in range(24):
    for j in range(60):
        filestr = "./20220415/20220415{:02d}{:02d}00.json.gz".format(i,j)
        try:
            with gzip.open(filestr, "r") as file:
                for line in file:
                    test = json.loads(line)
                    text = test['text']
                    text = re.sub(r'^RT @[a-zA-Z0-9_]*: ', "", text)
                    text = re.sub(r'^@[a-zA-Z0-9_]* ', '', text)
                    test['text'] = text
                    try:
                        lan = detect(text)
                    except Exception as ex:
                        continue   
                    if lan == 'ja':
                            jptweets.append([test['text'],test["id_str"]])                          
                            if re.search(r"[😂🤣💀😭]", text)  or re.search(r"[一-龠ぁ-ゔァ-ヴー々〆〤_]w+(?:[一-龠ぁ-ゔァ-ヴー々〆〤_]|(?:\s|$))", text) or "草" in text or "笑" in text:
                                jpltweets.append([test['text'],test["id_str"]])  
                    if lan == 'en':
                            entweets.append([test['text'],test["id_str"]])  
                            if re.search(r"[😂🤣💀😭]", text)  or "lol" in text or "lmao" in text:
                                enltweets.append([test['text'],test["id_str"]]) 
        except Exception as ex:
                        continue   
        file.close()
        print("Finished: " + "./20220415/20220415{:02d}{:02d}00.json.gz".format(i,j) + "\n")
        print("Number of jp tweets: " + str(len(jptweets)) + " \n")
        print("Number of en tweets: " + str(len(entweets)) + " \n")
for i in range(24):
    for j in range(60):
        filestr = "./20220621/20220621{:02d}{:02d}00.json.gz".format(i,j)
        try:
            with gzip.open(filestr, "r") as file:
                for line in file:
                    test = json.loads(line)
                    text = test['text']
                    text = re.sub(r'^RT @[a-zA-Z0-9_]*: ', "", text)
                    text = re.sub(r'^@[a-zA-Z0-9_]* ', '', text)
                    test['text'] = text
                    try:
                        lan = detect(text)
                    except Exception as ex:
                        continue   
                    if lan == 'ja':
                            jptweets.append([test['text'],test["id_str"]])                          
                            if re.search(r"[😂🤣💀😭]", text)  or re.search(r"[一-龠ぁ-ゔァ-ヴー々〆〤_]w+(?:[一-龠ぁ-ゔァ-ヴー々〆〤_]|(?:\s|$))", text) or "草" in text or "笑" in text:
                                jpltweets.append([test['text'],test["id_str"]])  
                    if lan == 'en':
                            entweets.append([test['text'],test["id_str"]])  
                            if re.search(r"[😂🤣💀😭]", text)  or "lol" in text or "lmao" in text:
                                enltweets.append([test['text'],test["id_str"]])  
            file.close()
        except Exception as ex:
                        continue 
        print("Finished: " + "./20220621/20220621{:02d}{:02d}00.json.gz".format(i,j) + "\n")
        print("Number of jp tweets: " + str(len(jptweets)) + " \n")
        print("Number of en tweets: " + str(len(entweets)) + " \n")        
with open("jptweets4.csv", "w", encoding='utf-8') as file:
    for x in jptweets:
        pt = x[0].replace("\n", " ")
        pt = re.sub(r'https://t.co/[a-zA-Z_0-9]*', "", pt)
        pt = re.sub(r'[♯#＃][一-龠ぁ-ゔァ-ヴーa-zA-Z0-9ａ-ｚＡ-Ｚ０-９々〆〤_]*', "", pt)
        pt = re.sub(r'[】【]', "", pt)
        pt = re.sub(r'@[a-zA-Z0-9_]*', '', pt)
        file.write( pt + "," + x[1] +"\n")
with open("entweets4.csv", "w", encoding='utf-8') as file:
    for x in entweets:
        pt = x[0].replace("\n", " ")
        pt = re.sub(r'https://t.co/[a-zA-Z_0-9]*', "", pt)
        pt = re.sub(r'[♯#＃][一-龠ぁ-ゔァ-ヴーa-zA-Z0-9ａ-ｚＡ-Ｚ０-９々〆〤_]*', "", pt)
        pt = re.sub(r'[】【]', "", pt)
        pt = re.sub(r'@[a-zA-Z0-9_]*', '', pt)
        file.write( pt + "," + x[1] +"\n")
with open("jpltweets4.csv", "w", encoding='utf-8') as file:
    for x in jpltweets:
        pt = x[0].replace("\n", " ")
        pt = re.sub(r'https://t.co/[a-zA-Z_0-9]*', "", pt)
        pt = re.sub(r'[♯#＃][一-龠ぁ-ゔァ-ヴーa-zA-Z0-9ａ-ｚＡ-Ｚ０-９々〆〤_]*', "", pt)
        pt = re.sub(r'[】【]', "", pt)
        pt = re.sub(r'@[a-zA-Z0-9_]*', '', pt)
        file.write( pt + "," + x[1] +"\n")
with open("enltweets4.csv", "w", encoding='utf-8') as file:
    for x in enltweets:
        pt = x[0].replace("\n", " ")
        pt = re.sub(r'https://t.co/[a-zA-Z_0-9]*', "", pt)
        pt = re.sub(r'[♯#＃][一-龠ぁ-ゔァ-ヴーa-zA-Z0-9ａ-ｚＡ-Ｚ０-９々〆〤_]*', "", pt)
        pt = re.sub(r'[】【]', "", pt)
        pt = re.sub(r'@[a-zA-Z0-9_]*', '', pt)
        file.write( pt + "," + x[1] +"\n")
