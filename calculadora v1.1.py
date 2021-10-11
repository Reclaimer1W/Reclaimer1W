print("Bienvenido a la calculadora v1.1")

primerCifra = input("Por favor digite una cifra: ")
try:
    primerCifra = int(primerCifra)
except:
    primerCifra = str()
if  primerCifra == str():
    print("No has ingresado un valor válido. Por favor, escribe sólo una cifra.")
    exit()

segundaCifra = input("Por favor digite una cifra: ")
try:
    segundaCifra = int(segundaCifra)
except:
    segundaCifra = str()
if  segundaCifra == str():
    print("No has ingresado un valor válido. Por favor, escribe sólo una cifra.")
    exit()

operacion = input("Ingrese una operación: \n Para sumar: +\n Para restar: -\n Para multiplicar: *\n Para dividir: /\n")
if operacion == "+":
    print("El resultado de la suma es: ", primerCifra + segundaCifra)
if operacion == "-":
    print("El resultado de la resta es: ", primerCifra - segundaCifra)
if operacion == "*":
    print("El resultado de la multiplicación es: ", primerCifra * segundaCifra)
if operacion == "/":
    print("El resultado de la división es: ", primerCifra / segundaCifra)