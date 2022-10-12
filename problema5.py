from random import randint
n=int(input("Dati lungimea fiecarui sir: "))
A=[]
B=[]
C=[]
for i in range(0,n):
    A.append(randint(0,99))
    B.append(randint(1,999))
    C.append(0)
print(A)
print(B)
for i in range(0,len(A)):
    if(A[i]%2==0 and B[i]%2!=0):
        C[i]=A[i]-B[i]
    elif(A[i]%2!=0 and B[i]%2==0):
        C[i]=A[i]+B[i]
    else:
        C[i]=A[i]*B[i]
print(C)