decimal=int(input())
i=0
n=0
pot=3
while i<=(decimal//2):
    if i%2==0 or i==(decimal//2)-1:
        n+=10
    if i%4==0 and i!=0:
            n=(10**pot)
            pot+=1
    if (i%2)!=0 and i<(decimal//2):
            n+=90
    i+=1
if decimal%2==0:
    print(n)
else:
    print(n+1)