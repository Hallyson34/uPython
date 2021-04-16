n = int(input())
i=1
somapar=0
somaimp=0
while i<=n:
    m = int(input())
    if m%2==0:
        somapar = somapar+m
    else:
        somaimp = somaimp+m
    i+=1
print(f"Pares: {somapar}")
print(f"Impares: {somaimp}")