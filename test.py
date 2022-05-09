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
    print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
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
        if xul in list_incercari:
            xul = input(f" Hey!, vezi ca ai gresit! (coordonate) Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
            continue
        list_incercari.append(xul)
        tabla = [rand1, rand2, rand3]
        print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
        tabla = [rand1, rand2, rand3]
        game1 = False
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
        if oul in list_incercari:
            oul = input(f"0  Hey!, vezi ca ai gresit (coordonate)! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
            continue
        list_incercari.append(oul)
        tabla = [rand1, rand2, rand3]
        print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
        game1 = False
        return tabla
            
 

def joc(tabla,mark_x,mark_o, empty_box):
    """Castigator sau remiza"""
    rand3_x = ["[x]", "[x]", "[x]"]
    rand2_x = ["[x]", "[x]", "[x]"]
    rand1_x = ["[x]", "[x]", "[x]"]
    cola_x = [rand1_x[0], rand2_x[0], rand3_x[0]]
    colb_x = [rand1_x[1], rand2_x[1], rand3_x[1]]
    colc_x = [rand1_x[2], rand2_x[2], rand3_x[2]]
    oblic_x_1 = [rand3_x[0], rand2_x[1], rand1_x[2]]
    oblic_x_2 = [rand1_x[0], rand2_x[1], rand3_x[2]]
    tabla_x = [rand1_x, rand2_x, rand3_x, cola_x, colb_x, colc_x ,oblic_x_1,oblic_x_2]

    rand3_o = ["[o]", "[o]", "[o]"]
    rand2_o = ["[o]", "[o]", "[o]"]
    rand1_o = ["[o]", "[o]", "[o]"]
    cola_o = [rand1_o[0], rand2_o[0], rand3_o[0]]
    colb_o = [rand1_o[1], rand2_o[1], rand3_o[1]]
    colc_o = [rand1_o[2], rand2_o[2], rand3_o[2]]
    oblic_o_1 = [rand3_o[0], rand2_o[1], rand1_o[2]]
    oblic_o_2 = [rand1_o[0], rand2_o[1], rand3_o[2]]
    tabla_o = [rand1_o, rand2_o, cola_o, colb_o, colc_o,rand3_o, oblic_o_1, oblic_o_2]
    incercari_x = 0
    incercari_o = 0
    prim_joc = True
    while incercari_x <= 9 and incercari_o <= 9:
        if prim_joc == True:
            for a in range(len(tabla)):
                if mark_x not in tabla[a] and a != len(tabla):
                    if a == len(tabla) - 1:
                        push_x(tabla, mark_x)
                        incercari_x = incercari_x + 1
                        push_o(tabla, mark_o)
                        incercari_o = incercari_o + 1
                        prim_joc = False
        
joc(tabla,mark_x,mark_o, empty_box)

