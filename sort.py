A, B, C = map(int, input().split())
if A<B and A<C:
    print(A)
    if B<C:
        print(f"{B}\n{C}")
    else:
        print(f"{C}\n{B}")
elif B<A and B<C:
    print(B)
    if A<C:
        print(f"{A}\n{C}")
    else:
        print(f"{C}\n{A}")
else:
    print(C)
    if B<A:
        print(f"{B}\n{A}")
    else:
        print(f"{A}\n{B}")
print(f"\n{A}\n{B}\n{C}")