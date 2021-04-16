n = int(input())
crescente=True
numero1=int(input())
n-=1
while n>0:
    numero2=int(input())
    if numero2<numero1:
        crescente=False
    numero1 = numero2
    n-=1
if crescente:
    print("Sim")
else:
    print("nao")