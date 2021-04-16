A,B,C = map(float, input().split())
D = B**2-4.0*A*C
if D<0:
    print("Impossivel calcular")
elif A==0: 
    print("Impossivel calcular")
else:
    R1 = (-B+(D**0.5))/(2*A)
    R2 = (-B-(D**0.5))/(2*A)
    print(f"R1 = {R1:.5f}\nR2 = {R2:.5f}")