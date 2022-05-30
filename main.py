
from useri import *
from jocul import *
import jocul



final_game = True
raspuns = ""
while final_game == True:
    if start_signup == True and raspuns == "":
        joc(tabla,mark_x,mark_o, prim_x, prim_o, empty_box, useri_dict, userul_x, userul_o)
        castigatori(useri_dict, userul_x, userul_o)
        print("1. Doresti sa joci in continuare?. Scrie \"1\" >>> \n2. Doresti sa resetezi jocul si sa innregistrezi playeri noi?. Scrie \"2\" >>> \n3. Doresti sa iesi din joc?. Scrie \"da\", \"3\" sau \"x\" >>> ")
        raspuns = input("Raspunde aici >>> ")
    elif raspuns == "1":
        start_signup = False
        useri_dict["user_X"][3] = []
        useri_dict["user_0"][3] = []
        joc(tabla,mark_x,mark_o, prim_x, prim_o, empty_box, useri_dict, userul_x, userul_o)
        castigatori(useri_dict, userul_x, userul_o)
        print("1. Doresti sa joci in continuare?. Scrie \"1\" >>> \n2. Doresti sa resetezi jocul si sa innregistrezi playeri noi?. Scrie \"2\" >>> \n3. Doresti sa iesi din joc?. Scrie \"da\", \"3\" sau \"x\" >>> ")
        raspuns = input("Raspunde aici >>> ")

         