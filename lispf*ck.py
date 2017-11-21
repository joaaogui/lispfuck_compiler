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
lexer = ox.make_lexer([
	('OPEN', r'\('),
	('CLOSE', r'\)'),
	('SYMBOL', r'[-a-zA-Z]+'),
	('NUMBER', r'[0-9]+'),
	('ignore_COMMENT', r';[^\n]*'),
	('ignore_NEWLINE', r'\s+'),
])


tokens = ['SYMBOL',
      	'NUMBER',
      	'OPEN',
      	'CLOSE']

parser = ox.make_parser([
    	('sexpr : OPEN CLOSE', lambda x,y: '()'),
    	('sexpr : OPEN expr CLOSE', lambda x,y,z: y),
    	('expr : atom expr', lambda x,y: (x,) + y),
    	('expr : atom', lambda x: (x,)),
    	('atom : sexpr', lambda x: x),
    	('atom : NUMBER', lambda x: x),
    	('atom : SYMBOL', lambda x: x),
], tokens)
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
