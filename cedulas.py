#notas de 100/50/20/10/5/2/1
valor1 = input("")
valor = int(valor1)
qnt100 = valor//100
valor = valor-qnt100*100
qnt50 = valor//50
valor = valor-qnt50*50
qnt20 = valor//20
valor = valor-qnt20*20
qnt10 = valor//10
valor = valor-qnt10*10
qnt5 = valor//5
valor = valor-qnt5*5
qnt2 = valor//2
valor = valor-qnt2*2
qnt1 = valor//1
print(valor1)
print(f"{qnt100} nota(s) de R$ 100,00")
print(f"{qnt50} nota(s) de R$ 50,00")
print(f"{qnt20} nota(s) de R$ 20,00")
print(f"{qnt10} nota(s) de R$ 10,00")
print(f"{qnt5} nota(s) de R$ 5,00")
print(f"{qnt2} nota(s) de R$ 2,00")
print(f"{qnt1} nota(s) de R$ 1,00")