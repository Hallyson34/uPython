import random
i=0
n = random.randint(0,10)
while i!=n:
    i = int(input("Digite um numero: "))
    if i==n:
        print("Parabens! Voce acertou!!!")
    else:
        print("Voce errou.Tente novamente")
        i=0
print("Bye.")