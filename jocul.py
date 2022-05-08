from useri import useri_dict
# Creeare si rulare joc



    

def joc():
    rand3 = ["[_]", "[_]", "[_]"]
    rand2 = ["[_]", "[_]", "[_]"]
    rand1 = ["[_]", "[_]", "[_]"]
    tabla = [rand1, rand2, rand3]
    print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
    
    xul = input(f"{useri_dict['user_X'][0]} introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
    if xul[1] == "a":
        sec_digit = 0
    elif xul[1] == "b":
        sec_digit = 1
    elif xul[1] == "c":
        sec_digit = 2
    first_digit = xul[0]
    first_digit = int(first_digit)

    tabla = tabla[first_digit - 1]
    tabla[sec_digit] = len(tabla) - sec_digit
    tabla[sec_digit] = "[x]"
    print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")







if len(useri_dict) == 2:
    joc()
