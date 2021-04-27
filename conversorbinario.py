#bin - decimal
binario = int(input())
soma = 0
pot = 0
while binario != 0:
    if binario % 10 == 1:
        binario = binario // 10
        soma = soma + 1*2**pot
    else:
        binario = binario // 10
    pot+=1
print(soma)    
#decimal - bin
decimal = int(input())
soma = 0
pot = 0
while decimal != 0:
    if decimal % 2 == 1:
        soma = soma + 1*10**pot
        decimal = decimal // 2
    else:
        decimal = decimal // 2
    pot+=1
print(soma)

