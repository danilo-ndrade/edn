
# 2- Escrita de Arquivo CSV  
# Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

# * Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
# * Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
# * Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
# * Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
# * Trate possíveis erros de escrita de arquivo.

# Dica: Use `csv.writer()` para escrever os dados linha por linha.

# ---

import csv
import sys

def main():

    dados_pessoas = [
        ['Alice', 30, 'São Paulo'],
        ['Bruno', 25, 'Rio de Janeiro'],
        ['Carlos', 45, 'Belo Horizonte']
    ]

    cabecalhos = ['nome', 'idade', 'cidade']

    nome_arquivo = input("Digite o nome do arquivo CSV para salvar os dados: ")

    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:

            writer = csv.writer(arquivo_csv)

            writer.writerow(cabecalhos)

            writer.writerows(dados_pessoas)

        print(f"Sucesso! Os dados foram salvos em '{nome_arquivo}'.")

    except IOError as e:
        print(f"Erro de E/S ao escrever no arquivo: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)

main()

