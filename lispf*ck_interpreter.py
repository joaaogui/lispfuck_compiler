import ox

 # Lexer
tokens_list = [
     'NUMBER',
     'DO',
     'PRINT',
     'ADD',
     'LOOP',
     'L_PARANTHESIS',
     'R_PARANTHESIS',
     'FUNCTION',
     'DO_BEFORE',
     'DO_AFTER',
     'INCREMENT',
     'DECREMENT',
     'READ',
     'RIGHT',
     'LEFT',
     'SUB',
]

lexer = ox.make_lexer([
    (tokens_list[0], r'[0-9]+'),
    (tokens_list[1], r'^\s*do'),
    (tokens_list[2], r'^\s*print'),
    (tokens_list[3], r'^\s*add'), 
    (tokens_list[4], r'^\s*loop'),
    (tokens_list[5], r'^\s*[(]'),
    (tokens_list[6], r'^\s*[)]'),
    (tokens_list[7], r'^\s*def'),
    (tokens_list[8], r'^\s*do[-]before'),
    (tokens_list[9], r'^\s*do[-]after'),
    (tokens_list[10], r'^\s*inc'),
    (tokens_list[11], r'^\s*dec'),
    (tokens_list[12], r'^\s*read'),
    (tokens_list[13], r'^\s*right'),
    (tokens_list[14], r'^\s*left'),
    (tokens_list[15], r'^\s*sub'),
])

# Parser
parser_rules = [
    ('expr : L_PARANTHESIS R_PARANTHESIS', lambda x, y: '()'),
    ('expr : L_PARANTHESIS term R_PARANTHESIS', lambda x, y, z: y),
    ('term : atom term', lambda x, y: (x,) + y),
    ('term : atom', lambda x:(x,)),
    ('atom : READ', lambda x: x),
    ('atom : DO', lambda x: x),
    ('atom : LOOP', lambda x: x),
    ('atom : FUNCTION', lambda x: x),
    ('atom : DO_BEFORE', lambda x: x),
    ('atom : DO_AFTER', lambda x: x),
    ('atom : DECREMENT', lambda x: x),
    ('atom : INCREMENT', lambda x: x),
    ('atom : LEFT', lambda x: x),
    ('atom : RIGHT', lambda x: x),
    ('atom : ADD', lambda x: x),
    ('atom : SUB', lambda x: x),
    ('atom : PRINT', lambda x: x),
    ('atom : NUMBER', lambda x: float(x)),
]

parser = ox.make_parser(parser_rules, tokens_list)

# Evaluate
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

    while i < len(ast):

        if isinstance(ast[i], tuple):
            source_array, position = interpreter(ast[i], source_array, position)

        elif ast[i] == 'do-before':
            i += 1
            operand = ast[i]
            i += 1
            array = do_before(operand, list(ast[i]))
            interpreter(array, source_array, position)

        elif ast[i] == 'do-after':
            i += 1
            operand = ast[i]
            i += 1
            array = do_after(operand, list(ast[i]))
            interpreter(array, source_array, position)

        elif ast[i] == 'inc':
            source_array[position] += 1

        elif ast[i] == 'dec':
            source_array[position] -= 1
        
        elif ast[i] == 'right':
            position += 1
            if len(source_array) - 1 < position:
                source_array.append(0)

        elif ast[i] == 'left':
            position -= 1
            if position < 0:
                source_array.append(0)

        elif ast[i] == 'add':
            i += 1
            source_array[position] += ast[i]

        elif ast[i] == 'sub':
            i += 1
            source_array[position] -= ast[i]

        elif ast[i] == 'print':
            print(chr(source_array[position]), end='')

        elif ast[i] == 'read':
            source_array[position] = input('input: ')

        elif ast[i] == 'loop':
            if source_array[position] == 0:
                is_loop = False
                break
            else:
                is_loop = True

        # Run again
        if is_loop is True and i == len(ast) - 1:
            i = -1

        i += 1

    return source_array, position

def evaluater(ast):
    array = [0] 
    position = 0
    array, position = interpreter(ast, array, position)

  # Click Module

  
# @click.command()
# @click.argument('lispf_ck_interpreter', type=click.File('r'))

# # Run Application
# def run(lispf_ck):
#     lispfu_ck_code = lispf_ck.read()
#     tokens = lexer(lispfu_ck_code)
#     tree = parser(tokens)
#     pprint.pprint(tree)


# if __name__ == '__main__':
# 	run()