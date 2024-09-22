import json
import string
import urllib
ans = input("> ")
if ans.startswith("setup"):
     test = ans.split(" ")
     for i in range(len(test)-1):
         if test[i+1].startswith("http:") or test[i+1].startswith("https:"):
             with open(urllib):

lang = input("Quel est la lang du message chiffrer > ")