
def verifica_arquivo(nome_arquivo):
    with open(nome_arquivo, encoding='utf-8') as arq:
        for linha in arq:
            print(linha, end="")

def escrita_arquivo(nome_arquivo, modo, texto):
    if modo in ['w','x','a','r+']:
        with open(nome_arquivo, modo, encoding='utf-8') as arq:
            caracteres = arq.write(texto)
            print(f'{caracteres} foram escritos')
    else:
        print('Modo inválido para escrita de arquivos')
        exit()
    
