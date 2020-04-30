# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c+1}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}... ', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}... ', end='')
print()