nota = 0.0
soma = 0.0
validacao = True
while validacao:
    nota = float(input())
    if nota<0 or nota>10:
        print("nota invalida")
    else:
        if soma == 0.0:
            soma=nota+1
        else:
            if soma>0:
                soma-=1
                soma+=nota
                print(f"media = {soma/2:.2f}")
                validacao = False


