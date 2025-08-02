# ---

# 3- Consulta de CEP  
# Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

# * Solicite ao usuário que digite um CEP (apenas números, sem traço).  
# * Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
# * Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
# * Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

# Dica: Use o módulo `requests` e trate exceções com `try/except`.

import requests

def main():

    cep = input("Digite o CEP: ")

    cep = cep.replace('-', '')

    try:
        res = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        print(f'Status da requisição: {res.status_code}')

        if res.json()['erro'] == "true":
            print("CEP inválido/não encontrado.")


        street = res.json()['logradouro']
        neighborhood = res.json()['bairro']
        city = res.json()['localidade']
        state = res.json()['estado']
        zipcode = res.json()['cep']
        
        print(f"{street}, {neighborhood} - {zipcode}, {city}, {state}")

    except requests.exceptions.RequestException as e:
        print(f"ERRO de requisição: {e}. Verifique sua conexão ou o URL.")
    except requests.exceptions.JSONDecodeError:
        print("ERRO: Resposta não é um JSON válido.")
    except KeyError as e:
        print(f"ERRO: Chave não encontrada na resposta JSON: {e}. A estrutura da resposta pode ter mudado.")
    except IndexError:
        print("ERRO: A lista de resultados está vazia. Nenhuma informação de usuário disponível.")



main()

