diccionario_ejemplo={'llave':'valor'}
diccionario={'1':'uno','2':'dos','3':'tres'}
# print(diccionario.keys())
# print(diccionario.values())
# print(diccionario.items())

diccionario['4']='cuatro'
print(diccionario)
diccionario['0']='none'
print(diccionario)
diccionario['0']='cer'
print(diccionario)
diccionario.update({'0':'cero'})
print(diccionario)