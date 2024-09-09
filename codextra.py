#!/usr/bin/env python3

"""
Extração de códigos de um arquivo CSV.
"""

from argparse import ArgumentParser
from csv import DictReader
from pathlib import Path

from slugify import slugify

def main():
    parser = ArgumentParser(description='Analisa arquivo CSV')
    parser.add_argument('arquivo', type=Path, help='Arquivo CSV a ser analisado')
    args = parser.parse_args()
    
    
    pwd = Path.cwd()
    with args.arquivo.open() as arquivo:
        leitor = DictReader(arquivo)
        # print(leitor.fieldnames)
        # leitor.fieldnames = ['Carimbo de data/hora', 'Endereço de e-mail', 
        # 'Pontuação', 'Nome', 'Matrícula', 'nome', 'ano_nasc', 'idade', 
        # 'frase', 'eh_pcd', 'qt_irmaos', 'eh_adolescente', 'peso', 
        # 'estado_lampada', 'saldo_conta', 'Variáveis']
        
        codigos = pwd / 'codigos'
        codigos.mkdir(exist_ok=True)
        
        for i,linha in enumerate(leitor, start=1):
            email = linha['Endereço de e-mail']
            usuario = email.split('@')[0]
            # arquivo_saida = codigos / f'm{i:02d}-{slugify(usuario)}.py'
            arquivo_saida = codigos / f'{slugify(usuario.replace(".", ""))}.py'
            with arquivo_saida.open(mode='w', encoding='utf-8') as saida:
                saida.write(f'__AUTOR__ = "{linha["Nome"]}"\n')
                saida.write(f'__MATRICULA__ = "{linha["Matrícula"]}"\n')
                saida.write(f'__EMAIL__ = "{linha["Endereço de e-mail"]}"\n')
                saida.write('\n\n')
                saida.write(linha['Variáveis'])
                
            
if __name__ == '__main__':
    main()