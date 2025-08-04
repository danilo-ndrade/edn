# 4- Leitura e Escrita de Arquivo JSON  
# Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

# * Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
# * Solicite ao usuário o nome do arquivo JSON.  
# * Salve os dados no arquivo usando o módulo `json`.  
# * Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
# * Trate possíveis erros como ausência do arquivo ou problemas na escrita.

# Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.

# ---

import json
import sys

def main():
    dados_pessoa = {
        "nome": "João da Silva",
        "idade": 35,
        "cidade": "Salvador"
    }
    
    nome_arquivo = input("Digite o nome do arquivo JSON para salvar os dados: ")

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados_pessoa, arquivo_json, indent=4, ensure_ascii=False)
            
        print(f"Sucesso! Dados da pessoa foram salvos em '{nome_arquivo}'.")

    except IOError as e:
        print(f"Erro de E/S ao escrever no arquivo: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao salvar: {e}")
        sys.exit(1)
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_carregados = json.load(arquivo_json)
        
        print(f"\n--- Conteúdo lido do arquivo '{nome_arquivo}' ---")
        print(f"Nome: {dados_carregados['nome']}")
        print(f"Idade: {dados_carregados['idade']}")
        print(f"Cidade: {dados_carregados['cidade']}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado para leitura.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não contém um JSON válido.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler: {e}")
        sys.exit(1)

main()