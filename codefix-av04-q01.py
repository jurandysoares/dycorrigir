#!/usr/bin/env python3

"""
Correção de código Python.
"""

from argparse import ArgumentParser
from importlib import import_module
from pathlib import Path
import sys

# tipos_validos = ['int', 'float', 'str', 'bool', 'list', 'tuple', 'dict', 'set']
tipo_esperado_para = {
    'nome': 'str',
    'matricula': 'str',
    'tenho_irmaos': 'bool',
    'qt_irmaos': 'int',
    'ano_nasc': 'int',
    'altura': 'float',
    'frase': 'str',
    'prof_matematica': 'str',
    'num_bolas': 'int',
    'qt_leite': 'float'
}

def main():
    parser = ArgumentParser(description='Analisa código Python da Av03')
    parser.add_argument('arquivo', type=str, help='Arquivo Python a ser analisado')
    args = parser.parse_args()
    
    cam_modulo = Path(args.arquivo)
    nome_modulo = args.arquivo[:-3]
    sys.path.append('.')
    
    global mod_av04
    mod_av04 = import_module(nome_modulo)
    
    pontuacao = 0
    cam_log = cam_modulo.parent / 'correcao' / f'{nome_modulo}.txt' 
    with cam_log.open(mode='w', encoding='utf-8') as f:
        for nome, tipo in tipo_esperado_para.items():
            if not hasattr(mod_av04, nome):
                f.write(f'Variável "{nome}" não encontrada no módulo "{nome_modulo}".\n')
                continue
            valor = getattr(mod_av04, nome)
            if not isinstance(valor, eval(tipo)):
                f.write(f'Variável "{nome}" deveria ser do tipo "{tipo}".\n')
                continue
            f.write(f'Variável "{nome}" está com o tipo correto.\n')
            pontuacao += 2
            
        f.write(f'Pontuação: {pontuacao}\n')
    
if __name__ == '__main__':
    main()