N = int(input())
i=1
div=0
while i<=N:
    X = int(input())
    for j in range(1,X):
        if X%j==0:
            div=div+j
    if div==X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
    div=0
    i+=1