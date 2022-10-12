from random import randint as r
n=int(input("Dati numarul de bile care trebuie sa fie extrase: "))
numar=0
max=0
for i in range(0,n):
    numar=r(1,20)
    print(numar)
    if(numar>max):
        max=numar
print("Cel mai mare: ",max)
