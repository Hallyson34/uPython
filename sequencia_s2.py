s=0.0
dim=0
for i in range(1,40,2):
    s+=i/2**(dim)
    dim+=1
print(f"{s:.2f}")