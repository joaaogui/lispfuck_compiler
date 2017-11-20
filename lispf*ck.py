import ox
import re

# TOKENS

tokens_list = [
    'NUMBER',
    'BLOCK',
    'PRINT',
    'ADD',
    'LOOP',
    'L_PARANTHESIS',
    'R_PARANTHESIS',
    'FUNCTION',
    'DO_BEFORE',
    'DO_AFTER'
]


# LEXER

lexer = ox.make_lexer([
    (tokens_list[0], r'\d+(\.\d*)?(e-?\d+)?'),
    (tokens_list[1], r'^\s*do'),
    (tokens_list[2], r'^\s*print'),
    (tokens_list[3], r'^\s*add'),
    (tokens_list[4], r'^\s*loop'),
    (tokens_list[5], r'[(]'),
    (tokens_list[6], r'[)]'),
    (tokens_list[7], r'^\s*def'),
    (tokens_list[8], r'^\s*do-before'),
    (tokens_list[9], r'^\s*do-after')
])

aux = lexer('do-after')
print(aux)

