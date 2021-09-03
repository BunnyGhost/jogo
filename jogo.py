from random import randint

n = int(randint(0, 10))

p=0

t = 0

while p != n:

    p = int(input('Digite um numero: '))

    t+= 1

    if p == n:

        print('Acertou placar {}'.format(t))

    elif p <n:

        print('Digite um numero maior: ')

    else:

        print('Digite um numero menor: ')

        print('Fim do jogo!')
