a, b, c = map(int, input().split())

if c > a and c > b:
    x = c
    if a > b:
        y = a
        z = b
    else:
        y = b
        z = a
if b > a and b > c:
    x = b
    if a > c:
        y = a
        z = c
    else:
        y = c
        z = a
if a > b and a > c:
    x = a
    if b > c:
        y = b
        z = c
    else:
        y = c
        z = b
else:
    print(c)
    if b<a:
        print(f"{b}\n{a}")
    else:
        print(f"{a}\n{b}")
print(f"\n{a}\n{b}\n{c}")

