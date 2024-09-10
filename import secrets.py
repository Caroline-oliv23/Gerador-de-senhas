import secrets
import string

def gerar_senha(comprimento=12, incluir_simbolos=True):
    """
    Gera uma senha aleatória.

    :param comprimento: Comprimento da senha gerada (default é 12).
    :param incluir_simbolos: Se True, inclui caracteres especiais na senha (default é True).
    :return: Senha gerada.
    """
    # Define o conjunto de caracteres a serem usados na senha
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    # Gera a senha
    senha = ''.join(secrets.choice(caracteres) for _ in range(comprimento))
    return senha

# Exemplo de uso
if __name__ == "__main__":
    comprimento = int(input("Digite o comprimento desejado para a senha: "))
    incluir_simbolos = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'
    
    senha_gerada = gerar_senha(comprimento, incluir_simbolos)
    print(f"Sua senha gerada é: {senha_gerada}")
