# Ce code a été créé par Ic3Sh4rk | This code was created by Ic3Sh4rk


"""
feature :
    recherche internet
   simplification du code
   commande de vérification

note :
data['words']['help_words']
data['words']['hello_words']
data['words']['cancel_words']
data['words']['bye_words']['good_night']
data['words']['bye_words']['bye']
data['words']['fonction_words']['change_name']
data['words']['fonction_words']['conversion']
data['words']['fonction_words']['activation_log']
data['words']['fonction_words']['desactivation_log']
data['words']['yes_words']
data['words']['no_words']
"""
#
#  import zone
#
import os
import time
import json


#
#  fonction zone
#
def log(reply, username, log, reponse=None):

    if log is True:
        import time
        base = f"[{time.strftime('%H:%M:%S')}-{username}]"
        if reponse is None:
            while True:
                try:
                    with open(f"E:\\pyka\\log\\{os.environ['COMPUTERNAME']}\\{time.strftime('%d-%m-%Y')}.log", mode='a',
                              encoding='UTF8') as log_file:
                        log_file.write(f"{base} : {reply}\n")
                        break
                except FileNotFoundError:
                    os.mkdir(f"E:\\pyka\\log\\{os.environ['COMPUTERNAME']}\\")
        else:
            while True:
                try:
                    with open(f"E:\\pyka\\log\\{os.environ['COMPUTERNAME']}\\{time.strftime('%d-%m-%Y')}.log", mode='a',
                              encoding='UTF8') as log_file:
                        reponse = reponse.replace("\n", f"\n{' ' * int(len(base))} > ")
                        log_file.write(f"{base} : {reply}\n{' ' * int(len(base))} > {reponse}\n")
                        break
                except FileNotFoundError:
                    os.mkdir(f"E:\\pyka\\log\\{os.environ['COMPUTERNAME']}\\")


#
#  le fichier memory.json est transformé en variables python
#
with open('E:\\pyka\\memory\\memory.json', encoding='UTF8') as memory_file:
    data = json.load(memory_file)

try:
    USERNAME = data["memory"]["profiles"][os.environ['COMPUTERNAME']][os.environ['USERNAME']]
except KeyError:
    USERNAME = os.environ['USERNAME']
    data["memory"]["profiles"][os.environ['COMPUTERNAME']][os.environ['USERNAME']] = USERNAME
    with open("E:\\pyka\\memory\\memory.json", mode="w", encoding="UTF8") as data_file:
        json.dump(data, data_file, ensure_ascii=False, indent=4)

#
#  vérification dev
#
print(f"{' ' * 13}help words : {data['words']['help_words']}\n{' ' * 12}hello words : {data['words']['hello_words']}\n "
      f"          cancel words : {data['words']['cancel_words']}\n       conversion words : "
      f"{data['words']['fonction_words']['conversion']}\n      change name words : "
      f"{data['words']['fonction_words']['change_name']}\n   activation log words : "
      f"{data['words']['fonction_words']['activation_log']}\ndesactivation log words : "
      f"{data['words']['fonction_words']['desactivation_log']}\n{' ' * 14}yes words : {data['words']['yes_words']}\n"
      f"{' ' * 15}no words : {data['words']['no_words']}\n       good night words : "
      f"{data['words']['bye_words']['good_night']}\n              bye words : {data['words']['bye_words']['bye']}")

#
#  salutation par rapport à l'heure
#
if 6 <= int(time.strftime("%H")) <= 16:
    print(f"Bonjour {USERNAME}")
else:
    print(f"Bonsoir {USERNAME}")

