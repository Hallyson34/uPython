t = int(input())
i=1
anos=0
val=True
while i<=t:
    PA,PB,CA,CB=map(float,input().split())
    PA=int(PA)
    PB=int(PB)
    while PA<=(PB):
        PA= PA + (CA/100)*PA
        PA=int(PA)
        PB= PB + (CB/100)*PB
        PB=int(PB)
        anos+=1
        if anos>100:
            print("Mais de 1 seculo.")
            val=False
            PA=PB+1
        else:
            val=True
    if val:
        print(f"{anos} anos.")
    anos=0
    i+=1
