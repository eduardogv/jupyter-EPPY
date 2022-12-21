class Empleado:
    empresa = "Google"  # dato compartido por todas las instancias
    
    def mostrar_empresa():    # Función de clase. Esto es un Comportamiento??
        print(f"Todos los empleados trabajan en {Empleado.empresa}")
    
    def __init__(self):
        self.salario = 1000  # dato de instancia
    
    def incrementar_salario(self, incremento):  # comportamiento compartido por todas las instancias
        self.salario += incremento

        
empleado_1 = Empleado()
empleado_2 = Empleado()

print(empleado_1.empresa)
print(empleado_2.empresa)
print(Empleado.empresa)

#empleado_1.mostrar_empresa()
#empleado_2.mostrar_empresa()
#Empleado.mostrar_empresa()

empleado_1.incrementar_salario(200)
#empleado_2.incrementar_salario(500)

print(empleado_1.salario)
#print(empleado_2.salario)
Empleado.mostrar_empresa()

class Figura_Geometrica:
    def __init__(self, tipo):
        self.tipo = tipo
        print (f'Esta figura es un {tipo}')
   
figurax = Figura_Geometrica('circulo')
