temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Qual a unidade de origem? (C, F ou K): ").upper()
unidade_destino = input("Para qual unidade deseja converter? (C, F ou K): ").upper()

if unidade_origem == 'C':
    if unidade_destino == 'F':
        resultado = (temperatura * 9/5) + 32
        print(f"{temperatura}°C é igual a {resultado:.2f}°F")
    elif unidade_destino == 'K':
        resultado = temperatura + 273.15
        print(f"{temperatura}°C é igual a {resultado:.2f}K")
    elif unidade_destino == 'C':
        print(f"{temperatura}°C é igual a {temperatura}°C")
    else:
        print("Unidade de destino inválida.")
elif unidade_origem == 'F':
    if unidade_destino == 'C':
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura}°F é igual a {resultado:.2f}°C")
    elif unidade_destino == 'K':
        resultado = (temperatura - 32) * 5/9 + 273.15
        print(f"{temperatura}°F é igual a {resultado:.2f}K")
    elif unidade_destino == 'F':
        print(f"{temperatura}°F é igual a {temperatura}°F")
    else:
        print("Unidade de destino inválida.")
elif unidade_origem == 'K':
    if unidade_destino == 'C':
        resultado = temperatura - 273.15
        print(f"{temperatura}K é igual a {resultado:.2f}°C")
    elif unidade_destino == 'F':
        resultado = (temperatura - 273.15) * 9/5 + 32
        print(f"{temperatura}K é igual a {resultado:.2f}°F")
    elif unidade_destino == 'K':
        print(f"{temperatura}K é igual a {temperatura}K")
    else:
        print("Unidade de destino inválida.")
else:
    print("Unidade de origem inválida.")