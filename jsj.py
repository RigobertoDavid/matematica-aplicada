import time
time.sleep (2)
print("Bienvenido a matematica aplicada...")
time.sleep (3)

while True:
    try:
        numero = int(input("Por favor ingrese un número:"))
        break
    except ValueError:
        print("Upsi! Ese no es un número válido, inténtelo de nuevo...")

numero = float(input("Ingrese un numero: "))
print(numero)
if numero<0:
    print("El número ingresado es negativo.")
elif numero==0:
    print("El número ingresado es cero.")
else:
    print("El número ingresado es positivo.")


