# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = input('\nDigite a expressão matemática: ')
pa = 0
pf = 0
for a in list(exp):
    if a == '(':
        pa += 1
    if a == ')':
        pf += 1
if pa == pf:
    print('Expessão válida!')
else:
    print('Expressão inválida!')