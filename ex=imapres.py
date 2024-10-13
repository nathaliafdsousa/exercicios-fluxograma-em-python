i = 1
while i <= 99:
    if i % 2 != 0:
        print(f'O número ímpar é {i}')
    i += 2  # Corrigido para incrementar 'i'

print(f'Os números ímpares de 1 a 99 são: {list(range(1, 100, 2))}')