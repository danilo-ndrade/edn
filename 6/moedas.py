# ---

# 4- Conversor de Moedas (para Reais - BRL)  
# Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

# * Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
# * Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
# * Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
# * Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

# Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.

# --
import requests
from datetime import datetime

def main():
    while True:
        currency = input("Insira a moeda(USD | EUR | GBP): ").upper()

        if currency not in ['USD', 'EUR', 'GBP']:
            print('Moeda inválida.')
            continue

        print(datetime.now())

        try:
            res = requests.get(f'https://economia.awesomeapi.com.br/last/{currency}-BRL')
            res = res.json()

            value = res[f'{currency}BRL']['ask']
            time = res[f'{currency}BRL']['create_date']

            print(f"BRL 1.00 == {currency}{value} | {time}")
            break
        except requests.exceptions.RequestException as e:
            print(f"ERRO de requisição: {e}. Verifique sua conexão ou o URL.")
        except requests.exceptions.JSONDecodeError:
            print("ERRO: Resposta não é um JSON válido.")
        except KeyError as e:
            print(f"ERRO: Chave não encontrada na resposta JSON: {e}. A estrutura da resposta pode ter mudado.")
        except IndexError:
            print("ERRO: A lista de resultados está vazia. Nenhuma informação disponível.")


main()