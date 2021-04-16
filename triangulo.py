#a=3 b=4 c=6
a, b, c = map(float, input().split())
if a==0 or b==0 or c==0:
    print(f"Area = {(a+b)*c/2:.1f}")
else:
    if a<c or a<b:
        if b<c and a+b>c:
            print(f"Perimetro = {a+b+c:.1f}")
        elif c<b and c+a>b:
            print(f"Perimetro = {a+b+c:.1f}")
        else:
           print(f"Area = {c*(a+b)/2:.1f}")
    else:
        if b<c or c<b and b+c>a:
            print(f"Perimetro = {a+b+c:.1f}")
        else:
            print(f"Area = {c*(a+b)/2:.1f}")
    