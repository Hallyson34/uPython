A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
par = 0
impar = 0
pos = 0
neg = 0
if A%2==0:
    par = par+1
    if A>0:
        pos = pos+1 
    else:
        if A!=0:
            neg = neg+1
else:
        impar = impar+1
        if A>0:
            pos = pos+1 
        else:
                neg = neg+1
#----------------------------------------------
if B%2==0:
    par = par+1
    if B>0:
        pos = pos+1 
    else:
        if B!=0:
            neg = neg+1
else:
        impar = impar+1
        if B>0:
            pos = pos+1 
        else:
                neg = neg+1
#----------------------------------------------
if C%2==0:
    par = par+1
    if C>0:
        pos = pos+1 
    else:
        if C!=0:
            neg = neg+1
else:
        impar = impar+1
        if C>0:
            pos = pos+1 
        else:
                neg = neg+1
#----------------------------------------------
if D%2==0:
    par = par+1
    if D>0:
        pos = pos+1 
    else:
        if D!=0:
            neg = neg+1
else:
        impar = impar+1
        if D>0:
            pos = pos+1 
        else:
                neg = neg+1
#----------------------------------------------
if E%2==0:
    par = par+1
    if E>0:
        pos = pos+1 
    else:
        if E!=0:
            neg = neg+1
else:
        impar = impar+1
        if E>0:
            pos = pos+1 
        else:
                neg = neg+1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")