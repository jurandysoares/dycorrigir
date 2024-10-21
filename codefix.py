#!/usr/bin/env python3

"""
Correção de código Python.
"""

from argparse import ArgumentParser
from importlib import import_module
import sys

# tipos_validos = ['int', 'float', 'str', 'bool', 'list', 'tuple', 'dict', 'set']
tipo_esperado_para = {
    'nome': 'str',
    'ano_nasc': 'int',
    'idade': 'int',
    'frase': 'str',
    'eh_pcd': 'bool',
    'qt_irmaos': 'int',
    'eh_adolescente': 'bool',
    'peso': 'float',
    'estado_lampada': 'bool',
    'saldo_conta': 'float',
}

def main():
    parser = ArgumentParser(description='Analisa código Python da Av03')
    parser.add_argument('arquivo', type=str, help='Arquivo Python a ser analisado')
    args = parser.parse_args()
    
    nome_modulo = args.arquivo[:-3]
    sys.path.append('.')
    
    global mod_av03
    mod_av03 = import_module(nome_modulo)
    
    pontuacao = 0
    for nome, tipo in tipo_esperado_para.items():
        if not hasattr(mod_av03, nome):
            print(f'Variável "{nome}" não encontrada no módulo "{nome_modulo}"\n')
            continue
        valor = getattr(mod_av03, nome)
        if not isinstance(valor, eval(tipo)):
            print(f'Variável "{nome}" deveria ser do tipo "{tipo}"\n')
            continue
        print(f'Variável "{nome}" está correta\n')
        pontuacao += 5
        
    print(f'Pontuação: {pontuacao}\n')
    
if __name__ == '__main__':
    main()