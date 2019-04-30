def palabramaslarga (lista):
    palabra = ""
    largo = 0
    for x in lista:
       if (len(x)>largo):
             palabra= x
             largo = len (x)
    return palabra
def menu ():
    print ("1) Calcular palabra mas larga")
    print ("")
lista = []
menu ()
op = input ("ingrese su opcion")

if op == "1":
    largo = int(input("ingrese largo de la lista"))
    for i in range (largo):
        lista.append (input("ingrese palabra"))
    print ("la palabra mas larga es: ",palabramaslarga (lista))
for i in lista:
    invertido = i[::-1]
    print (invertido)
