# 3- Verificador de Senhas Fortes
# Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

# * Solicitar a senha até que o usuário digite "sair".  
# * Verificar se a senha possui pelo menos 8 caracteres.  
# * Verificar se contém pelo menos um número.  
# * Informar se a senha é fraca ou forte.  
# * Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair". 

def verificar_senha_forte():
    while True:
        senha = input("Digite sua senha (ou 'sair' para encerrar): ")

        if senha.lower() == "sair":
            print("Programa encerrado.")
            break

        if len(senha) < 8:
            print("Senha fraca: Deve ter pelo menos 8 caracteres.")
            continue 

        contem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                contem_numero = True
                break 

        if not contem_numero:
            print("Senha fraca: Deve conter pelo menos um número.")
            continue 

        print("Senha forte: Sua senha atende aos requisitos de segurança.")
        break

verificar_senha_forte()