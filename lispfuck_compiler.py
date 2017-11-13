
"""
    Python package that allows to create command_line tools
    For more info: http://click.pocoo.org/
"""

import  click

# Dictionary to reference tokens from lispfuck to similar code in c
lispfuck_tokens =  ["right", "left", "inc", "dec","print", "read", "(loop", ")"]
parser_tokens =  {
    lispfuck_tokens[0]: '\t++ptr; \n',
    lispfuck_tokens[1]: '\t--ptr; \n'  ,
    lispfuck_tokens[2]: '\t++(*ptr); \n',
    lispfuck_tokens[3]: '\t--(*ptr); \n',
    lispfuck_tokens[4]: '\tprintf("%c",(*ptr)); \n',
    lispfuck_tokens[5]: '\tscanf(" %c",&(*ptr)); \n',
    lispfuck_tokens[6]: '\twhile(*ptr) { \n',
    lispfuck_tokens[7]: '\t}\n'
}

@click.command()
@click.argument('param_1', type=click.File('r'))
@click.option('-o', nargs=1, type=click.File('w'))
# Make parser from lispfuck to c

def parser(param_1, o):

    c_code = """#include<stdio.h>
#include <stdlib.h>\n
int main(){
\tunsigned char *tape = malloc(sizeof(char)*30000);
\t unsigned char *ptr =  &tape[0];\n"""

    lispfuck_code = param_1.read()
    for data in lispfuck_code:
        if data in parser_tokens:
            c_code += parser_tokens[data]

    eof = " \n return 0; \n} "
    c_code = c_code + eof

    o.write(c_code)
    o.flush()


if __name__ == "__main__":
    parser()
