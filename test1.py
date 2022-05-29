

# def tabla():
#     rand3 = ["[_]", "[_]", "[_]"]
#     rand2 = ["[_]", "[_]", "[_]"]
#     rand1 = ["[_]", "[_]", "[_]"]
#     tabla = [rand1, rand2, rand3,]
#     tabla = f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C"
#     return tabla
# def tabla_x():
#     rand3_x = ["[x]", "[x]", "[x]"]
#     rand2_x = ["[x]", "[x]", "[x]"]
#     rand1_x = ["[x]", "[x]", "[x]"]
#     tabla_x = [rand1_x, rand2_x, rand3_x,]
#     return tabla_x
# def tabla_o():
#     rand3_o = ["[o]", "[o]", "[o]"]
#     rand2_o = ["[o]", "[o]", "[o]"]
#     rand1_o = ["[o]", "[o]", "[o]"]
#     tabla_o = [rand1_o, rand2_o, rand3_o,]
#     return tabla_o
    
# mark_x = "[x]"
# mark_o = "[o]"
# prim_x = [mark_x, mark_x, mark_x]
# prim_o = [mark_o, mark_o, mark_o]
# empty_box = "[_]"
# list_incercari = []

# userul_o = useri_dict['user_0'][0]
# userul_o = userul_o.center(30, "*")
# userul_x = useri_dict['user_X'][0]
# userul_x = userul_x.center(30, "*")

# # Functie marcare X
# def push_x(tabla,mark_x, useri_dict, userul_x):
#     """Jocul pt X"""
#     x_u = useri_dict["user_X"][1]
#     x_u = x_u.center(30, "*")
#     tabel_nr = ["1", "2", "3"]
#     tabel_lit = ["a", "b", "c"]
#     game1 = True
#     cuvant1 = True
#     print(userul_x)
#     print(x_u)
#     while game1:
#         if cuvant1 == True:
#             xul = input(">>> ")
#         if xul[0] == "" or xul[0] == "" or xul[0] not in tabel_nr:
#             xul = input(f" Hey! {useri_dict['user_X'][0]}, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
#             cuvant1 = False
#             continue
#         elif xul[1] == "" or xul[1] == " " or xul[1] not in tabel_lit:
#             xul = input(f" Hey! {useri_dict['user_X'][0]}, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
#             cuvant1 = False
#             continue
#         while xul in list_incercari:
#             xul = input(f" Hey! {useri_dict['user_X'][0]}, vezi ca ai gresit! (coordonate) Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
#         list_incercari.append(xul)
#         cuvant1 = True
#         first_digit = int(xul[0])
#         if xul[1] == "a":
#             sec_digit = 0
#         elif xul[1] == "b":
#             sec_digit = 1
#         elif xul[1] == "c":
#             sec_digit = 2
#         tabla = tabla[first_digit - 1]
#         tabla[sec_digit] = len(tabla) - sec_digit
#         tabla[sec_digit] = mark_x
#         game1 = False

# # Functie marcare 0
# def push_o(tabla, mark_o, useri_dict, userul_o):
#     """Jocul pt 0"""
#     o_u = useri_dict["user_0"][1]
#     o_u = o_u.center(30, "*")
#     tabel_nr = ["1", "2", "3"]
#     tabel_lit = ["a", "b", "c"]
#     game1 = True
#     cuvant1 = True
#     print(userul_o)
#     print(o_u)
#     while game1:
#         if cuvant1 == True:
#             oul = input(">>> ")
#         if oul[0] == "" or oul[0] == " " or oul[0] not in tabel_nr:
#             oul = input(f" 0 Hey! {useri_dict['user_0'][0]}, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ")
#             cuvant1 = False
#             continue
#         elif oul[1] == "" or oul[1] == " " or oul[1] not in tabel_lit:
#             oul = input(f" 0 Hey! {useri_dict['user_0'][0]}, vezi ca ai gresit! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ")
#             cuvant1 = False
#             continue
#         while oul in list_incercari:
#             oul = input(f"0  Hey! {useri_dict['user_0'][0]}, vezi ca ai gresit (coordonate)! Introdu' coordonatele (Se incepe cu randurile, respectiv 1, 2 sau 3 si apoi coloanele - A, B sau C >>> ").lower()
#         list_incercari.append(oul)
#         cuvant1 = True
#         first_digit = int(oul[0])
#         if oul[1] == "a":
#             sec_digit = 0
#         elif oul[1] == "b":
#             sec_digit = 1
#         elif oul[1] == "c":
#             sec_digit = 2
#         tabla = tabla[first_digit - 1]
#         tabla[sec_digit] = len(tabla) - sec_digit
#         tabla[sec_digit] = mark_o
#         game1 = False
            

# # Functie jocul....Greu ii futa-l drequ'
# def joc(tabla,mark_x,mark_o, prim_x, prim_o, empty_box, useri_dict, userul_x, userul_o):
#     """Castigator sau remiza....Vai futa-l drequ'"""
#     incercari_x = 0
#     incercari_o = 0
#     prima_etapa = True
   

# # Afisare castigator sau remiza
# def castigatori(useri_dict, userul_x, userul_o):
#     os.system('cls')
#     print(f"3 > {rand3}\n2 > {rand2}\n1 > {rand1}\n       ^      ^      ^\n       A      B      C")
#     if useri_dict["user_X"][2] > useri_dict["user_0"][2]:
#         if useri_dict["user_X"][2] == 1:
#             print(userul_x)
#             print(useri_dict["user_X"][0] + " " + "a castigat! si are " + str(useri_dict["user_X"][2]) + " " + "punct")
#         else:
#             print(userul_x)
#             print(useri_dict["user_X"][0] + " " + "a castigat! si are " + str(useri_dict["user_X"][2]) + " " + "puncte")
#     elif useri_dict["user_0"][2] > useri_dict["user_X"][2]:
#         if useri_dict["user_0"][2] == 1:
#             print(userul_o)
#             print(useri_dict["user_0"][0] + " " + "a castigat! si are " + str(useri_dict["user_0"][2]) + " " + "punct")
#         else:
#             print(userul_o)
#             print(useri_dict["user_0"][0] + " " + "a castigat! si are " + str(useri_dict["user_0"][2]) + " " + "puncte")
#     else:
#         remiza = "Remiza"
#         remiza = remiza.center(30, "*")
#         print(remiza)
#         print("scor: " + str(useri_dict["user_X"][2]) + " >>> " + useri_dict["user_X"][0])
#         print("scor: " + str(useri_dict["user_0"][2]) + " >>> " + useri_dict["user_0"][0])
        
        
    


