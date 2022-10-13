from gettext import find


cadena = "Hola mundo"
salto = '\n----------------------------\n'
imprimir = f"{cadena}{salto}salto de linea: \\n{salto}\ttabulacion: \\t{salto}comillas dobles \"\" : \\\" {salto}comillas simples '' \\' {salto} diagonal invertida \\ : \\\\"
# print(imprimir)
cadena= "Hola" +' '+ "Mundo"
cadena+=" Hola Mundo"
# print(f"{cadena}{salto}Para acceder a los elementos de la cadena es variable[] ejemplo cadena[2]: {cadena[2]}")

cadenaUno="cadena"
cadenaDos="codena"
cadenaTres="cadena"
resultado=f"Primer caso cadenaUno es mayor que cadenaDos = {cadenaUno>cadenaDos}\n"
resultado+=f"Segundo caso cadenaUno es menor que cadenaDos = {cadenaUno<cadenaDos}\n"
resultado+=f"Tercer caso cadenaUno es igual que cadenaDos = {cadenaUno==cadenaDos}\n"
resultado+=f"Cuarto caso cadenaUno es igual que cadenaTres = {cadenaUno==cadenaTres}"
# print(resultado)

cadenaCuatro="hola mundo"
condicion= 'h' in cadenaCuatro
# print(condicion)
# if condicion:
#     print('Si esta')
# else:
#     print('No esta') 

cadena="Esta es una cadena"
longitudCadena=len(cadena)
# print(f"cadena: '{cadena}' longitud: {longitudCadena}")

cadena = "Los vengadores estan aqui"
# print(cadena.count('e'))
# print(cadena.count('e',3,7))
# print(cadena.count('e',6,len(cadena)))

cadena = "Hola esta es una prueba de python para el metodo find y rfind en el cual nos permitira conoser su funcionalidad"
# print(cadena.find("el"),cadena.rfind('el'))

cadena = "Los vengadores estan aqui"
# print(cadena.lower())
# print(cadena.upper())
# print(cadena.capitalize())
# print(cadena.title())
# print(cadena.swapcase())

cadena = "-----++++---Los vengadores estan aqui-----+++-----"
# print(cadena.strip("-+"))
# print(cadena.rstrip("-+"))
# print(cadena.lstrip("-+"))
# cadena = "      Los vengadores estan aqui  "
# print(cadena)
# print(cadena.strip())

cadena="2022-10-07"
# print(cadena.split('-'))

cadena="Los vengadores estan aqui"
print(cadena)
print(cadena.replace('Los','Mis'))