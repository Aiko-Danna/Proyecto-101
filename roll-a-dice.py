import random;

response = "y"

while response == "y":
    no = random.randint(1,6)
    
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        response=str(input("presiona y para girar otra vez y n para salir: "))
    
    if no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
        response=str(input("presiona y para girar otra vez y n para salir: "))
    
    if no == 3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")
        response=str(input("presiona y para girar otra vez y n para salir: "))
    
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        response=str(input("presiona y para girar otra vez y n para salir: "))
    
    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        response=str(input("presiona y para girar otra vez y n para salir: "))
    
    if no == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
        response=str(input("presiona y para girar otra vez y n para salir: "))

    