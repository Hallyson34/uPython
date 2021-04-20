x = float(input())
k = int(input())
valor= 0.0
val=True
for i in range(0,k+1,2):
    fat=1
    for j in range(1,i+1):
        fat=fat*j
    if val:
        valor=valor +(x**i/fat)
        val=False
    else:
        valor=valor - (x**i/fat)
        val=True
print(f"{valor:.4f}")
