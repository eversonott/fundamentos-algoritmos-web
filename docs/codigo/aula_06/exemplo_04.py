import os

caminho = './tabelas/episodios.csv'

# Para obter o último componente do caminho:
os.path.basename(caminho)

# Para obter o nome do diretório:
os.path.dirname(caminho)

# Para reunir os componentes do caminho:
os.path.join('/tmp', 'testes', 'python')

# Separar a extensão do arquivo
os.path.splitext(caminho
