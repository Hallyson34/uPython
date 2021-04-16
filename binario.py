#ler binario e mostrar valor em decimal.  
binario = int(input())
resto=0
soma=0
pot=0
while binario != 0:
    if binario%10==0:
        resto=0
        binario = binario//10
        soma=soma+resto
    else:
        resto= 1*2**pot
        soma=soma+resto
        binario = binario//10
    pot+=1
print(soma)