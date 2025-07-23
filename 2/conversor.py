valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Valor em Dólar: US$ {valor_dolar:.2f}")
print(f"Valor em Euro: € {valor_euro:.2f}")