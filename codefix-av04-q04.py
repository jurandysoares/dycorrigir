#!/usr/bin/env python3

"""
Correção de código Python.
"""

from argparse import ArgumentParser
from importlib import import_module
from math import ceil
from pathlib import Path
import sys

anos_teste = [1900, 2000, 2016, 1987]
resp_esperadas = {
    'nao_eh_bissexto': [False, False, False, True],
    'pode_ser_bissexto': [False, False, True, False],
    'eh_bissexto': [False, True, True, False]
}

def main():
    parser = ArgumentParser(description='Analisa código Python da Av03')
    parser.add_argument('arquivo', type=str, help='Arquivo Python a ser analisado')
    args = parser.parse_args()
    
    cam_modulo = Path(args.arquivo)
    nome_modulo = args.arquivo[:-3]
    sys.path.append('.')
    
    global mod_av04q2
    mod_av04q2 = import_module(nome_modulo)
    
    cam_log = cam_modulo.parent / 'correcao' / f'{nome_modulo}.txt' 
    with cam_log.open(mode='w', encoding='utf-8') as f:
        pontuacao = 0
        for ano in anos_teste:
            for fun in ['nao_eh_bissexto', 'pode_ser_bissexto', 'eh_bissexto']:
                try:
                    resp = getattr(mod_av04q2, fun)(ano)
                    if resp == resp_esperadas[fun][anos_teste.index(ano)]:
                        pontuacao += 2.5
                        f.write(f'Teste para {fun}({ano}): OK\n')
                    else:
                        f.write(f'Teste para {fun}({ano}): ERRO\n')
                except Exception as e:
                    f.write(f'Teste para {fun}({ano}): ERRO\n')

        f.write(f'\nPontuação: {ceil(pontuacao)}\n')
    
if __name__ == '__main__':
    main()