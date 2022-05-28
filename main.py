from useri import *
from jocul import *



final_game = True
raspuns = ""
while final_game:
    if start_signup == True:
        joc(tabla,mark_x,mark_o, prim_x, prim_o, empty_box, useri_dict, userul_x, userul_o)
        castigatori(useri_dict, userul_x, userul_o)
        print("1. Doresti sa joci in continuare?. Scrie \"1\" >>> \n2. Doresti sa resetezi jocul si sa innregistrezi playeri noi?. Scrie \"2\" >>> \n3. Doresti sa iesi din joc?. Scrie \"da\", \"3\" sau \"x\" >>> ")
        raspuns = input("Raspunde aici >>> ")
