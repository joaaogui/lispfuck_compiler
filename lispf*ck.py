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
    'FUNCTION_NAME',
    'DO_BEFORE',
    'DO_AFTER',
    'PARAMS',
    'OPERATORS',
]


# LEXER

lexer_rules =  [
    (tokens_list[0], r'\d+(\.\d*)?(e-?\d+)?'),
    (tokens_list[1], r'^\s*do'),
    (tokens_list[2], r'^\s*print'),
    (tokens_list[3], r'^\s*add'),
    (tokens_list[4], r'^\s*loop'),
    (tokens_list[5], r'[(]'),
    (tokens_list[6], r'[)]'),
    (tokens_list[7], r'^\s*def'),
    (tokens_list[8], r'^([\'|\"]{1})+(?:(\w+|\W+|\d+|\D+|\s+|\S+|))+([\'|\"]{1})$'),
    (tokens_list[9], r'^\s*do-before'),
    (tokens_list[10], r'^\s*do-after'),
    (tokens_list[11], r'[()]'),
    (tokens_list[12], r'/\((.*?)\)/'),
]

# PARSER

parser_rules = [
    ('function: FUNCTION FUNCTION_NAME PARAMS'),
    ('atom: PARAMS', None),
    ('atom: FUNCTION',  None),
    ('atom: FUNCTION_NAME', None),
    ('atom: NUMBER', float),
]


lexer = ox.make_lexer(lexer_rules)
parser = ox.make_parser(parser_rules, tokens_list)
aux = parser(lexer('def f ()'))

print(aux)


# Functions
