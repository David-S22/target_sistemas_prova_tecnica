# DECLARAÇÃO DE LISTAS E VARIÁVEIS
lista_valores = []  # Possui por objetivo armazenar todos os valores de faturamento obtidos no mês.
global media_fat_mes  # Média do faturamento mensal.


# DADOS DO FATURAMENTO DIÁRIO NO MÊS
lista_fat_diario = [
        {
            "dia": 1,
            "valor": 22174.1664
        },
        {
            "dia": 2,
            "valor": 24537.6698
        },
        {
            "dia": 3,
            "valor": 26139.6134
        },
        {
            "dia": 4,
            "valor": 0.0
        },
        {
            "dia": 5,
            "valor": 0.0
        },
        {
            "dia": 6,
            "valor": 26742.6612
        },
        {
            "dia": 7,
            "valor": 0.0
        },
        {
            "dia": 8,
            "valor": 42889.2258
        },
        {
            "dia": 9,
            "valor": 46251.174
        },
        {
            "dia": 10,
            "valor": 11191.4722
        },
        {
            "dia": 11,
            "valor": 0.0
        },
        {
            "dia": 12,
            "valor": 0.0
        },
        {
            "dia": 13,
            "valor": 3847.4823
        },
        {
            "dia": 14,
            "valor": 373.7838
        },
        {
            "dia": 15,
            "valor": 2659.7563
        },
        {
            "dia": 16,
            "valor": 48924.2448
        },
        {
            "dia": 17,
            "valor": 18419.2614
        },
        {
            "dia": 18,
            "valor": 0.0
        },
        {
            "dia": 19,
            "valor": 0.0
        },
        {
            "dia": 20,
            "valor": 35240.1826
        },
        {
            "dia": 21,
            "valor": 43829.1667
        },
        {
            "dia": 22,
            "valor": 18235.6852
        },
        {
            "dia": 23,
            "valor": 4355.0662
        },
        {
            "dia": 24,
            "valor": 13327.1025
        },
        {
            "dia": 25,
            "valor": 0.0
        },
        {
            "dia": 26,
            "valor": 0.0
        },
        {
            "dia": 27,
            "valor": 25681.8318
        },
        {
            "dia": 28,
            "valor": 1718.1221
        },
        {
            "dia": 29,
            "valor": 13220.495
        },
        {
            "dia": 30,
            "valor": 8414.61
        }
]


# FUNÇÕES
def titulo(mensagem):
    """
    Cria e centraliza um título para a interface de visualização do conteúdo.
    :param mensagem: Contém o título a ser apresentado.
    :return: Essa função não possui retorno de valor.
    """

    tam_msg = len(mensagem)  # Armazena a quantidade total de caracteres da mensagem.
    tam_lado = int((100 - tam_msg) / 2)  # Quantidade de espaços de um dos lados horizontais da mensagem de modo
    # que esta fique centralizada no momento da visualização do conteúdo.

    print('=' * 100)
    print(' ' * tam_lado + mensagem + ' ' * tam_lado)
    print('-' * 100)


def calc_menor_fat_mes(lista):
    """
    Realiza o cálculo do menor faturamento do mês.
    :return: Retorna uma mensagem apresentando o menor valor de faturamento do mês.
    """
    return f'Menor valor de faturamento do mês: R${min(lista):,.2f}'


def calc_maior_fat_mes(lista):
    """
    Realiza o cálculo do maior faturamento do mês.
    :return: Retorna uma mensagem apresentando o maior valor de faturamento do mês.
    """
    return f'Maior valor de faturamento do mês: R${max(lista):,.2f}'


def calc_media_mensal(lista):
    """
    Calcula a média mensal do faturamento no mês.
    :param lista: Recebe uma lista contendo os valores de faturamento do mês.
    :return: Essa função não retorna nenhum valor.
    """

    global media_fat_mes  # Média do faturamento do mês.
    soma = 0  # Variável local responsável por armazenar o somatório de todo o faturamento do mês.
    total_dias_fat = 0  # Total de dias em que houve faturamento diferente de zero.

    for valor in lista:
        if valor != 0:
            soma += valor
            total_dias_fat += 1

    media_fat_mes = soma / total_dias_fat  # Cálculo da média mensal do faturamento do mês.


def calc_fat_smm_dia(lista, media):
    """
    Calcula a quantidade de dias em que o faturamento diário foi superior a média mensal do mês atual.
    :return: Retorna a quantidade de dias em que o faturamento diário foi superior a média mensal.
    """

    fat_smm_dia = 0  # Responsável por armazenar a quantidade total de dias em que o faturamento diário foi superior à
    # média mensal.

    for item in lista:
        if item > media:
            fat_smm_dia += 1

    return fat_smm_dia


# PROGRAMA PRINCIPAL
for i in range(0, len(lista_fat_diario), 1):  # Estrutura de repetição que armazena o faturamento mensal na
    # lista valores.
    lista_valores.append(lista_fat_diario[i]['valor'])


# PROCESSAMENTO E SAÍDA DE DADOS
titulo('LEVANTAMENTO DO FATURAMENTO MENSAL')
print(calc_menor_fat_mes(lista_valores))  # Apresenta o menor faturamento do mês.
print(calc_maior_fat_mes(lista_valores))  # Apresenta o maior faturamento do mês.
calc_media_mensal(lista=lista_valores)
print(f'Média mensal de faturamento do mês: R${media_fat_mes:,.2f}')
print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: '
      f'{calc_fat_smm_dia(lista=lista_valores, media=media_fat_mes)} dia(s)')
print('=' * 100)
