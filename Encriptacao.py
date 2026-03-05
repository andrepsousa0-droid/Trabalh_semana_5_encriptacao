
def encriptar(texto: str, chaves: list) -> str:
    """
    Encripta um texto usando um método de substituição baseado na Tabela ASCII.
    Aceita chaves de um número (ex: [3]) ou múltiplos números (ex: [1, 5, 2]).
    """
    texto_encriptado = ""
    
    # O enumerate permite-nos saber em que posição (i) e letra (char) estamos
    for i, char in enumerate(texto):
        # A MAGIA DA CHAVE MÚLTIPLA: 
        # O operador % (resto da divisão) faz com que a chave ande em círculo.
        # Se a chave for [1, 5, 2], ele usa o 1, depois o 5, depois o 2, e volta ao 1!
        chave_atual = chaves[i % len(chaves)]
        
        # Transforma o carácter em número, soma a chave, e volta a carácter.
        # O '% 256' garante que o número não sai dos limites da Tabela ASCII.
        novo_char = chr((ord(char) + chave_atual) % 256)
        
        texto_encriptado += novo_char
        
    return texto_encriptado


def desencriptar(texto: str, chaves: list) -> str:
    """
    Faz exatamente o inverso da função encriptar, subtraindo a chave.
    """
    texto_desencriptado = ""
    
    for i, char in enumerate(texto):
        chave_atual = chaves[i % len(chaves)]
        
        # Aqui SUBTRAÍMOS a chave para andar para trás no alfabeto/tabela
        novo_char = chr((ord(char) - chave_atual) % 256)
        
        texto_desencriptado += novo_char
        
    return texto_desencriptado


def main() -> None:
    # 1. Definimos o nosso texto de teste
    mensagem_secreta = "Python e Criptografia: A combinacao perfeita para o 20!"
    
    # --- TESTE A: CHAVE SIMPLES (Apenas 1 número) ---
    chave_simples = [3]
    resultado_enc_simples = encriptar(mensagem_secreta, chave_simples)
    resultado_dec_simples = desencriptar(resultado_enc_simples, chave_simples)
    
    print("=== TESTE 1: CHAVE SIMPLES [3] ===")
    print(f"Original:      {mensagem_secreta}")
    print(f"Encriptado:    {resultado_enc_simples}")
    print(f"Desencriptado: {resultado_dec_simples}")
    # Verificação automática (Requisito 2)
    print(f"✅ O código reverteu perfeitamente? {mensagem_secreta == resultado_dec_simples}\n")


    # --- TESTE B: CHAVE MÚLTIPLA (Vários números) ---
    chave_multipla = [1, 4, 2]
    resultado_enc_multi = encriptar(mensagem_secreta, chave_multipla)
    resultado_dec_multi = desencriptar(resultado_enc_multi, chave_multipla)
    
    print("=== TESTE 2: CHAVE MÚLTIPLA [1, 4, 2] ===")
    print(f"Original:      {mensagem_secreta}")
    print(f"Encriptado:    {resultado_enc_multi}")
    print(f"Desencriptado: {resultado_dec_multi}")
    # Verificação automática (Requisito 2)
    print(f"✅ O código reverteu perfeitamente? {mensagem_secreta == resultado_dec_multi}\n")

if __name__ == "__main__":
    main()