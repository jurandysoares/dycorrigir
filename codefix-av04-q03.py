#!/usr/bin/env python3

"""
Correção de código Python.
"""

from argparse import ArgumentParser
from importlib import import_module
from pathlib import Path
import sys

valores_teste  = [(46, 1.65), (55, 1.65), (74, 1.65)]
resp_esperadas = [     False,       True, False]

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
        for i,(peso,altura) in enumerate(valores_teste):
            try:
                resp = mod_av04q2.tem_peso_ideal(peso=peso, altura=altura)
                if resp == resp_esperadas[i]:
                    pontuacao += 10
                    f.write(f'Teste se tem peso ideal com altura={altura} e peso={peso}: OK\n')
                else:
                    f.write(f'Teste se tem peso ideal com altura={altura} e peso={peso}: ERRO\n')
            except Exception as e:
                f.write(f'Teste se tem peso ideal com altura={altura} e peso={peso}: ERRO\n')

        f.write(f'\nPontuação: {pontuacao}\n')
    
if __name__ == '__main__':
    main()