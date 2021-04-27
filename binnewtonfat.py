n = int(input())
k = int(input())
fatn=1
fatk=1
fatnk=1
for x in range(1,n+1):
    fatn=fatn*x
for y in range(1,k+1):
    fatk=fatk*y
for z in range(1,(n-k)+1):
    fatnk=fatnk*z
print(fatn//(fatk*fatnk))