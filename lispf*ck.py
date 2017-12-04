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
    'ignore_COMMENT',
    'ignore_NEWLINE',
]

# Lexer regular expressions to user tokens list
lexer_rules = [
    ('L_PARANTHESIS', r'\('),
    ('R_PARANTHESIS', r'\)'),
    ('CHARACTER', r'[-a-zA-Z]+'),
    ('NUMBER', r'[0-9]+'),
    ('ignore_COMMENT', r';[^\n]*'),
    ('ignore_NEWLINE', r'\s+'),
]

# Parser rules to create AST
parser_rules = [
    ('block : L_PARANTHESIS R_PARANTHESIS', lambda x, y: '()'),
    ('block : L_PARANTHESIS expr R_PARANTHESIS', lambda x, y, z: y),
    ('expr : atom expr', lambda x, y: (x,) + y),
    ('expr : atom', lambda x: (x,)),
    ('atom : block', lambda x: x),
    ('atom : NUMBER', lambda x: x),
    ('atom : CHARACTER', lambda x: x),
]

lexer = ox.make_lexer(lexer_rules)
parser = ox.make_parser(parser_rules, tokens_list)

# Click Module


@click.command()
@click.argument('lispf_ck', type=click.File('r'))
# Run Application
def ast(lispf_ck):
    lispfu_ck_code = lispf_ck.read()
    tokens = lexer(lispfu_ck_code)
    tree = parser(tokens)
    pprint.pprint(tree)


if __name__ == '__main__':
    ast()
