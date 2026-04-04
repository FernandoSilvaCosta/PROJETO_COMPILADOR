from jacktoken import  Token, TokenType

#SUBSTITUIR CARACTERES PRESENTES NO HTML
def _escape_xml(text: str) -> str:
    escapes = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;'
    }
    for char, escaped in escapes.items():
        text = text.replace(char, escaped)
    return text

#MAPEAR OS TOKENS PARA TAG HTML
def _get_category(token: Token) -> str:
    if token.type == TokenType.IDENT:
        return "identifier"
    elif token.type == TokenType.NUMBER:
        return "integerConstant"
    elif token.type == TokenType.STRING:
        return "stringConstant"
    elif token.type.value == "keyword":
        return "keyword"
    else:
        return "symbol"
    
#GERAR A LINHA DO HTML
def token_to_xml(token: Token) -> str:
    category = _get_category(token)
    value = _escape_xml(token.lexeme)
    return f"<{category}> {value} </{category}>"

#CRIAÇÃO DO HTML COMPLETO
def generate_xml(tokens: list[Token]) -> str:
    lines = ["<tokens>"]
    for token in tokens:
        lines.append("  " + token_to_xml(token))
    lines.append("</tokens>")
    return "\n".join(lines)


