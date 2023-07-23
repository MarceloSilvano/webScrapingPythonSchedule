import requisicoes
import json

# A variável python em forma de string
python_string = str(requisicoes.tabela)

# Encontrar o índice em que a constante "classificacao" começa
start_index = python_string.find('const classificacao = ') + len('const classificacao = ')

# Remover o código HTML restante da string
classificacao_str = python_string[start_index:]

# Encontrar o índice do ponto e vírgula que termina a declaração da constante "classificacao"
end_index = classificacao_str.find(';')

# Recuperar a string apenas com a constante "classificacao"
classificacao_str = classificacao_str[:end_index]

# Carregar a string em formato JSON
classificacao_json = json.loads(classificacao_str)

# Salvar em um arquivo JSON
with open('classificacao.json', 'w') as file:
    json.dump(classificacao_json, file)

print("Dados da classificação foram salvos em classificacao.json")

#teste