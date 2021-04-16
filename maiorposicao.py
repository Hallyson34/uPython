i=1
pos=0
num=0
n=1
while i<=100:
    n = int(input())
    if n>num:
        pos=i
        num=n
    i+=1
if n>num:
    print(f"{n}\n{pos}")
else:
    print(f"{num}\n{pos}")