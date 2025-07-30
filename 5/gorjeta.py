# 1- Calculadora de Gorjeta
# Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

# * Defina o valor da conta (ex: R$ 100,00).  
# * Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
# * O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.

def calculadora():
    while True:
        
        try:
            conta = float(input("Valor da conta: "))
            porcentagem = float(input("Porcentagem de gorjeta: "))

            if conta <= 0:
                print("O valor da conta precisa ser maior que 0.")
                continue
                
            resultado = conta * (porcentagem / 100)

            print(f"O valor da gorjeta é: R$ {resultado:.2f}")

        except ValueError:
            print("O valores devem ser numéricos.")



calculadora()


