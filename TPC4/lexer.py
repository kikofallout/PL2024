import ply.lex as lex

tokens = (
    'SELECT', 'VARIABLE', 'FROM', 'WHERE', 'COMMA', 'NUMBER',
    'EQUALS', 'GREATER_THAN', 'LESS_THAN', 'GREATER_THAN_EQUALS', 'LESS_THAN_EQUALS'
)

t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_VARIABLE = r'id|nome|salario|empregados'
t_COMMA = r','
t_NUMBER = r'\d+'
t_EQUALS = r'\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_EQUALS = r'\>\='
t_LESS_THAN_EQUALS = r'\<\='

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
SELECT id, nome, salario FROM empregados WHERE salario >= 1000
'''

lexer.input(data)

for tok in iter(lexer.token, None):
    print(tok)