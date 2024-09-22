# Ce code a été créé par Ic3Sh4rk | This code was created by Ic3Sh4rk


"""
def memorysearch(type_search):
    type_search = type_search.upper()
    import os
    mode = "None"
    identity = [os.environ['COMPUTERNAME'], os.environ['USERNAME']]
    with open('..\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        for memory in memorylist:
            memory = memory.strip("\n")
            if memory.startswith("logfilenumber" + " > "):
                logfilenumber = int(memory[-1])
            elif memory.startswith("username" + " <"):
                mode = "Username"
            elif memory.startswith("\t"):
                if mode == "Username":
                    if memory[0:memory.find(">") - 1] == "\t{0},{1}".format(identity[0], identity[1]):
                        username = memory.replace(memory[0:memory.find(">") + 2], "")
                    elif memory[0:memory.find(">") - 1] == "\t{0},{1}".format(identity[0], identity[1]):
                        username = memory.replace(memory[0:memory.find(">") + 2], "")
                elif mode == "None":
                    print("ERROR 0101")
        if type_search == "USERNAME":
            return username
        elif type_search == "LOGFILENUMBER":
            return logfilenumber
        else:
            return "ERROR"


print(memorysearch("USERNAME"), memorysearch("LOGFILENUMBER"))
"""


"""
def listfind(search, list):
    if search in list:
        for i in range(len(a)):
            if search in a[i]:
                return i
    else:
        return None
"""
"""
def memorymodify(object, type, modify):


    def listfind(search, list):
        if search in list:
            for i in range((len(list))):
                if search in list[i]:
                    return i
        else:
            print("ERROR 1.1")
            return None


    def linefind(search, list):
        for i in range((len(list))):
            if list[i].startswith(search):
                return i


    object = object.strip("\n")
    object += "\n"
    with open('..\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        print(memorylist)
        listfound = listfind(object, memorylist)
        if listfound is not None:
            if object.strip("\n")[-1] == "<":
                memorylist.insert(listfound + 1, modify)
                return memorylist
            if object.strip("\n")[-1] == ">":
                return memorylist[int(linefind(object, memorylist))]
        elif listfound is None:
            return "ERROR 0010"


print(memorymodify("username <", 'LIST', 'test'))
print(memorymodify("logfilenumber >", 'LINE', "+1"))
"""
"""
object = "username"
modify = 'DESKTOP-TKIP36M,Coralie Mdc > Coralie'
with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
    memorylist = memoryfile.readlines()
    for i in range(len(memorylist)):
        memorylist[i] = memorylist[i].strip("\n")
        if memorylist[i] == f"{object} <":
            print(f"i : {i}, ligne : {memorylist[i]}")
"""
"""
object = "username"
modify = 'DESKTOP-TKIP36M,Coralie Mdc > Coralie'
with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
    memorylist = memoryfile.readlines()
    modify = modify.split(" > ")
    for i in range(len(memorylist)):
        memorylist[i] = memorylist[i].strip("\n")
        if memorylist[i] == f"{object} <":
            print(f"i : {i}, ligne : {memorylist[i]}")
            a = i
            inlist = True
        elif memorylist[i].startswith("\t"):
            if memorylist[i].startswith(f"\t{modify[0]}"):
                print(f"i : {i}, ligne : {memorylist[i]}")
        elif memorylist[i].count('<') >= 1:
            print(f"{memorylist[i]}")
            
"""
"""
object = "username"
modify = 'DESKTOP-TKIP36M,Coralie Mdc > Coralie'
with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
    memorylist = memoryfile.readlines()
    modify = modify.split(" > ")
    for i in range(len(memorylist)):
        memorylist[i] = memorylist[i].strip("\n")
        if memorylist[i] == f"{object} <":
            print(f"i : {i}, ligne : {memorylist[i]}")
            for a in range(i+1,len(memorylist)):
                memorylist[a] = memorylist[a].strip("\n")
                if memorylist[a][0] == "\t":
                    print(f"a : {a}, ligne : {memorylist[a]}")
                    if memorylist[a].split(" > ")[0].strip("\t") == modify[0]:
                        print("OK")
                elif memorylist[a][0] != "\t":
                    break
                    """
