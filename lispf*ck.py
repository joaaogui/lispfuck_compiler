import ox
import re
import click
import pprint


# Click Module
@click.command()
@click.argument('lispf_ck', type=click.File('r'))


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
    ('exec_block : L_PARANTHESIS R_PARANTHESIS', lambda x,y: '()'),
    ('exec_block : L_PARANTHESIS expr R_PARANTHESIS', lambda x, y, z: y),
    ('expr : atom expr', lambda x,y: (x,) + y),
    ('expr : atom', lambda x: (x,)),
    ('atom: exec_block', lambda x: x),
    ('atom: CHARACTER', lambda x: x),
    ('atom: NUMBER', lambda x: float(x)),
]

lexer = ox.make_parser(lexer_rules)
parser = ox.make_parser(parser_rules, tokens_list)


# Run Application
def ast(lispf_ck):

    lispfu_ck_code = lispf_ck.read()
    tokens = lexer(lispfu_ck_code)
    tree = parser(tokens)
    pprint.pprint(tree)

if __name__ == '__main__':
    ast()
