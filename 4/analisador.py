# 4- Analisador de Números Pares e Ímpares
# Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

# * Solicitar números inteiros até que o usuário digite "fim".  
# * Informar se o número digitado é par ou ímpar.  
# * Ao final, exibir a quantidade total de números pares e ímpares informados.  
# * Tratar entradas inválidas com mensagens de erro apropriadas. 

def analisador_pares_impares():
    total_pares = 0
    total_impares = 0

    print("--- Analisador de Números Pares e Ímpares ---")
    print("Digite um número inteiro ou 'fim' para encerrar.")

    while True:
        entrada = input("Digite um número: ")

        if entrada.lower() == "fim":
            break 

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                total_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                total_impares += 1

        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

    print("\n--- Resumo ---")
    print(f"Total de números PARES: {total_pares}")
    print(f"Total de números ÍMPARES: {total_impares}")
    print("Programa encerrado.")

analisador_pares_impares()