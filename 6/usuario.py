# ---

# 2- Gerador de Usuário Aleatório  
# Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

# * Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
# * Mostre na tela: nome completo, e-mail e país do usuário.  
# * O programa deve tratar possíveis erros de conexão ou falha na API.  

# Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.

import requests

def main():
    try:
        res = requests.get("https://randomuser.me/api/")
        print(f'Status da requisição: {res.status_code}')
        
        json_res = res.json()
        user_info = json_res['results'][0]

        name = f"{user_info['name']['title']} {user_info['name']['first']} {user_info['name']['last']}"
        email = user_info['email']
        country = user_info['location']['country']

        print(f"Nome: {name}\nEmail: {email}\nPaís: {country}")

    except requests.exceptions.RequestException as e:
        print(f"ERRO de requisição: {e}. Verifique sua conexão ou o URL.")
    except requests.exceptions.JSONDecodeError:
        print("ERRO: Resposta não é um JSON válido.")
    except KeyError as e:
        print(f"ERRO: Chave não encontrada na resposta JSON: {e}. A estrutura da resposta pode ter mudado.")
    except IndexError:
        print("ERRO: A lista de resultados está vazia. Nenhuma informação de usuário disponível.")



main()

