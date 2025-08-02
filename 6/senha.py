
# 1- Gerador de Senhas Seguras  
# Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

# * Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
# * A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
# * Exiba a senha gerada ao final do programa.  

# Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.

import random
import string
import secrets

def main():
    size = int(input("Tamanho da senha: "))

    # usar random.SystemRandom() é mais seguro do que random.choice() num contexto de criar senhas.
    # password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(size))
    # password = ''.join(random.SystemRandom(string.ascii_letters + string.digits + string.punctuation) for _ in range(size))

    # para python > 3.6 secrets.choice()
    password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(size))


    print(password)


main()

