# 4- Calculadora de Idade em Dias
# Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

# * Solicite o ano de nascimento da pessoa.  
# * Considere o ano atual automaticamente.  
# * Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
# * Exiba o resultado final.

from datetime import datetime

def main():
    birth_year = int(input("Ano de nascimento: "))
    current_year = datetime.now().year

    age_in_years = current_year - birth_year
    age_in_days = age_in_years * 365

    print(f"Idade em anos: {age_in_years}, idade em dias: {age_in_days}")
    
main()