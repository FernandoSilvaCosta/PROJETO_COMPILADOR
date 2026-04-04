from jacktoken import Token, TokenType

#CLASSE DE LEITURA DO CODIGO JACK
class Scanner:
    def __init__(self, code: str):
        self.code = code       # codigo fonte completo
        self.current = 0       # posição atual no código
        self.line = 1          # linha atual (para mensagens de erro)
        self.tokens = []       # lista de tokens reconhecidos

      #DEFIÇÃO DOS SIMBOLOS
        self.SYMBOLS = {
            '(': TokenType.LPAREN,    ')': TokenType.RPAREN,
            '{': TokenType.LBRACE,    '}': TokenType.RBRACE,
            '[': TokenType.LBRACKET,  ']': TokenType.RBRACKET,
            ',': TokenType.COMMA,     ';': TokenType.SEMICOLON,
            '.': TokenType.DOT,       '+': TokenType.PLUS,
            '-': TokenType.MINUS,     '*': TokenType.ASTERISK,
            '/': TokenType.SLASH,     '&': TokenType.AND,
            '|': TokenType.OR,        '<': TokenType.LT,
            '>': TokenType.GT,        '=': TokenType.EQ,
            '~': TokenType.NOT,
        }
      #DEFINIÇAO DAS KEYWORDS DA LINGUAGEM JACK
        self.KEYWORDS = {
            'class': TokenType.CLASS,           'constructor': TokenType.CONSTRUCTOR,
            'function': TokenType.FUNCTION,     'method': TokenType.METHOD,
            'field': TokenType.FIELD,           'static': TokenType.STATIC,
            'var': TokenType.VAR,               'int': TokenType.INT,
            'char': TokenType.CHAR,             'boolean': TokenType.BOOLEAN,
            'void': TokenType.VOID,             'true': TokenType.TRUE,
            'false': TokenType.FALSE,           'null': TokenType.NULL,
            'this': TokenType.THIS,             'let': TokenType.LET,
            'do': TokenType.DO,                 'if': TokenType.IF,
            'else': TokenType.ELSE,             'while': TokenType.WHILE,
            'return': TokenType.RETURN,
        }


#OLHAR O CARACTERE ATUAL E OS PROXIMOS
    def peek(self, offset=0) -> str:
        pos = self.current + offset
        if pos < len(self.code):
            return self.code[pos]
        return '\0'  # fim do código
    

#AVANÇA O CARACTERE
    def advance(self) -> None:
        if self.current < len(self.code):
            if self.code[self.current] == '\n':
                self.line += 1
            self.current += 1


#IGNORAR ESPAÇOS, TABS E QUEBRA DE LINHA
    def skip_whitespace(self) -> None:
        while True:
            c = self.peek()
            if c in (' ', '\t', '\r'):
                self.advance()
            elif c == '\n':
                self.line += 1
                self.advance()
            else:
                break


