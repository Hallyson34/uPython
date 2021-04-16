tam, queijo, borda = input().split()
total = 0.0
if tam=="P":
    total=15
    if queijo=="S":
        total+=2.5
    if borda=="S":
        total+=5
        print(f"Total: R$ {total:.2f}")
    else:
        print(f"Total: R$ {total:.2f}")
elif tam=="M":
    total=18.5
    if queijo=="S":
        total+=4
    if borda=="S":
        total+=5
        print(f"Total: R$ {total:.2f}")
    else:
        print(f"Total: R$ {total:.2f}")
else:
    total=23
    if queijo=="S":
        total+=4
    if borda=="S":
        total+=5
        print(f"Total: R$ {total:.2f}")
    else:
        print(f"Total: R$ {total:.2f}")