#
#  programme principale
#
reply = ""
while reply != "stop":
    reply = str(input(" > ").lower().strip())
    if reply != "":
        #
        #  Bonjours
        #
        if reply in data['words']["hello_words"]:
            if 6 <= int(time.strftime("%H")) <= 16:
                log(reply, USERNAME, data["memory"]["log"], f"Bonjour {USERNAME}")
                print(f"Bonjour {USERNAME}")
            else:
                log(reply, USERNAME, data["memory"]["log"], f"Bonsoir {USERNAME}")
                print(f"Bonsoir {USERNAME}")
        #
        #  Aide
        #
        elif reply in data['words']["help_words"]:
            # en
            if data["memory"]["lang"] == 'en':
                log(reply, USERNAME, data["memory"]["log"], f"Do you want change the default language ? >")
                reply = input("Do you want change the default language ?\n > ")
            # fr
            elif data["memory"]["lang"] == 'fr':
                log(reply, USERNAME, data["memory"]["log"], f"Voulez-vous changer la langue par défaut ? >")
                reply = input("Voulez-vous changer la langue par défaut ?\n > ")
            if reply in data['words']['yes_words']:
                # en
                if data["memory"]["lang"] == 'en':
                    while reply not in data['words']['no_words'] or reply in data['words']['cancel_words']:
                        log(reply, USERNAME, data["memory"]["log"], f"Available languages : fr >")
                        reply = input("Available languages : fr\n >")
                        if reply == 'fr':
                            data["memory"]["lang"] = 'fr'
                            with open("E:\\pyka\\memory\\memory.json", mode="w", encoding="UTF8") as data_file:
                                json.dump(data, data_file, ensure_ascii=False, indent=4)
                            log(reply, USERNAME, data["memory"]["log"], f"The language has been changed\rdata"
                                                                        f"[\"memory\"][\"lang\"] = 'en'")
                            print("The language has been changed")
                            break
                        else:
                            log(reply, USERNAME, data["memory"]["log"], f"Please enter a correct language or to stop"
                                                                        f" enter cancel")
                            print("Please enter a correct language or to stop enter cancel")
                # fr
                elif data["memory"]["lang"] == 'fr':
                    while reply not in data['words']['no_words'] or reply == "stop" or reply == "annuler":
                        log(reply, USERNAME, data["memory"]["log"], f"Langue disponible : en >")
                        reply = input("Langue disponible : en\n >")
                        if reply == 'en':
                            data["memory"]["lang"] = 'en'
                            with open("E:\\pyka\\memory\\memory.json", mode="w", encoding="UTF8") as data_file:
                                json.dump(data, data_file, ensure_ascii=False, indent=4)
                            log(reply, USERNAME, data["memory"]["log"], f"La langue a bien été modifier\rdata"
                                                                        f"[\"memory\"][\"lang\"] = 'en'")
                            print("La langue a bien été modifier")
                            break
                        else:
                            log(reply, USERNAME, data["memory"]["log"], f"Veuillez entrer un langue correct ou pour"
                                                                        f" arrêter entrez annuler")
                            print("Veuillez entrer un langue correct ou pour arrêter entrez annuler")
            elif reply in data['words']['no_words']:
                log(reply, USERNAME, data["memory"]["log"], f"Ok")
                print("Ok")
        #
        #  Fonction change de surnom
        #
        elif reply in data['words']["fonction_words"]["change_name"]:
            log(reply, USERNAME, data["memory"]["log"], f"Quel est votre nouveau nom ? >")
            USERNAME = input("Quel est votre nouveau nom ?\n >")
            log(USERNAME, USERNAME, f"D'accord je vous appelerais {USERNAME} maintenant\n"
                                    "Voulez-vous enregistrer ce nom ? >")
            print(f"D'accord je vous appelerais {USERNAME} maintenant")
            reply = input("Voulez-vous enregistrer ce nom ?\n > ")
            if reply in data['words']['yes_words']:
                data["memory"]["profiles"][os.environ['COMPUTERNAME']][os.environ['USERNAME']] = USERNAME
                with open("E:\\pyka\\memory\\memory.json", mode="w", encoding="UTF8") as data_file:
                    json.dump(data, data_file, ensure_ascii=False, indent=4)
                log(reply, USERNAME, data["memory"]["log"], "Votre nouveau nom d'utilisateur à bien été energistrée"
                                                            f"\rdata[\"memory\"][\"profiles\"]"
                                                            f"[{os.environ['COMPUTERNAME}']}]"
                                                            f"[{os.environ['USERNAME']}] = USERNAME")
                print("Votre nouveau nom d'utilisateur à bien été energistrée")
            elif reply in data['words']['no_words']:
                log(reply, USERNAME, data["memory"]["log"], "Ok")
                print("Ok")
            else:
                log(reply, USERNAME, data["memory"]["log"], "Veuillez répondre par oui ou par non")
                print("Veuillez répondre par oui ou par non")
        #
        #  Fonction convertion (en cours)
        #
        elif reply in data['words']['fonction_words']['conversion']:
            log(reply, USERNAME, data["memory"]["log"], "Que voulez-vous convertir ? >")
            reply = input("Que voulez-vous convertir ?\n > ")
            if reply.split(" > "):
                print("ok")
            else:
                print("Ecrivez de la manière\"%% > %%\"")
        #
        #  Activation des registres
        #
        elif data["memory"]["log"] is True and reply in data['words']['fonction_words']['activation_log']:
            log(reply, USERNAME, data["memory"]["log"], "Les registres sont déja activé\nVoulez vous les "
                                                        "désactivés ? >")
            print("Les registres sont déja activé")
            reply = input("Voulez-vous les désactivés ?\n > ")
            if reply in data['words']['yes_words']:
                data["memory"]["log"] = False
                with open("E:\\pyka\\memory\\memory.json", mode="w", encoding="UTF8") as data_file:
                    json.dump(data, data_file, ensure_ascii=False, indent=4)
                    log(reply, USERNAME, True, "Les registres sont désormais désactiver")
                print("Les registres sont désormais désactiver")
            elif reply in data['words']['no_words']:
                log(reply, USERNAME, data["memory"]["log"], "Ok")
                print("Ok")
            else:
                log(reply, USERNAME, data["memory"]["log"], "Veuillez répondre par oui ou par non")
                print("Veuillez répondre par oui ou par non")
        elif data["memory"]["log"] is False and reply in data['words']['fonction_words']['activation_log']:
            reply = input("Voulez-vous activer les registres ?\n > ")
            if reply in data['words']['yes_words']:
                data["memory"]["log"] = True
                with open("E:\\pyka\\memory\\memory.json", mode="w", encoding="UTF8") as data_file:
                    json.dump(data, data_file, ensure_ascii=False, indent=4)
                    log(reply, USERNAME, data["memory"]["log"], "Les registres sont désormais activer")
                print("Les registres sont désormais activer")
            elif reply in data['words']['no_words']:
                print("Ok")
            else:
                print("Veuillez répondre par oui ou par non")
        #
        #  Activation des registres
        #
        elif data["memory"]["log"] is False and reply in data['words']['fonction_words']['desactivation_log']:
            log(reply, USERNAME, data["memory"]["log"], "Les registres sont déja désactivé\nVoulez vous les "
                                                        "activés ? >")
            print("Les registres sont déja désactivé")
            reply = input("Voulez-vous les activés ?\n > ")
            if reply in data['words']['yes_words']:
                data["memory"]["log"] = True
                with open("E:\\pyka\\memory\\memory.json", mode="w", encoding="UTF8") as data_file:
                    json.dump(data, data_file, ensure_ascii=False, indent=4)
                    log(reply, USERNAME, data["memory"]["log"], "Les registres sont désormais activer")
                print("Les registres sont désormais activer")
            elif reply in data['words']['no_words']:
                log(reply, USERNAME, data["memory"]["log"], "Ok")
                print("Ok")
            else:
                log(reply, USERNAME, data["memory"]["log"], "Veuillez répondre par oui ou par non")
                print("Veuillez répondre par oui ou par non")
        elif data["memory"]["log"] is True and reply in data['words']['fonction_words']['desactivation_log']:
            reply = input("Voulez-vous désactiver les registres ?\n > ")
            if reply in data['words']['yes_words']:
                data["memory"]["log"] = False
                with open("E:\\pyka\\memory\\memory.json", mode="w", encoding="UTF8") as data_file:
                    json.dump(data, data_file, ensure_ascii=False, indent=4)
                    log(reply, USERNAME, True, "Les registres sont désormais désactiver")
                print("Les registres sont   désormais désactiver")
            elif reply in data['words']['no_words']:
                log(reply, USERNAME, data["memory"]["log"], "Ok")
                print("Ok")
            else:
                log(reply, USERNAME, data["memory"]["log"], "Veuillez répondre par oui ou par non")
                print("Veuillez répondre par oui ou par non")

        else:
            #
            #  Stop
            #
            if reply == "stop":
                pass
            #
            #  Bonne nuit
            #
            elif reply in data['words']['bye_words']['good_night'] and not 6 <= int(time.strftime("%H")) <= 16:
                log(reply, USERNAME, data["memory"]["log"], "Bonne nuit\nExit Code : Bot set > OFF")
                print("Bonne nuit")
                exit("Bot set > OFF")
            #
            #  Aurevoir
            #
            elif reply in data['words']['bye_words']['bye'] and 6 <= int(time.strftime("%H")) <= 16:
                log(reply, USERNAME, data["memory"]["log"], "Aurevoir\nExit Code : Bot set > OFF")
                print("Aurevoir")
                exit("Bot set > OFF")
            else:
                #
                #  Autres
                #
                if data["memory"]["lang"] == 'en':
                    log(reply, USERNAME, data["memory"]["log"], "What ?")
                    print("What ?")
                elif data["memory"]["lang"] == 'fr':
                    log(reply, USERNAME, data["memory"]["log"], "Quoi ?")
                    print("Quoi ?")

#
#  vérification dev
#
log(reply, USERNAME, data["memory"]["log"], f"Exit Code : Bot set > OFF")
print("")
exit("Bot set > OFF")
