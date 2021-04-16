dec = int(input())
mod=0
soma=0
i=0
while dec!=0:
    mod=dec%2
    soma+=mod*10**i
    i+=1
    dec=dec//2
print(soma)