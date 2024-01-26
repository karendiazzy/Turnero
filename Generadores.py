def Perfumeria():
    for num in range (1,500):
        yield f"P {num}"
        
def Farmacia():
    for num in range (1,500):
        yield f"F {num}"
        
def Cosmeticos():
    for num in range (1,500):
        yield f"C {num}"
        
P= Perfumeria()
F= Farmacia()
C= Cosmeticos()

def decorador(turnos):
    print("Su numero es:")
    if turnos == "P":
        print(next(P))
    elif turnos == "F":
        print(next(F))
    elif turnos == "C":
        print(next(C))
    print("Espere a ser atendid@")
        
        

