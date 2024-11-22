soma = 0
cont = 0
while cont < 50:
    peso = float(input('DIgite o seu peso: '))
    while peso < 0:
        peso = float(input('ERRO! digite seu peso novamente: '))
    soma = soma + peso
    cont +=1
media = soma / 50
print(media)
