import Generadores 

def pregunta():
    print("Hola buen dia! BIENVENID@ Elige aqui que tramite vienes a realizar hoy")
    
    while True:
        print("[P]-Perfumeria\n[F]-Farmacia\n[C]-Cosmeticos")
        try:
            turno= input("Escriba la letra que corresponda con su tramite:  ").upper()
            ["F","C","P"].index(turno)
        except ValueError:
            print("Esa opcion no existe o no es valida")
            
        else:
            break
        
    Generadores.decorador(turno)
    
def Inicio():
    print("Desea otro turno?")
    
    while True:
        pregunta()
        try:
            otro_turno= input("Desea otro turno? SI O NO:   ").upper()
            ["SI","NO"].index(otro_turno)
        except ValueError:
            print("Esa opcion no existe o no es valida") 
        else:
            if otro_turno == "NO":
                print("Gracias por usar este servicio")
                break
            
Inicio()
    


            
        
