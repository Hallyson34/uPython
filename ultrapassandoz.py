x = int(input())
y = int(input())
i=1
soma=x
while x>=y:
    y=int(input())
while soma<=y:
    soma=soma+(x+i)
    i+=1
print(i)