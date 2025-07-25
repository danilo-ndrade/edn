# 1- Calculadora Simples
# Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

# * Solicite ao usuário dois números reais.  
# * Peça a operação desejada (+, -, *, /).  
# * Realize a operação escolhida e exiba o resultado.  
# * Trate divisões por zero e operações inválidas com mensagens apropriadas.  

# O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.

def main():
    while True:
        print('-------------------------')
        print('Insira 2 números. Operadores válidos: + | - | * | /')
        print('-------------------------')
        try:
            x = float(input('Primeiro número: '))
            operator = input('Operador: ')
            if operator not in ['+', '-', '/', '*']:
                print('Operadores válidos: + | - | * | /')
                continue
            y = float(input('Segundo número: '))

            print(f'Resultado: {calculator(operator, x, y)}')
            break
        except ValueError:
            print('Error: Apenas números são aceitos.')
            continue
        except ZeroDivisionError:
            print('Error: Não é possível dividir por 0.')
            continue


def calculator(operator, x, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    else:
        return x / y


main()