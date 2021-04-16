n = int(input())
i=1
soma=0
while i<=n:
    x,y = map(int,input().split())
    if x%2==0:
        for a in range(x+1,x+y*2,2):
            soma= soma+a
    else:
        for b in range(x,x+y*2,2):
            soma = soma+b
    print(soma)
    soma=0
    i+=1
