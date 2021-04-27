m = int(input())
res1=0
k=0
res2=0
fatn=1
fatk=1
fatnk=1
for n in range(0,m):
    for k in range(0,n+1):
        fatn=1
        fatk=1
        fatnk=1
        for x in range(1,n+1):
            fatn=fatn*x
        for y in range(1,k+1):
            fatk=fatk*y
        for z in range(1,(n-k)+1):
            fatnk=fatnk*z
        if k==n:
            print(f"{fatn//(fatk*fatnk)}", end=" \n")
        else:
            print(f"{fatn//(fatk*fatnk)}", end=" ")
        
    