# 3- Leitura de Arquivo CSV  
# Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

# * Solicite ao usuário o nome do arquivo CSV a ser lido.  
# * Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
# * Exiba cada linha completa como uma lista.  
# * Trate erros como arquivo inexistente ou problemas na leitura.

# Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.

# ---

import csv
import sys

def main():
    nome_arquivo = input("Digite o nome do arquivo CSV para leitura: ")

    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)

            print(f"\n--- Conteúdo do arquivo '{nome_arquivo}' ---")
            for linha in leitor:
                print(linha)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        sys.exit(1)
    except csv.Error as e:
        print(f"Erro de leitura do arquivo CSV: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)

main()

