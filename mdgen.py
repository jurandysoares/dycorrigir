"""
Gerador de arquivos Markdown (Extensão ".md") para estudantes.
"""

# TODO: Passar a lista de códigos como argumento para o script.

from csv import DictReader
from slugify import slugify

leitor = DictReader(open('../lista-codigos.txt'))

for linha in leitor:
    slug_nome = slugify(linha['nome'])
    with open(f'{slug_nome}.md', mode='w', encoding='utf-8') as arq_estudante:
        arq_estudante.write(f'''\
# {linha["nome"]}

```{{literalinclude}} {linha["codigo"]}
:linenos:
```

''')

