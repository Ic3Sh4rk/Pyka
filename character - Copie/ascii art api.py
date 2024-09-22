import urllib.request
import json
import os

with open("E:\\pyka\\character\\available character.json", encoding='UTF8') as data:
    data = json.load(data)

available_character = list()


# sélectionez une police de caractère parmis la liste sur https://artii.herokuapp.com/fonts_list sauf pyramid et maxfour
font = "nancyj-underlined"


# minuscules

print("lowercase : in progress...")
for i in range(len(data['lowercase'])):
    f = urllib.request.urlopen(f"https://artii.herokuapp.com/make?text={data['lowercase'][i]}&font={font}")
    while True:
        try:
            with open(f"E:\\pyka\\character\\{font}\\letter\\lowercase\\{str(data['lowercase'][i])}.txt", mode='w',
                      encoding='UTF8') as testfile:
                testfile.write(f.read().decode())
                break
        except FileNotFoundError:
            os.makedirs(f"E:\\pyka\\character\\{font}\\letter\\lowercase\\")
print("lowercase : check\nupper case : in progress...")

# majuscules

for i in range(len(data['upper case'])):
    f = urllib.request.urlopen(f"https://artii.herokuapp.com/make?text={data['upper case'][i]}&font={font}")
    while True:
        try:
            with open(f"E:\\pyka\\character\\{font}\\letter\\upper case\\{str(data['upper case'][i])}.txt", mode='w',
                      encoding='UTF8') as testfile:
                testfile.write(f.read().decode())
                break
        except FileNotFoundError:
            os.makedirs(f"E:\\pyka\\character\\{font}\\letter\\upper case\\")
print("upepr case : check\nnumber : in progress...")

# nombres

for i in range(len(data['number'])):
    f = urllib.request.urlopen(f"https://artii.herokuapp.com/make?text={data['number'][i]}&font={font}")
    while True:
        try:
            with open(f"E:\\pyka\\character\\{font}\\letter\\number\\{str(data['number'][i])}.txt", mode='w',
                      encoding='UTF8') as testfile:
                testfile.write(f.read().decode())
                break
        except FileNotFoundError:
            os.makedirs(f"E:\\pyka\\character\\{font}\\letter\\number\\")
print("number : check\npunctuation : in progress...")

# ponctuation

for i in range(len(data['punctuation'])):
    f = urllib.request.urlopen(f"https://artii.herokuapp.com/make?text={data['punctuation'][i]}&font={font}")
    while True:
        try:
            with open(f"E:\\pyka\\character\\{font}\\letter\\punctuation\\ponctuation n{str([i])}.txt", mode='w',
                      encoding='UTF8') as testfile:
                testfile.write(f.read().decode())
                break
        except FileNotFoundError:
            os.makedirs(f"E:\\pyka\\character\\{font}\\letter\\punctuation\\")
print("punctuation : check\nsymbol : in progress...")

# symboles

for i in range(len(data['symbol'])):
    f = urllib.request.urlopen(f"https://artii.herokuapp.com/make?text={data['symbol'][i]}&font={font}")
    while True:
        try:
            with open(f"E:\\pyka\\character\\{font}\\letter\\symbol\\symbole n{str([i])}.txt", mode='w',
                      encoding='UTF8') as testfile:
                testfile.write(f.read().decode())
                break
        except FileNotFoundError:
            os.makedirs(f"E:\\pyka\\character\\{font}\\letter\\symbol\\")
print("upper case : check")
