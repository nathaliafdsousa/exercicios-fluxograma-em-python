V = 10 * [0]
i = 0
while i < 10:
    num = int(input('Digite um número positivo: '))
    V[i] = num
    i += 1
j = 0
while j < 10:
    if j% 2 == 0:
        print(V[j])
    j +=1

