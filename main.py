from threading import Thread



###sortowanie bąbelkowe
lista=[]
final=[]
from random import randint
for x in range(0,5):
    lista.append(randint(0,100))
    print(lista[x],end=" ")
###sortowanie
def wyswietlenie(lista):
    for x in range(0,len(lista)):
        print(lista[x],end=" ")
def sortowanie(lista):
    wartosc=False
    while wartosc==False:
        ilosc=0
        for x in  range(0,len(lista)-1):
        
            if lista[x]>lista[x+1]:
                zmienna=lista[x]
                lista[x]=lista[x+1]
                lista[x+1]=zmienna
                ilosc+=1
            elif ilosc==0 and x == len(lista)-2:
                wartosc=True
            else:
                continue
    print()
    wyswietlenie(lista)
sortowanie(lista)
print()
test=[]
for x in range(0,5):
    test.append(randint(0,100))
    print(test[x],end=" ")
###sortowanie faster way 

def sortowanie_2(lista):
    wartosc=False
    while wartosc==False:
        wynik=0
        for x in range(0,len(lista)):
            while wynik==0:
                wynik=0
                for j in range(x,-1,-1):
                    if lista[j]<lista[j-1]:
                        zmienna=lista[j]
                        lista[j]=lista[j-1]
                        lista[j+1]=zmienna
                    elif lista[j]>lista[j-1]:
                        wynik+=1
                        break
                    else:
                        continue
            if x==len(lista)-1:
                wartosc=True
                break
        print()
        wyswietlenie(lista)

sortowanie_2(test)


