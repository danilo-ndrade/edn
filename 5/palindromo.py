# 2- Verificador de Palíndromos
# Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

# *Solicite ao usuário uma palavra ou frase.
# *Desconsidere letras maiúsculas, espaços e sinais de pontuação.
# *Verifique se a frase é um palíndromo.
# *Exiba "Sim" se for palíndromo ou "Não" se não for.

# Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.

def verificador():
    palavra = input("Palavra: ").strip().lower()

    palavra_limpa = ""

    for letra in palavra:
        if 'a' <= letra <= 'z':
            palavra_limpa += letra
        elif '0' <= letra <= '9':
            palavra_limpa += letra

    print(palavra_limpa)

    if palavra_limpa == palavra_limpa[::-1]:
        print(f"{palavra} é um palíndromo")
    else:
        print(f"{palavra} não é um palíndromo")


verificador()


