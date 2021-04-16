I,Q = map(int,input().split())
if I==1:
    print(f"Total: R$ {Q*4:.2F}")
elif I==2:
    print(f"Total: R$ {Q*4.5:.2F}")
elif I==3:
    print(f"Total: R$ {Q*5:.2f}")
elif I==4:
    print(f"Total: R$ {Q*2:.2f}")
else:
    print(f"Total: R$ {Q*1.5:.2f}")