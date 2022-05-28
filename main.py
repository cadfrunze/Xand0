from useri import *
from jocul import *

final_game = True
raspuns = ""
while final_game:
    if start_signup == True:
        joc(tabla,mark_x,mark_o, prim_x, prim_o, empty_box, useri_dict, userul_x, userul_o)
        raspuns = input("""1. Doresti sa joci in continuare?. Scrie \"1\" >>> 
        2. Doresti sa innregistrezi playeri noi?. Scrie \"2\" >>> 
        3. Doresti sa iesi din joc?. Scrie \"da\", \"3\" sau \"x\" >>> """)
