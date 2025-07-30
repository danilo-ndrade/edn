
# 3- Calculadora de Desconto em Produto
# Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

# * Solicitar o preço original do produto.  
# * Solicitar o percentual de desconto desejado.  
# * Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.

def main():
    try:
        original_price = float(input("Preço do produto: "))
        discount_percentage = float(input("Percentual de desconto: "))
        
        final_price = original_price - (original_price * (discount_percentage / 100))

        print(f"Preço com desconto: R$ {final_price:.2f}")
    
    except ValueError:
        print("Os valores devem ser numéricos.")

main()

