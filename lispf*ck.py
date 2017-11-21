import ox
import re
import click
import pprint

# Parser functions
def create_list(l_paranthesis, r_paranthesis):
    return '()'


def add_to_list(first_param, second_param):
    return(first_param,) + second_param

# Tokens: List of tokens for lispf*ck
tokens_list = [
    'NUMBER',
    'CHARACTER',
    'L_PARANTHESIS',
    'R_PARANTHESIS',
    'COMMENT',
    'NEW_LINE',
]

# Lexer regular expressions to user tokens list
lexer_rules = [
    (tokens_list[0], r'\d+(\.\d*)?(e-?\d+)?'),
    (tokens_list[1], r'^([\'|\"]{1})+(?:(\w+|\W+|\d+|\D+|\s+|\S+|))+([\'|\"]{1})$'),
    (tokens_list[2], r'[(]'),
    (tokens_list[3], r'[)]'),
    (tokens_list[4], r';[^\n]*'),
    (tokens_list[5], r'\s+'),
]

# Parser rules to create AST
parser_rules = [
    ('exec_block : L_PARANTHESIS R_PARANTHESIS', create_list(l_paranthesis, r_paranthesis)),
    ('exec_block : L_PARANTHESIS expr R_PARANTHESIS', lambda x, y, z: y),
    ('expr : atom expr',  add_to_list(first_param, second_param)),
    ('expr : atom', lambda x: (x,)),
    ('atom: exec_block', lambda x: x),
    ('atom: CHARACTER', lambda x: x),
    ('atom: NUMBER', lambda x: float(x)),
]

# Click Module
@click.command()
@click.argument('source', type=click.File('r'))

# Run Application
def ast(source):

    lispfu_ck_code = source.read()
    tokens = lexer(lispfu_ck_code)
    tree = parser(tokens)
    pprint.pprint(tree)

if __name__ == '__main__':
    ast()
