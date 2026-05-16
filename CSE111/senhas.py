#criando o verificador de força de senhas com funções
MINUSCULAS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
MAIUSCULAS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
ESPECIAIS=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]



def main():
    while True:
        senha = input("Digite a senha para verificar sua força (ou 'q' para sair): ")
        if senha == "q" or senha == "Q":
            break
        forca = validar_senha(senha)
        print(f"Força da senha: {forca}")
        if forca < 4:
            sugerir_melhoria(senha)

def validar_senha(senha, comprimento_min=10, comprimento_forte=15):
    # 1. Verifica dicionário (sem distinção de maiúsculas)
    if procurar_palavra(senha, "lista_de_palavras.txt"):
        print("A senha é uma palavra do dicionário e não é segura.")
        return 0
    
    # 2. Verifica senhas comuns (COM distinção de maiúsculas)
    if procurar_palavra(senha, "senhas_mais_comuns.txt", True):
        print("A senha é comumente usada e não é segura.")
        return 0
    
    # 3. Verifica comprimento mínimo
    if len(senha) < comprimento_min:
        print("A senha é muito curta e não é segura.")
        return 1
    
    # 4. Verifica comprimento forte
    if len(senha) > comprimento_forte:
        print("A senha é longa, o comprimento supera a complexidade e é uma boa senha.")
        return 5
    
    # 5. Demais casos - calcula complexidade
    complexidade = calcular_complexidade(senha)
    return complexidade

def calcular_complexidade(palavra):
    complexidade = 0
    
    if palavra_tem_caractere(palavra, MINUSCULAS):
        complexidade += 1
    if palavra_tem_caractere(palavra, MAIUSCULAS):
        complexidade += 1
    if palavra_tem_caractere(palavra, DIGITOS):
        complexidade += 1
    if palavra_tem_caractere(palavra, ESPECIAIS):
        complexidade += 1
    
    return complexidade

def palavra_tem_caractere(palavra, lista_caracteres):
    for caractere in palavra:
        if caractere in lista_caracteres:
            return True
    return False

def procurar_palavra(palavra, nome_do_arquivo, maiusculas_e_minusculas=False):
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not maiusculas_e_minusculas:
                linha = linha.lower()
                palavra = palavra.lower()
            if linha == palavra:
                return True
    return False

# CRIATIVIDADE: função que sugere melhorias para a senha com base nos tipos
# de caracteres ausentes, ajudando o usuário a criar senhas mais seguras.
def sugerir_melhoria(senha):
    if not palavra_tem_caractere(senha, MAIUSCULAS):
        print("Dica: adicione letras maiúsculas.")
    if not palavra_tem_caractere(senha, DIGITOS):
        print("Dica: adicione números.")
    if not palavra_tem_caractere(senha, ESPECIAIS):
        print("Dica: adicione símbolos especiais.")

if __name__ == "__main__":
    main()