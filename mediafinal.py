i=1
n=1
media=1
mediaf=0
soma=0
while i<=4:
    while n<=3:
        nota = float(input("Digite as notas do Bimestre: "))
        soma=nota+soma
        n+=1
    media=soma/3
    mediaf+=media
    print(f"Media {i}º Bimestre: {media:.1f}")
    n=1
    soma=0
    i+=1
print(f"Media final: {mediaf/4:.1f}")