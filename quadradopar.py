n = int(input())
i=2
while i<=n:
    par=n-(n-i)
    print(f"{par}^2 = {par**2}")
    i+=2
