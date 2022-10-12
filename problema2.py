from random import randint as rand
bile=["Alba","Neagra"]
n=int(input("Dati numarul de cate ori vom extrage bile: "))
albe=0
negre=0
bila=0
for i in range(0,n):
    bila=rand(1,2)
    print("Bila: ",bile[bila-1])
    if(bila==1):
        albe+=1
    else:
        negre+=1
print("Albe:",albe,"\nNegre:",negre)