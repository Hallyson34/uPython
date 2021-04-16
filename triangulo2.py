a,b,c = map(float,input().split())
if (b-c)< a <(b+c):
    print(f"Perimetro = {a+b+c:.1f}")
else:
    print(f"Area = {c*(a+b)/2:.1f}")