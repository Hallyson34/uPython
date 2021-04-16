i=1
n=1
m=1
soma=0
validacao=True
while validacao:
    m,n = map(int, input().split())
    if m>0 and n>0: 
        while m<n: 
            print(f"{m}",end=" ")
            soma += m
            m+=1
        while n<=m:
            print(f"{n}",end=" ")
            soma += n
            n+=1
        print("",end=f"Sum={soma}\n")
        soma=0
    else:
        validacao = False