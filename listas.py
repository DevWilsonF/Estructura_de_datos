lista_vacia=[]
lista=['esto es una lista']#esta es una lista de un solo elemento
lista1=[1,2,3,True,'elemento de la lista']#este es una lista de 5 elementos
listaConcatenada=lista+lista1
# print(listaConcatenada)
listaDeLista=[lista,lista1]

# print(lista_vacia)
# print(lista)
# print(lista1)
# print(listaDeLista)
lista= ['uno','dos','tres','cuatro']
len(lista)
# print(lista[2])
if 'uno' in lista:
    pass
    # print ('si esta')
# print('ciclo para')
for i in lista:
    # print (i)
    pass
i=0
# print('ciclo mientras')
while i < len(lista):
    # print (lista[i])
    i+=1
    
# print(len(lista))
# print(lista)
lista.append('cinco')
lista.insert(0,'cero')
# print(lista)
lista.remove('cinco')
# print(lista)

lista=[1,2,3,4,1,1,2,2,4,4,4,5,8,3,1,]
# print(lista.count(1))
# print(lista.index(4))
# print('min de la lista: ',min(lista),' el max de la lista: ',max(lista))
lista.sort()
# print(lista)
lista.sort(reverse=True)
# print(lista)

lista= ['uno','dos','tres','cuatro']
print(lista)
elemento_eliminado= lista.pop(0)
print(lista)
print(elemento_eliminado)