import ox
import click
import pprint

tokens_list = [
    'NUMBER',
    'DO',
    'PRINT',
    'ADD',
    'LOOP',
    'L_PARENTHESIS',
    'R_PARENTHESIS',
    'DO_BEFORE',
    'DO_AFTER',
    'INCREMENT',
    'DECREMENT',
    'READ',
    'RIGHT',
    'LEFT',
    'SUB',
    'ignore_COMMENT',
    'ignore_BREAK_LINE',
    'ignore_SPACE',
]

lexer = ox.make_lexer([
    (tokens_list[4], r'loop'),
    (tokens_list[10], r'dec'),
    (tokens_list[9], r'inc'),
    (tokens_list[5], r'\('),
    (tokens_list[6], r'\)'),
    (tokens_list[12], r'right'),
    (tokens_list[13], r'left'),
    (tokens_list[2], r'print'),
    (tokens_list[11], r'read'),
    (tokens_list[1], r'do'),
    (tokens_list[8], r'do-after'),
    (tokens_list[7], r'do-before'),
    (tokens_list[3], r'add'),
    (tokens_list[14], r'sub'),
    (tokens_list[0], r'[0-9]+'),
    (tokens_list[15], r';[^\n]*'),
    (tokens_list[16], r'\n'),
    (tokens_list[17], r'\s+'),
])
parser_rules = [
    ('expr : L_PARENTHESIS R_PARENTHESIS', lambda x, y: '()'),
    ('expr : L_PARENTHESIS term R_PARENTHESIS', lambda x, y, z: y),
    ('term : atom term', lambda x, y: (x,) + y),
    ('term : atom', lambda x:(x,)),
    ('atom : expr', lambda x:x),
    ('atom : DECREMENT', lambda x:x),
    ('atom : INCREMENT', lambda x:x),
    ('atom : LOOP', lambda x:x),
    ('atom : RIGHT', lambda x:x),
    ('atom : LEFT', lambda x:x),
    ('atom : PRINT', lambda x:x),
    ('atom : READ', lambda x:x),
    ('atom : DO', lambda x:x),
    ('atom : DO_AFTER', lambda x:x),
    ('atom : DO_BEFORE', lambda x:x),
    ('atom : ADD', lambda x:x),
    ('atom : SUB', lambda x:x),
    ('atom : NUMBER', int),
]

parser = ox.make_parser(parser_rules, tokens_list)


def do_after(operand, source_array):

    array = []
    index = 0
    array_size = len(source_array)

    while index < array_size:
        if source_array[index] == 'add' or source_array[index] == 'sub':
            array.append(source_array[index])
            index += 1

        array.append(source_array[index])
        array.append(operand)

        index += 1

    return array


def do_before(operand, source_array):

    array = []
    index = 0
    array_size = len(source_array)

    while index < size:
        array.append(operand)
        array.append(source_array[index])

        if source_array[index] == 'add' or source_array[index] == 'sub':
            index += 1
            array.append(source_array[index])

        index += 1

    return array


def interpreter(ast, source_array, position):
    is_loop = False
    index = 0

    while index < len(ast):

        if isinstance(ast[index], tuple):
            source_array, position = interpreter(
                ast[index], source_array, position)

        elif ast[index] == 'do-before':
            index += 1
            operand = ast[index]
            index += 1
            array = do_before(operand, list(ast[index]))
            interpreter(array, source_array, position)

        elif ast[index] == 'do-after':
            index += 1
            operand = ast[index]
            index += 1
            array = do_after(operand, list(ast[index]))
            interpreter(array, source_array, position)

        elif ast[index] == 'inc':
            source_array[position] += 1

        elif ast[index] == 'dec':
            source_array[position] -= 1

        elif ast[index] == 'right':
            position += 1
            if len(source_array) - 1 < position:
                source_array.append(0)

        elif ast[index] == 'left':
            position -= 1
            if position < 0:
                source_array.append(0)

        elif ast[index] == 'add':
            index += 1
            source_array[position] += ast[index]

        elif ast[index] == 'sub':
            index += 1
            source_array[position] -= ast[index]

        elif ast[index] == 'print':
            print(chr(source_array[position]), end='')

        elif ast[index] == 'read':
            source_array[position] = input('input: ')

        elif ast[index] == 'loop':
            if source_array[position] == 0:
                is_loop = False
                break
            else:
                is_loop = True

        # Run again
        if is_loop is True and index == len(ast) - 1:
            index = -1

        index += 1

    return source_array, position

# Eval
def evaluator(ast):
    array = [0]
    position = 0
    array, position = interpreter(ast, array, position)

# Click Module
@click.command()
@click.argument('lispf_ck', type=click.File('r'))

# Run Script
def run(lispf_ck):
    source = lispf_ck.read()
    tokens = lexer(source)
    print("")
    print('List of tokens: \n\n', tokens)
    print("")
    tree = parser(tokens)
    print("\nSyntax Tree:")
    print("")
    pprint.pprint(tree)
    evaluator(tree)


if __name__ == '__main__':
    run()
