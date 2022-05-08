
# Creeare si rulare joc

def joc():
    rand3 = ["[_]", "[_]", "[_]"]
    rand2 = ["[_]", "[_]", "[_]"]
    rand1 = ["[_]", "[_]", "[_]"]
    tabla = [rand1, rand2, rand3]

    print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
    tabel_nr = ["1", "2", "3"]
    tabel_lit = ["a", "b", "c"]
    mark_X = "[x]"
    mark_0 = "[o]"
    game1 = True
    cuvant1 = True
    while game1:
        if cuvant1 == True:
            xul = input(f" introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
        if xul[0] == "" or xul[0] == "" or xul[0] not in tabel_nr:
            xul = input(f" Hey!, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ")
            cuvant1 = False
            continue
        elif xul[1] == "" or xul[1] == " " or xul[1] not in tabel_lit:
            xul = input(f" Hey!, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ")
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
        tabla[sec_digit] = mark_X
        print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
        tabla = [rand1, rand2, rand3]

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
            tabla[sec_digit] = mark_0
            print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
            tabla = [rand1, rand2, rand3]
            break
        
    
    


joc()





