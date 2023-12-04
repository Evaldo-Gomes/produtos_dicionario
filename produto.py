#cadastro de produtos
#Apresentação
print('\n\t\t\t  --  Cadastro de Produtos  --')

#Estrutura do dicionário
produto = {
    'Produto': 'Nome do produto',
    'Preço': 0.0,
    'Quantidade': 0,
    'Total': 0.0
}

#Entrada
produto['Nome'] = input('Informe o nome do ítem: ')
produto['Preço'] = float(input('Informe o valor (R$): '))
produto['Quantidade'] = int(input('Informe a quantidade: '))

#Processamento
produto['Total'] = produto['Preço'] * produto['Quantidade']

#Saída
print(f'Ítem.....................{produto["Nome"]}')
print(f'Preço....................{produto["Preço"]}')
print(f'Quantidade.....................{produto["Quantidade"]}')
print(f'O produto {produto["Nome"]} em {produto["Quantidade"]} unidade(s) totaliza R${produto["Total"]}')