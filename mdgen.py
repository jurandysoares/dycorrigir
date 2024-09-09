#!/usr/bin/env python3

"""
Gerador de arquivos Markdown (Extensão ".md") para estudantes.
"""

from argparse import ArgumentParser
from csv import DictReader
from slugify import slugify

parser = ArgumentParser('Gerador de arquivos Markdown para estudantes')
parser.add_argument('arquivo', help='Arquivo no formato <nome>,<codigo>')
args = parser.parse_args()

leitor = DictReader(open(args.arquivo))


for linha in leitor:
    slug_nome = slugify(linha['nome'])
    with open(f'{slug_nome}.md', mode='w', encoding='utf-8') as arq_estudante:
        arq_estudante.write(f'''\
# {linha["nome"]}

```{{literalinclude}} {linha["codigo"]}
:linenos:
```

''')

