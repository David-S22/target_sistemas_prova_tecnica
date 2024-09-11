# PROGRAMA PRINCIPAL
word = input('Escreva algo que desejar: ')  # Entrada de dado do usuário.
print('')

for i in range(len(word) - 1, -1, -1):  # Estrutura de repetição responsável por inverter a ordem da string.
    print(f'{word[i]} ', end='')

print('')
print(f'Total de caracteres: {len(word)} caracteres')  # Informa ao usuário a quantidade total de caracteres inseridos.
