# Ordena os códigos dos autores no arquivo codigos.txt
# Formato: "nome_do_autor":"caminho_do_arquivo"
# Exemplo com cabeçalho: 
#   nome,codigo
#   "Fulano de Tal":"src/fulanotal.py"

grep __AUTOR__ src/*.py | awk -F'[:=]' '{print $3":"$1}' | sed 's/"//g' | sort > codigos.txt