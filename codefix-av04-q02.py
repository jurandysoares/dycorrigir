#!/usr/bin/env python3

"""
Correção de código Python.
"""

from argparse import ArgumentParser
from importlib import import_module
from pathlib import Path
import sys

valores_teste = [ -10,    1,     10,    15,    16,    20,    25,    30,    31,    40]
resp_esperadas = {
    '1_quinzena': [False, True,  True,  True,  False, False, False, False, False, False],
    '2_quinzena': [False, False, False, False, True,  True,  True,  True,  True,  False]
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
        for v in valores_teste:
            try:
                resp = mod_av04q2.eh_prim_quinzena(v)
                if resp == resp_esperadas['1_quinzena'][valores_teste.index(v)]:
                    pontuacao += 1
                    f.write(f'Teste da 1ª quinzena para valor {v}: OK\n')
                else:
                    f.write(f'Teste da 1ª quinzena para valor {v}: ERRO\n')
            except Exception as e:
                f.write(f'Teste da 1ª quinzena para valor {v}: ERRO\n')

            try:
                resp = mod_av04q2.eh_seg_quinzena(v)
                if resp == resp_esperadas['2_quinzena'][valores_teste.index(v)]:
                    pontuacao += 1
                    f.write(f'Teste da 2ª quinzena para valor {v}: OK\n')
                else:
                    f.write(f'Teste da 2ª quinzena para valor {v}: ERRO\n')
            except Exception as e:
                f.write(f'Teste da 2ª quinzena para valor {v}: ERRO\n')

        f.write(f'\nPontuação: {pontuacao}\n')
    
if __name__ == '__main__':
    main()