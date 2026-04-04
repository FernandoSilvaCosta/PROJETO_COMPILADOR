from scanner import Scanner
from jacktoken import TokenType
from xml_generator import token_to_xml

#TESTA NUMEROS INTEIROS
def test_number():
  
    code = "157"
    scanner = Scanner(code)
    tokens = scanner.tokenize()

    assert tokens[0].type == TokenType.NUMBER
    assert tokens[0].lexeme == "157"
    assert token_to_xml(tokens[0]) == '<integerConstant> 157 </integerConstant>'
    print("Teste Finalizado e Aprovado!")
