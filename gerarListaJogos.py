import requisicoes
import json

# A variável python em forma de string
python_string = str(requisicoes.tabela)

# Encontrar o índice em que a constante "listaJogos" começa
start_index = python_string.find('const listaJogos =') + len('const listaJogos =')

# Remover o código HTML restante da string
listaJogos_str = python_string[start_index:]

# Encontrar o índice do ponto e vírgula que termina a declaração da constante "listaJogos"
end_index = listaJogos_str.find(';')

# Recuperar a string apenas com a constante "listaJogos"
listaJogos_str = listaJogos_str[:end_index]

# Carregar a string em formato JSON
listaJogos_json = json.loads(listaJogos_str)

# Salvar em um arquivo JSON
with open('listaJogos.json', 'w') as file:
    json.dump(listaJogos_json, file)

print("Dados da classificação foram salvos em listaJogos.json")