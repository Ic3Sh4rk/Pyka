# Ce code a été créé par Ic3Sh4rk | This code was created by Ic3Sh4rk


"""
note :
words['help_words']
words['hello_words']
words['cancel_words']
words['bye_words']['good_night']
words['bye_words']['bye']
words['fonction_words']['change_name']
words['fonction_words']['conversion']
words['fonction_words']['activation_log']
words['fonction_words']['desactivation_log']
words['yes_words']
words['no_words']
"""

import os
import time
import json


def log(reply, username, bool_log=True, answer=None):
    """
    reply {str} : ce que l'utilisateur à envoyer
    username {str} : le nom d'utilisateur
    log {bool} : si les logs sont activées
    reponse {str | None} : réponse du programme
    """
    if bool_log is True:
        import time
        base = f"[{time.strftime('%H:%M:%S')}-{username}]"
        if answer is None:
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
                        answer = answer.replace("\n", f"\n{' ' * int(len(base))} > ")
                        log_file.write(f"{base} : {reply}\n{' ' * int(len(base))} > {answer}\n")
                        break
                except FileNotFoundError:
                    os.mkdir(f"E:\\pyka\\log\\{os.environ['COMPUTERNAME']}\\")


def setup_memory():
    while True:
        try:
            with open("memory\\memory2.json", encoding='UTF8') as memory_file:
                data = json.load(memory_file)
                return data
        except FileNotFoundError:
            if not os.path.exists("memory"):
                os.mkdir("memory")
            nickname = ''
            data = {'lang': 'fr'}
            while nickname == '':
                if data['lang'] == 'fr':
                    nickname = input("Quel est votre surnom ?\n")
                elif data['lang'] == 'en':
                    nickname = input("What your nickname ?\n")
                else:
                    data['lang'] = 'en'
                    nickname = ''
            data = {
                'lang': 'fr',
                'number_of_log_files': 0,
                'log': True,
                'profiles':
                    {f'{os.environ["COMPUTERNAME"]}':
                         {f'{os.environ["USERNAME"]}': nickname}}}
            with open("memory\\memory2.json", mode='w', encoding='UTF8') as memory_file:
                json.dump(data, memory_file, ensure_ascii=False, indent=4)


def setup_words():
    while True:
        try:
            with open("words\\words.json", encoding='UTF8') as words_file:
                data = json.load(words_file)
                return data
        except FileNotFoundError:
            if not os.path.exists("words"):
                os.mkdir("words")
            data = {'help_words': ['?', '??', '???', 'help', 'aide'],
                    'hello_words': ['hello', 'hi', 'bonjour', 'bonjours', 'bonsoir', 'salut'],
                    'cancel_words': ['cancel', 'annuler'],
                    'bye_words': {
                        'good_night': ['bonne nuit', 'good night'],
                        'bye': ['aurevoir', 'bye']},
                    'play_words': ['veux-tu jouer avec moi', 'lance un jeu', 'tu veux jouer à un jeu',
                                   'do you want to play with me', 'start a game', 'you want to play a game',
                                   'launches a game', 'launch a game'],
                    'fonction_words': {
                        'change_name': ['modifies mon nom', 'modifies mon prénom', 'modifies mon surnom',
                                        "modifies mon nom d'utilisateur", 'change my name', 'change my username',
                                        'change my nickname'],
                        'conversion': ['conversion'],
                        'activation_log': ['active les registre', 'active les logs'],
                        'desactivation_log': ['desactive les registres', 'desactive les logs',
                                              'désactive les registres',
                                              'désactive les logs'],
                        'research_google': ['recherche', 'cherche', 'search', 'research']},
                    'yes_words': ['yep', 'yes', 'oui', 'yeah'], 'no_words': ['nop', 'no', 'non', 'nan'],
                    'politeness_word': ["s'il te plaît", "s'il te plait", 'stp', "s'il vous plaît", "s'il vous plait",
                                        'svp', 'please', 'pls'], 'politeness_end_word': ['merci', 'thank you', 'ty']}
            with open("words\\words.json", mode='w', encoding='UTF8') as words_file:
                json.dump(data, words_file, ensure_ascii=False, indent=4)


def setup_traduction():
    while True:
        try:
            with open("words\\translation.json", encoding='UTF8') as translation_file:
                data = json.load(translation_file)
                return data
        except FileNotFoundError:
            if not os.path.exists("words"):
                os.mkdir("words")
            data = {
                "day": {
                    "Monday": "Lundi",
                    "Tuesday": "Mardi",
                    "Wednesday": "Mercredi",
                    "Thursday": "Jeudi",
                    "Friday": "Vendredi",
                    "Saturday": "Samedi",
                    "Sunday": "Dimanche"
                },
                "month": {
                    "January": "Janvier",
                    "February": "Février",
                    "March": "Mars",
                    "April": "Avril",
                    "May": "Mai",
                    "June": "Juin",
                    "July": "Juillet",
                    "August": "Août",
                    "September": "Septembre",
                    "October": "Octobre",
                    "November": "Novembre",
                    "December": "Décembre"
                }
            }
            with open("words\\translation.json", mode='w', encoding='UTF8') as words_file:
                json.dump(data, words_file, ensure_ascii=False, indent=4)


def hello():
    if memory['lang'] == 'fr':
        print(f"{'Bonjour' if 6 <= int(time.strftime('%H')) <= 17 else 'Bonsoir'} {USERNAME}, nous sommes le "
              f"{translation['day'][time.strftime('%A')]} {time.strftime('%d')} "
              f"{translation['month'][time.strftime('%B')]} et il est {time.strftime('%H:%M')}.")  # Bonjour/Bonsoir ...
    elif memory['lang'] == 'en':
        print(time.strftime(f"Hello {USERNAME}, it is %A %d{'st' if time.strftime('%d')[-1] == 1 else ''}"
                            f"{'nd' if time.strftime('%d')[-1] == 2 else ''}"
                            f"{'rd' if time.strftime('%d')[-1] == 3 else ''}"
                            f"{'th' if time.strftime('%d')[-1] not in [1, 2, 3] else ''} {time.strftime('%B')} and it i"
                            f"s {time.strftime('%I.%M %p')}"))  # Hello ...


memory = setup_memory()
words = setup_words()
USERNAME = memory['profiles'][os.environ['COMPUTERNAME']][os.environ['USERNAME']]
translation = setup_traduction()
print(memory)
print(words)
hello()
