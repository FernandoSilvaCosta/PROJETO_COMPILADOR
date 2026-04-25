from parser import Parser
from scanner import Scanner
from jacktoken import TokenType

def test_parse_term_integer():
    """Testa o reconhecimento de um termo inteiro simples."""
    code = "10"
    tokens = [t for t in Scanner(code).tokenize() if t.type != TokenType.EOF]

    parser = Parser(tokens)
    parser.parse_term()
    xml = parser.get_xml()

    assert "<term>" in xml
    assert "<integerConstant> 10 </integerConstant>" in xml
    print("✅ Teste de term inteiro passou!")
    