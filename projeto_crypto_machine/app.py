import base64

def cryptoMachine(texto_plano):
    texto_criptografado = ''
    for char in texto_plano:
        char_encoded = base64.b64encode(char.encode('utf-8')).decode('utf-8')
        texto_criptografado += char_encoded
    return texto_criptografado

def cryptoCode():
    while True:
        var_texto = str(input('Digite o texto para ser criptografado: '))

        var_texto_criptografado = cryptoMachine(var_texto)

        print(f'O texto foi criptografado {var_texto_criptografado}')

if __name__ == '__main__':    
    cryptoCode()