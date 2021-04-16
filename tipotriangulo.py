A, B, C = map(float, input().split())
if B>A and B>C:
    M = B
    B = A
    A = M
else:
    if C>B and C>A:
        M = C
        C = A
        A = M
if A<=0 or B<=0 or C<=0 or A>=B+C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2==B**2+C**2:
        print("TRIANGULO RETANGULO")
    elif A**2>B**2+C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2<B**2+C**2:
        print("TRIANGULO ACUTANGULO")
if A==B==C:
    print("TRIANGULO EQUILATERO")
elif A==B or B==C or C==A:
    print("TRIANGULO ISOSCELES")