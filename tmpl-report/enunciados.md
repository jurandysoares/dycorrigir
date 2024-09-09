## Tipos de variáveis

Informe o tipo apropriado para cada um dos seguintes dados:

1. `nome:` Nome de uma pessoa.
1. `ano_nasc:` Ano de nascimento de uma pessoa.
1. `idade:` Idade de uma pessoa.
1. `frase:` Frase predileta da pessoa.
1. `eh_pcd:` É uma Pessoa com Deficiência?
1. `qt_irmaos:` Quantidade de irmãos.
1. `eh_adolescente:` Tem entre 10 (inclusive) e 18 anos?
1. `peso:` Peso em quilograma (kg) de uma pessoa.
1. `estado_lampada:` Estado de uma lâmpada (Ligada/Desligada).
1. `saldo_conta:` Saldo de uma conta bancária.

### Solução

1. `nome:` Texto
1. `ano_nasc:` Inteiro
1. `idade:` Inteiro
1. `frase:` Texto
1. `eh_pcd:` Lógico
1. `qt_irmaos:` Inteiro
1. `eh_adolescente:` Lógico
1. `peso:` Real
1. `estado_lampada:` Lógico
1. `saldo_conta:` Real


\pagebreak

## Código fonte

Abra o IDLE e teste individualmente cada uma das variáveis:

1. Atribua um valor a cada uma das 8 variáveis que **não** estão em negrito (`idade` e `eh_adolescente`)
2. Inicie a variável **idade** com uma expressão que a calcule baseado no ano atual (2024) e na variável **ano_nasc**
3. Inicie a variável **eh_adolescente** com uma **expressão** baseada na variável **idade**. Considere como adolescente uma pessoa tem mais de 10 anos, inclusive, e menos de 18 anos.
Cole ou digite o código com a **atribuição** de todas as 10 variáveis no campo **Variáveis**.

```{#mycode .haskell .numberLines}
# INI
nome
ano_nasc
idade
frase
eh_pcd
qt_irmaos
eh_adolescente
peso
estado_lampada
saldo_conta
# FIM
```

### Solução

```{#yourcode .python .numberLines}
# INI
nome: str = "Fulano de Tal Pereira da Silva" 
ano_nasc: int = 2008
idade: int = 2024-ano_nasc
frase: str = "Água mole em pedra dura, tanto bate até que fura" 
eh_pcd: bool = False
qt_irmaos: int = 6
eh_adolescente: bool = False
peso: float = 92.50
estado_lampada: bool = False
saldo_conta: float = 1_000.00
# FIM
```