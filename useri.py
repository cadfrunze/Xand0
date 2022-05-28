
import random
import os
import time

user1 = ""
user2 = ""
lista_useri = []
# Innregistrare useri
def useri():
    necenzurat = ["Pula", "Pulla", "Pizda", "Puta", "Coi", "Coaie", "Sugaci", "Sugi", "Suji", "Tampit", "Fuck", "Laba",]
    semne = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "`", "-", "=", "\"", ";", "'", ",", ".",
            "~", "@", "#", "$", "%", "^", "&" ,"*", "(", ")", "_", "+", "[", "]", "{", "}", "|", ":", "<", ">", "?", "/", " "]
    user_proba = ""
    incercari = 0
    game_1a = False
    game_1b = False
    game1 = True
    while incercari <= 3 and game1 == True:
        if incercari == 0:
            user1 = input("Primul jucator, introdu' un nume >>> ").capitalize()
        for a in user1:
            if a in semne:
                continue
            else:
                user_proba = user_proba + a
        if user_proba in necenzurat:
            if incercari < 2:
                os.system('cls')
                user_proba = ""
                user1 = input("Hey!, vezi ca ai scris o injuratura, scrieti un nume si gata! >>> ").capitalize()
                incercari = incercari + 1
                continue
            elif incercari == 2:
                os.system('cls')
                user_proba = ""
                user1 = input("Hey! ultima incercare! , ai scris o injuratura, scrieti un nume si gata! >>> ").capitalize()
                incercari = incercari + 1
                continue
            elif incercari == 3:
                os.system('cls')
                print("Program inchis! Nerespectare cerinte")
                game1 = False
        elif len(user1) <= 2:
            user_proba = ""
            if incercari < 2:
                os.system('cls')
                user1 = input("Hey!, vezi numele tau contine mai putin de 3 caractere, scrieun nume cu un numar mai mare de 3 caractere! >>> ").capitalize()
                incercari = incercari + 1
                continue
            elif incercari == 2:
                os.system('cls')
                user1 = input("Hey! ultima incercare!, vezi numele tau contine mai putin de 3 caractere, scrieun nume cu un numar mai mare de 3 caractere! >>> ").capitalize()
                incercari = incercari + 1
                continue
            elif incercari == 3:
                os.system('cls')
                print("Program inchis! Nerespectare cerinte")
                game1 = False
        elif len(user1) >= 3 and user1 not in necenzurat:
            print(f"Bun venit {user1}")
            lista_useri.append(user1)
            user_proba = ""
            incercari = 0
            game1 = False
            game_1a = True
    if game_1a == True:
        game2 = True 
        while incercari <= 3 and game2 == True:
            if incercari == 0:
                user2 = input("Al doilea jucator, introdu' un nume >>> ").capitalize()
            if user2 == user1:
                os.system('cls')
                if incercari == 2:
                    user2 = input(f"Hey!, ultima incercare!, vezi ca ai introdus acelasi nume ca si {user1} >> ").capitalize()
                    incercari = incercari + 1
                    continue
                elif incercari < 2:
                    user2 = input(f"Hey!, vezi ca ai introdus acelasi nume ca si {user1} >> ").capitalize()
                    incercari = incercari + 1
                    continue
                elif incercari == 3:
                    print("Program inchis! Nerespectare cerinte")
                    game2 = False
            for a in user2:
                if a in semne:
                    continue
                else:
                    user_proba = user_proba + a
            if user_proba in necenzurat:
                if incercari < 2:
                    os.system('cls')
                    user_proba = ""
                    user2 = input("Hmmm..., vezi ca ai scris o injuratura, scrieti un nume si gata! >>> ").capitalize()
                    incercari = incercari + 1
                    continue
                elif incercari == 2:
                    os.system('cls')
                    user_proba = ""
                    user2 = input("Hey! ultima incercare! , ai scris o injuratura, scrieti un nume si gata! >>> ").capitalize()
                    incercari = incercari + 1
                    continue
                elif incercari == 3:
                    os.system('cls')
                    print("Program inchis! Nerespectare cerinte")
                    game2 = False
            elif len(user2) <= 2:
                os.system('cls')
                user_proba = ""
                if incercari < 2:
                    user2 = input("Hey!, vezi numele tau contine mai putin de 3 caractere, scrieun nume cu un numar mai mare de 3 caractere! >>> ").capitalize()
                    incercari = incercari + 1
                    continue
                elif incercari == 2:
                    user2 = input("Hey! ultima incercare!, vezi numele tau contine mai putin de 3 caractere, scrieun nume cu un numar mai mare de 3 caractere! >>> ").capitalize()
                    incercari = incercari + 1
                    continue
                elif incercari == 3:
                    print("Program inchis! Nerespectare cerinte")
                    game2 = False
            elif len(user2) >= 3 and user2 not in necenzurat and user2 != user1:
                print(f"Bun venit si tie {user2}")
                lista_useri.append(user2)
                user_proba = ""
                incercari = 0
                game2 = False
                game_1b = True
    if game_1a == True and game_1b == True:       
        useri_dict = {
            "user_X": random.choice(lista_useri),
            }
        if useri_dict["user_X"] == user1:
            useri_dict["user_X"] = [user1, "X", 0,]
            useri_dict["user_0"] = [user2, "0", 0] 
        elif useri_dict["user_X"] == user2:
            useri_dict["user_X"] = [user2, "X", 0]
            useri_dict["user_0"] = [user1, "0", 0]
        return useri_dict
os.system('cls')

useri_dict = useri()
print(f"Primul care incepe este {useri_dict['user_X'][0]} si joaca cu {useri_dict['user_X'][1]}, iar apoi {useri_dict['user_0'][0]} si joaca cu {useri_dict['user_0'][1]}")
time.sleep(3)















