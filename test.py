
import os
# Creeare si rulare joc
rand3 = ["[_]", "[_]", "[_]"]
rand2 = ["[_]", "[_]", "[_]"]
rand1 = ["[_]", "[_]", "[_]"]
tabla = [rand1, rand2, rand3]
mark_x = "[x]"
mark_o = "[o]"
empty_box = "[_]"
list_incercari = []
def push_x(tabla,mark_x):
    """Jocul pt X"""
    tabel_nr = ["1", "2", "3"]
    tabel_lit = ["a", "b", "c"]
    game1 = True
    cuvant1 = True
    while game1:
        if cuvant1 == True:
            xul = input(f" introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
        if xul[0] == "" or xul[0] == "" or xul[0] not in tabel_nr:
            xul = input(f" Hey!, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
            cuvant1 = False
            continue
        elif xul[1] == "" or xul[1] == " " or xul[1] not in tabel_lit:
            xul = input(f" Hey!, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
            cuvant1 = False
            continue
        while xul in list_incercari:
            xul = input(f" Hey!, vezi ca ai gresit! (coordonate) Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
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
        tabla = [rand1, rand2, rand3]
        game1 = False
        print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
        return tabla


def push_o(tabla, mark_o):
    """Jocul pt 0"""
    tabel_nr = ["1", "2", "3"]
    tabel_lit = ["a", "b", "c"]
    game1 = True
    cuvant1 = True
    while game1:
        if cuvant1 == True:
            oul = input(f" 0 introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
        if oul[0] == "" or oul[0] == " " or oul[0] not in tabel_nr:
            oul = input(f" 0 Hey!, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ")
            cuvant1 = False
            continue
        elif oul[1] == "" or oul[1] == " " or oul[1] not in tabel_lit:
            oul = input(f" 0 Hey!, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ")
            cuvant1 = False
            continue
        while oul in list_incercari:
            oul = input(f"0  Hey!, vezi ca ai gresit (coordonate)! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
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
        tabla = [rand1, rand2, rand3]
        game1 = False
        print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
        return tabla
            
 

def joc(tabla,mark_x,mark_o, empty_box):
    """Castigator sau remiza"""
    incercari_x = 0
    incercari_o = 0
    list_x = []
    list_o = []
    prima_etapa = True
    print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
    while prima_etapa:
        if mark_x not in tabla[0] and mark_x not in tabla[1] and mark_x not in tabla[2]:
            push_x(tabla, mark_x)
            incercari_x = incercari_x + 1
        if mark_o not in tabla[0] and mark_o not in tabla[1] and mark_o not in tabla[2]:
            push_o(tabla, mark_o)
            incercari_o = incercari_o + 1
        for a in tabla[0]:
            if a == mark_x:
                list_x.append(a)
                if tabla[0] == list_x:
                    print("Prim_X")
                    prima_etapa = False
                    return tabla
            elif a == mark_o:
                list_o.append(a)
                if tabla[0] == list_o:
                    print("Prim_0")
                    prima_etapa = False
                    return tabla
        for a in tabla[1]:
            if a == mark_x:
                list_x.append(a)
                if tabla[1] == list_x:
                    print("Prim_X")
                    prima_etapa = False
                    return tabla
            elif a == mark_o:
                list_o.append(a)
                if tabla[1] == list_o:
                    print("Prim_0")
                    prima_etapa = False
                    return tabla
            for a in tabla[2]:
                if a == mark_x:
                    list_x.append(a)
                    if tabla[2] == list_x:
                        print("Prim_X")
                        prima_etapa = False
                        return tabla
                elif a == mark_o:
                    list_o.append(a)
                    if tabla[2] == list_o:
                        print("Prim_0")
                        prima_etapa = False
                        return tabla
            

            
        
        if incercari_o == incercari_x:
            push_x(tabla, mark_x)
            incercari_x = incercari_x + 1
            list_x = []
        elif incercari_x > incercari_o:
            push_o(tabla, mark_o)
            incercari_o = incercari_o + 1
            list_o = []
        

joc(tabla,mark_x,mark_o, empty_box)


