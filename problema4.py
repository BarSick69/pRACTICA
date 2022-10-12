def cautare():
    nume=["ion","vladimir","vlad","alexei","maxim","rodion","liviu","loredana","tatiana","petru","vadim","serghei","maia","vasile"]
    n=int(input("Cati elevi doriti sa cautati? "))
    numele=""
    if(n<=len(nume)):
      for i in range(0,n):
        numele=input("Dati numele elevului:")
        if(numele.lower() in nume):
            print("Acest elev este in lista")
        else:
            print("Acest elev nu este in lista")
    else:
        print("Lista nu contine asa numar de elevi")
cautare()