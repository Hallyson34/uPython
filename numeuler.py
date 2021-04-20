#Professor fez/code runner
x = float(input())
n = int(input())
valor=0.0
for i in range(0,n+1):
    fat=1
    for j in range(1,i+1):
        fat=fat*j
    valor=valor + x**i/fat
print(f"{valor:.4f}")