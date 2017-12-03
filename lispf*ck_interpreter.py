import ox

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
     'DO_AFTER',
]
 
parser_rules = [
    ('atom : NUMBER', lambda x: x),
    ('atom : PRINT', lambda x: x),
]

 # LEXER

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




parser = ox.make_parser(parser_rules, tokens_list)
  