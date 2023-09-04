import random

print('Bem-vindo ao gerador de senhas')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*()_+=?'

number = input('Quantidade de senhas para gerar: ')
number = int(number)

print('\nAqui estão suas senhas: ')

for pwd in range(number):
    password = ''
    for c in range(len(chars)):
        password += random.choice(chars)
    print(password)
    print('\n')