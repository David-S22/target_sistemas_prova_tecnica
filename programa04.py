# DECLARAÇÃO DE DICIONÁRIO
dicio_fat_mensal = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48,
                    'Outros': 19849.53}  # Responsável por armazenar o faturamento mensal estadual da distribuidora.


# PROGRAMA PRINCIPAL
total_mensal = (dicio_fat_mensal['SP'] + dicio_fat_mensal['RJ'] + dicio_fat_mensal['MG'] + dicio_fat_mensal['ES'] +
                dicio_fat_mensal['Outros'])  # Somatório de todo o faturamento mensal dos estados.


# CÁLCULO DO PERCENTUAL DE REPRESENTAÇÃO POR ESTADO + SAÍDA DE DADOS
print('=' * 40)
print('Percentual de representação dos estados'.upper())
print('-' * 40)
print(f'SP: {((dicio_fat_mensal['SP'] * 100) / total_mensal):.2f}%')
print(f'RJ: {((dicio_fat_mensal['RJ'] * 100) / total_mensal):.2f}%')
print(f'MG: {((dicio_fat_mensal['MG'] * 100) / total_mensal):.2f}%')
print(f'ES: {((dicio_fat_mensal['ES'] * 100) / total_mensal):.2f}%')
print(f'Outros: {((dicio_fat_mensal['Outros'] * 100) / total_mensal):.2f}%')
print('')
print(f'Valor total mensal: R${total_mensal:,}')
print('=' * 40)