"""
object = "username"
modify = 'DESKTOP-TKIP36M,Coralie Mdc > Coralie'
with open('F:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
    memorylist = memoryfile.readlines()
    modify = modify.split(" > ")
    for i in range(len(memorylist)):
        memorylist[i] = memorylist[i].strip("\n")
        if memorylist[i] == f"{object} <":
            print(f"i : {i}, ligne : {memorylist[i]}")
            for a in range(i+1,len(memorylist)):
                memorylist[a] = memorylist[a].strip("\n")
                if memorylist[a][0] == "\t":
                    print(f"a : {a}, ligne : {memorylist[a]}")
                    if memorylist[a].split(" > ")[0].strip("\t") == modify[0]:
                        print("OK")
                        memorylist[a] = f"{memorylist[a].split(' > ')[0]} > {modify[1]}"
                    
                elif memorylist[a][0] != "\t":
                    break
            memorylist.insert(i + 1, modify[1])
                
"""
"""
def memorymodifylist(object, modify):
    # object 'nom de la catégorie à modifier'
    # modify 'os.COMPUTERNAME, os.USERNAME > Nouveau nom'
    with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        modify = modify.split(" > ")
        for i in range(len(memorylist)):
            memorylist[i] = memorylist[i].strip("\n")
            if memorylist[i] == f"{object} <":
                for a in range(i + 1, len(memorylist)):
                    memorylist[a] = memorylist[a].strip("\n")
                    if memorylist[a].split(" > ")[0].strip("\t") == modify[0]:
                        memorylist[a] = f"{memorylist[a].split(' > ')[0]} > {modify[1]}"
                        break
                    elif memorylist[a][0] != "\t":
                        memorylist.insert(i + 1, f"\t{modify[0]} > {modify[1]}")
                        break
    with open('E:\\pyka\\memory\\memory.txt', 'w', encoding="UTF8") as memoryout:
        for memoryline in memorylist:
            memoryout.write(f"{memoryline}\n")


def memorymodifyline(object, modify):
    with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        for i in range((len(memorylist))):
            memorylist[i] = memorylist[i].strip("\n")
            a = memorylist[i].split(" ")
            if not a == ">" or a[1] == ">" and not a[0].startswith("\t"):
                if a[0] == object:
                    if memorylist[i][memorylist[i].find(">") + 2:memorylist[i].find(">") + 3 + len(a[-1])].isnumeric():
                        if modify.isnumeric():
                            modify = int(modify)
                            memorylist[i] = f"{a[0]} {a[1]} {modify}"
                        else:
                            if modify[0] == "+" and modify[0:].isnumeric():
                                memorylist[i] = f"{a[0]} {a[1]} {int(a[2]) + int(modify.strip('+'))}"
                            elif modify[0] == "-" and modify[0:].isnumeric():
                                memorylist[i] = f"{a[0]} {a[1]} {int(a[2]) - int(modify.strip('-'))}"
                            elif not modify.isnumeric():
                                memorylist[i] = f"{a[0]} {a[1]} {modify}"

                    else:
                        memorylist[i] = f"{a[0]} {a[1]} {modify}"

        with open('E:\\pyka\\memory\\memory.txt', 'w', encoding="UTF8") as memoryout:
            memorylist = memoryfile.readlines()
            for memoryline in memorylist:
                memoryout.write(f"{memoryline}\n")


def default(text, default):
    a = input(text)
    if a == "#":
        return default
    else:
        return a


def memorysearchline(object):
    # object 'nom de la ligne'
    with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        for i in range((len(memorylist))):
            memorylist[i] = memorylist[i].strip("\n")
            a = memorylist[i].split(" ")
            if a[0] == object and a[1] == ">":
                return a[2]


def memorysearchlist(object):
    # object ['nom de la catégorie', 'la ligne']
    with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        if type(object) == list:
            if f"{object[0]} <\n" in memorylist:
                for i in range(len(memorylist)):
                    memorylist[i] = memorylist[i].strip("\n")
                    if memorylist[i] == f"{object[0]} <":
                        for a in range(i + 1, len(memorylist)):
                            memorylist[a] = memorylist[a].strip("\n")
                            if memorylist[a] == ">":
                                return None
                            elif memorylist[a] == f"\t{object[1]} > {memorylist[a].split(' > ')[1]}":
                                return memorylist[a].split(' > ')[1]


print(memorysearchline('lang'))
print(memorysearchlist(['username', 'DESKTOP-TKIP36M,Coralie Mdc']))
memorymodifylist('username', 'DESKTOP-TKIP36M,ASH_Poitiers > Le Tester')
"""
"""
def memorysearchline(object):
    with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        for i in range((len(memorylist))):
            memorylist[i] = memorylist[i].strip("\n")
            a = memorylist[i].split(" ")
            if a[0] == object and a[1] == ">":
                return a[2]


def memorysearchlist(object):
    with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        if type(object) == list:
            if f"{object[0]} <\n" in memorylist:
                for i in range(len(memorylist)):
                    memorylist[i] = memorylist[i].strip("\n")
                    if memorylist[i] == f"{object[0]} <":
                        for a in range(i + 1, len(memorylist)):
                            memorylist[a] = memorylist[a].strip("\n")
                            if memorylist[a] == ">":
                                return None
                            elif memorylist[a] == f"\t{object[1]} > {memorylist[a].split(' > ')[1]}":
                                return memorylist[a].split(' > ')[1]


def memorymodifylist(object, modify):
    with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        modify = modify.split(" > ")
        for i in range(len(memorylist)):
            memorylist[i] = memorylist[i].strip("\n")
            if memorylist[i] == f"{object} <":
                for a in range(i + 1, len(memorylist)):
                    memorylist[a] = memorylist[a].strip("\n")
                    if memorylist[a].split(" > ")[0].strip("\t") == modify[0]:
                        memorylist[a] = f"{memorylist[a].split(' > ')[0]} > {modify[1]}"
                        break
                    elif memorylist[a][0] != "\t":
                        memorylist.insert(i + 1, f"\t{modify[0]} > {modify[1]}")
                        break
    with open('E:\\pyka\\memory\\memory.txt', 'w', encoding="UTF8") as memoryout:
        for memoryline in memorylist:
            memoryout.write(f"{memoryline}\n")


def memorymodifyline(object, modify):
    with open('E:\\pyka\\memory\\memory.txt', 'r', encoding="UTF8") as memoryfile:
        memorylist = memoryfile.readlines()
        for i in range((len(memorylist))):
            memorylist[i] = memorylist[i].strip("\n")
            a = memorylist[i].split(" ")
            if not a == ">" or a[1] == ">" and not a[0].startswith("\t"):
                if a[0] == object:
                    if memorylist[i][memorylist[i].find(">") + 2:memorylist[i].find(">") + 3 + len(a[-1])].isnumeric():
                        if modify.isnumeric():
                            modify = int(modify)
                            memorylist[i] = f"{a[0]} {a[1]} {modify}"
                        else:
                            if modify[0] == "+" and modify[0:].isnumeric():
                                memorylist[i] = f"{a[0]} {a[1]} {int(a[2]) + int(modify.strip('+'))}"
                            elif modify[0] == "-" and modify[0:].isnumeric():
                                memorylist[i] = f"{a[0]} {a[1]} {int(a[2]) - int(modify.strip('-'))}"
                            elif not modify.isnumeric():
                                memorylist[i] = f"{a[0]} {a[1]} {modify}"

                    else:
                        memorylist[i] = f"{a[0]} {a[1]} {modify}"

        with open('E:\\pyka\\memory\\memory.txt', 'w', encoding="UTF8") as memoryout:
            for memoryline in memorylist:
                memoryout.write(f"{memoryline}\n")
"""
"""
import urllib
import time
a = urllib.request.urlopen(f"https://artii.herokuapp.com/fonts_list")
c = a.read().decode()
b = c.split("\n")
b.remove("maxfour")
b.remove("pyramid")
for font in b:
    time.sleep(4)
    f = urllib.request.urlopen(f"https://artii.herokuapp.com/make?text=Test,+Louis&font={font}")
    print(f.read().decode())
    print(font)
"""
"""
import urllib.request
import json
import os
import time

with open("E:\\pyka\\character\\available character.json", encoding='UTF8') as data:
    data = json.load(data)

available_character = list()
font = "nancyj-underlined"

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
"""
"""
morpioncase = {"A0": " ", "A1": " ", "A2": " ", "B0": " ", "B1": " ", "B2": " ", "C0": " ", "C1": " ", "C2": " "}

print(f"╔═══╦═══╦═══╗\n║ {morpioncase['A0']} ║ {morpioncase['A1']} ║ {morpioncase['A2']} ║\n╠═══╬═══╬═══╣\n"
      f"║ {morpioncase['B0']} ║ {morpioncase['B1']} ║ {morpioncase['B2']} ║\n╠═══╬═══╬═══╣\n║ {morpioncase['C0']} ║ "
      f"{morpioncase['C1']} ║ {morpioncase['C2']} ║\n╚═══╩═══╩═══╝")
"""
