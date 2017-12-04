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
])

# Parser

parser_rules = [
    ('operand : NUMBER', lambda x: x),
    ('operand : PRINT', lambda x: x),
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



  