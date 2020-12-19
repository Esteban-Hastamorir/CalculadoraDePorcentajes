
def calcularElPorcentaje (cifra, porcentaje):
    print (cifra*(porcentaje/100))
def descuento (cifra, porcentaje):
    print(cifra-(cifra*(porcentaje/100))) 

print ("Que desea hacer?")
decision = int (input ("[1] Calcular el porcentaje de una cifra\n[2] Descuento\n"))
if (decision == 1):
    cifra = int(input("Ingrese la cifra\n"))
    porcentaje = float(input("Ingrese el porcentaje\n"))
    calcularElPorcentaje (cifra, porcentaje)

elif(decision == 2):
    cifra = int(input("Ingrese la cifra\n"))
    porcentaje = float(input("Ingrese el porcentaje a restar\n"))
    descuento (cifra, porcentaje)
else:
    print("Error")

