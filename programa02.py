# DECLARAÇÃO DE VARIÁVEIS E LISTAS
lista_fibonacci = []  # Responsável por armazenar os valores gerados da sequência de Fibonacci.
soma = 0  # Armazena o resultado da soma dos dois valores que antecedem o próximo número da sequência de Fibonacci.
i = -1  # Variável de controle da estrutura de repetição while.
x = 0  # 1°valor fixo da sequência de Fibonacci.
y = 1  # 2°valor fixo da sequência de Fibonacci.


# FUNÇÕES
def verificar_user_number(numero):
    """
    Essa função possui a finalidade de verificar se o valor informado pelo usuário existe na sequência de Fibonacci.
    :return: Retorna uma mensagem informando se o valor que o usuário informou está contido ou não na sequência de
    Fibonacci.
    """

    for b in range(0, len(lista_fibonacci), 1):
        if lista_fibonacci[b] == numero:  # Compara o valor inserido pelo usuário com cada item da lista Fibonacci.
            return f'\nO número {numero} pertence a sequência de Fibonacci!'
    return f'\nInfelizmente, o número {numero} não pertence a sequência de Fibonacci.'


# PROGRAMA PRINCIPAL
lista_fibonacci.append(x)  # Inserção do 1°valor fixo da sequência de Fibonacci a lista Fibonacci.
lista_fibonacci.append(y)  # Inserção do 2°valor fixo da sequência de Fibonacci a lista Fibonacci.


# ENTRADA DE DADOS
while True:
    try:
        user_number = int(input('Digite um número inteiro: '))  # Entrada de valor númerico inteiro pelo usuário.
        if user_number >= 0:  # Tratamento de entrada de números inválidos.
            break
        else:
            print('Número inválido. Por favor, tente novamente.')
    except ValueError:  # Tratamento de entrada de valores inválidos.
        print('Valor inválido.')


# CÁLCULO DA SEQUÊNCIA DE FIBONACCI
print('')
print('-' * 20)
print('Sequência de Fibonnacci')
print(f'{x}, {y}', end='')  # Impressão dos dois valores fixos da sequência de Fibonacci.

while soma < user_number:
    i += 1
    soma = x + y  # Soma dos dois valores que antecedem o próximo número da sequência de Fibonacci.

    if i % 2 == 0:  # Variável de Controle Par.
        x = soma
    else:  # Variável de Controle Ímpar.
        y = soma

    lista_fibonacci.append(soma)  # Inserção dos novos valores da sequência de Fibonacci a Lista Fibonacci.
    print(f', {soma}', end='')  # Impressão do valor contido na variável "soma".
print('\n' + '-' * 20)


# SAÍDA DE DADOS
print(verificar_user_number(user_number))
