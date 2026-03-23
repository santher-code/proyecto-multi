class receta:
    def __init__(self, nombrerc,ingredientes,cantidad):
        self.nombre = nombrerc
        self.ingredientes = ingredientes 
        self.cantidad =cantidad
        
   
class usuario:
    def __init__(self, nombreu, edad, correo):
        self.nombre = nombreu
        self.edad = edad
        self.correo = correo  
        self.peso= 0
        self.contraseña = ""
        
class plan_alimenticio:
    def __init__(self, nombrep, recetas):
        self.nombre = nombrep
        self.recetas = recetas

class ingredientes:
    def __init__(self, nombrei, cantidadi):
        self.nombre = nombrei
        self.cantidad = cantidadi
        self.calorias = 0
        self.proteinas =0
