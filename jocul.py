from useri import useri_dict
import os
# Creeare si rulare joc
# Afisare cerinte!
rand3 = ["[_]", "[_]", "[_]"]
rand2 = ["[_]", "[_]", "[_]"]
rand1 = ["[_]", "[_]", "[_]"]

tabla = [rand1, rand2, rand3,]
mark_x = "[x]"
mark_o = "[o]"
prim_x = [mark_x, mark_x, mark_x]
prim_o = [mark_o, mark_o, mark_o]
empty_box = "[_]"
list_incercari = []
userul_o = useri_dict['user_0'][0]
userul_o = userul_o.center(30, "*")
userul_x = useri_dict['user_X'][0]
userul_x = userul_x.center(30, "*")
# Functie marcare X
def push_x(tabla,mark_x, useri_dict, userul_x):
    """Jocul pt X"""
    x_u = useri_dict["user_X"][1]
    x_u = x_u.center(30, "*")
    tabel_nr = ["1", "2", "3"]
    tabel_lit = ["a", "b", "c"]
    game1 = True
    cuvant1 = True
    print(userul_x)
    print(x_u)
    while game1:
        if cuvant1 == True:
            xul = input(">>> ")
        if xul[0] == "" or xul[0] == "" or xul[0] not in tabel_nr:
            xul = input(f" Hey! {useri_dict['user_X'][0]}, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
            cuvant1 = False
            continue
        elif xul[1] == "" or xul[1] == " " or xul[1] not in tabel_lit:
            xul = input(f" Hey! {useri_dict['user_X'][0]}, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
            cuvant1 = False
            continue
        while xul in list_incercari:
            xul = input(f" Hey! {useri_dict['user_X'][0]}, vezi ca ai gresit! (coordonate) Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
        list_incercari.append(xul)
        cuvant1 = True
        first_digit = int(xul[0])
        if xul[1] == "a":
            sec_digit = 0
        elif xul[1] == "b":
            sec_digit = 1
        elif xul[1] == "c":
            sec_digit = 2
        tabla = tabla[first_digit - 1]
        tabla[sec_digit] = len(tabla) - sec_digit
        tabla[sec_digit] = mark_x
        return tabla

# Functie marcare 0
def push_o(tabla, mark_o, useri_dict, userul_o):
    """Jocul pt 0"""
    o_u = useri_dict["user_0"][1]
    o_u = o_u.center(30, "*")
    tabel_nr = ["1", "2", "3"]
    tabel_lit = ["a", "b", "c"]
    game1 = True
    cuvant1 = True
    print(userul_o)
    print(o_u)
    while game1:
        if cuvant1 == True:
            oul = input(">>> ")
        if oul[0] == "" or oul[0] == " " or oul[0] not in tabel_nr:
            oul = input(f" 0 Hey! {useri_dict['user_0'][0]}, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ")
            cuvant1 = False
            continue
        elif oul[1] == "" or oul[1] == " " or oul[1] not in tabel_lit:
            oul = input(f" 0 Hey! {useri_dict['user_0'][0]}, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ")
            cuvant1 = False
            continue
        while oul in list_incercari:
            oul = input(f"0  Hey! {useri_dict['user_0'][0]}, vezi ca ai gresit (coordonate)! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
        list_incercari.append(oul)
        cuvant1 = True
        first_digit = int(oul[0])
        if oul[1] == "a":
            sec_digit = 0
        elif oul[1] == "b":
            sec_digit = 1
        elif oul[1] == "c":
            sec_digit = 2
        tabla = tabla[first_digit - 1]
        tabla[sec_digit] = len(tabla) - sec_digit
        tabla[sec_digit] = mark_o
        return tabla
            

# Functie jocul....Greu ii futa-l drequ'
def joc(tabla,mark_x,mark_o, prim_x, prim_o, empty_box, useri_dict, userul_x, userul_o):
    """Castigator sau remiza....Vai futa-l drequ'"""
    incercari_x = 0
    incercari_o = 0
    prima_etapa = True
    while prima_etapa:
        os.system('cls')
        print("Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C")
        print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
        if mark_x not in tabla[0] and mark_x not in tabla[1] and mark_x not in tabla[2]:
            push_x(tabla, mark_x, useri_dict, userul_x)
            incercari_x = incercari_x + 1
            os.system('cls')
        if mark_o not in tabla[0] and mark_o not in tabla[1] and mark_o not in tabla[2]:
            print("Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C")
            print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
            push_o(tabla, mark_o, useri_dict, userul_o)
            incercari_o = incercari_o + 1
            os.system('cls')
            print("Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C")
            print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
        for cautare in range(len(tabla)):
            if tabla[cautare] == prim_x:
                tabla[cautare].remove(mark_x)
                tabla[cautare].remove(mark_x)
                tabla[cautare].remove(mark_x)
                tabla[cautare].insert(0, "[X]")
                tabla[cautare].insert(1, "[X]")
                tabla[cautare].insert(2, "[X]")
                useri_dict['user_X'][2] = useri_dict['user_X'][2] + 1
                return tabla
            elif tabla[cautare] == prim_o:
                tabla[cautare].remove(mark_o)
                tabla[cautare].remove(mark_o)
                tabla[cautare].remove(mark_o)
                tabla[cautare].insert(0, "[0]")
                tabla[cautare].insert(1, "[0]")
                tabla[cautare].insert(2, "[0]")
                useri_dict['user_0'][2] = useri_dict['user_0'][2] + 1
                return tabla
        if rand1[0] == mark_x and rand2[0] == mark_x and rand3[0] == mark_x:
            rand1.remove(mark_x)
            rand2.remove(mark_x)
            rand3.remove(mark_x)
            rand1.insert(0, "[X]")
            rand2.insert(0, "[X]")
            rand3.insert(0, "[X]")
            useri_dict['user_X'][2] = useri_dict['user_X'][2] + 1
            return tabla
        elif rand1[0] == mark_o and rand2[0] == mark_o and rand3[0] == mark_o:
            rand1.remove(mark_o)
            rand2.remove(mark_o)
            rand3.remove(mark_o)
            rand1.insert(0, "[0]")
            rand2.insert(0, "[0]")
            rand3.insert(0, "[0]")
            useri_dict['user_0'][2] = useri_dict['user_0'][2] + 1
            return tabla
        elif rand1[1] == mark_x and rand2[1] == mark_x and rand3[1] == mark_x:
            rand1.remove(mark_x)
            rand2.remove(mark_x)
            rand3.remove(mark_x)
            rand1.insert(1, "[X]")
            rand2.insert(1, "[X]")
            rand3.insert(1, "[X]")
            useri_dict['user_X'][2] = useri_dict['user_X'][2] + 1
            return tabla
        elif rand1[1] == mark_o and rand2[1] == mark_o and rand3[1] == mark_o:
            rand1.remove(mark_o)
            rand2.remove(mark_o)
            rand3.remove(mark_o)
            rand1.insert(1, "[0]")
            rand2.insert(1, "[0]")
            rand3.insert(1, "[0]")
            useri_dict['user_0'][2] = useri_dict['user_0'][2] + 1
            return tabla
        elif rand1[2] == mark_x and rand2[2] == mark_x and rand3[2] == mark_x:
            rand1.remove(mark_x)
            rand2.remove(mark_x)
            rand3.remove(mark_x)
            rand1.insert(2, "[X]")
            rand2.insert(2, "[X]")
            rand3.insert(2, "[X]")
            useri_dict['user_X'][2] = useri_dict['user_X'][2] + 1
            return tabla
        elif rand1[2] == mark_o and rand2[2] == mark_o and rand3[2] == mark_o:
            rand1.remove(mark_o)
            rand2.remove(mark_o)
            rand3.remove(mark_o)
            rand1.insert(2, "[0]")
            rand2.insert(2, "[0]")
            rand3.insert(2, "[0]")
            useri_dict['user_0'][2] = useri_dict['user_0'][2] + 1
            return tabla
        elif rand1[0] == mark_x and rand2[1] == mark_x and rand3[2] == mark_x:
            rand1.remove(mark_x)
            rand2.remove(mark_x)
            rand3.remove(mark_x)
            rand1.insert(0, "[X]")
            rand2.insert(1, "[X]")
            rand3.insert(2, "[X]")
            useri_dict['user_X'][2] = useri_dict['user_X'][2] + 1
            return tabla
        elif rand1[0] == mark_o and rand2[1] == mark_o and rand3[2] == mark_o:
            rand1.remove(mark_o)
            rand2.remove(mark_o)
            rand3.remove(mark_o)
            rand1.insert(0, "[0]")
            rand2.insert(1, "[0]")
            rand3.insert(2, "[0]")
            useri_dict['user_0'][2] = useri_dict['user_0'][2] + 1
            return tabla
        elif rand3[0] == mark_x and rand2[1] == mark_x and rand1[2] == mark_x:
            rand3.remove(mark_x)
            rand2.remove(mark_x)
            rand1.remove(mark_x)
            rand3.insert(0, "[X]")
            rand2.insert(1, "[X]")
            rand1.insert(2, "[X]")
            useri_dict['user_X'][2] = useri_dict['user_X'][2] + 1
            return tabla
        elif rand3[0] == mark_o and rand2[1] == mark_o and rand1[2] == mark_o:
            rand3.remove(mark_o)
            rand2.remove(mark_o)
            rand1.remove(mark_o)
            rand3.insert(0, "[0]")
            rand2.insert(1, "[0]")
            rand1.insert(2, "[0]")
            useri_dict['user_0'][2] = useri_dict['user_0'][2] + 1
            return tabla
        
        elif empty_box not in tabla[0] and empty_box not in tabla[1] and empty_box not in tabla[2]:
            print("Remiza")
            return tabla
        elif incercari_x == incercari_o:
            push_x(tabla, mark_x, useri_dict, userul_x)
            incercari_x = incercari_x + 1
            os.system('cls')
        elif incercari_x > incercari_o:
            push_o(tabla, mark_o, useri_dict, userul_o)
            incercari_o = incercari_o + 1
        os.system('cls')

# Afisare castigator sau remiza
def castigatori(useri_dict, userul_x, userul_o):
    os.system('cls')
    if useri_dict["user_X"][2] > useri_dict["user_0"][2]:
        if useri_dict["user_X"][2] == 1:
            print(userul_x)
            print(useri_dict["user_X"][0] + " " + "a castigat! si are " + str(useri_dict["user_X"][2]) + " " + "punct")
        else:
            print(userul_x)
            print(useri_dict["user_X"][0] + " " + "a castigat! si are " + str(useri_dict["user_X"][2]) + " " + "puncte")
        print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
    elif useri_dict["user_0"][2] > useri_dict["user_X"][2]:
        if useri_dict["user_0"][2] == 1:
            print(userul_o)
            print(useri_dict["user_0"][0] + " " + "a castigat! si are " + str(useri_dict["user_0"][2]) + " " + "punct")
        else:
            print(userul_o)
            print(useri_dict["user_0"][0] + " " + "a castigat! si are " + str(useri_dict["user_0"][2]) + " " + "puncte")
        print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
    else:
        remiza = "Remiza"
        remiza = remiza.center(30, "*")
        print(remiza)
        print("scor: " + str(useri_dict["user_X"][2]) + " >>> " + useri_dict["user_X"][0])
        print("scor: " + str(useri_dict["user_0"][2]) + " >>> " + useri_dict["user_0"][0])
        
        print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")