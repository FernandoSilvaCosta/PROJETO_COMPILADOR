import os
import re
import pytest
from parser import Parser
from scanner import Scanner
from jacktoken import TokenType


def _normalize_xml(xml_text: str) -> str:
    """Normaliza XML removendo linhas vazias e espaços extras."""
    lines = []
    for line in xml_text.strip().splitlines():
        stripped = line.rstrip()
        if stripped:
            lines.append(stripped)
    return "\n".join(lines)


# ==================================================================
# Testes Unitários Básicos
# ==================================================================

def test_parse_term_integer():
    code = "10"
    tokens = [t for t in Scanner(code).tokenize() if t.type != TokenType.EOF]
    parser = Parser(tokens)
    parser.parse_term()
    xml = parser.get_xml()
    assert "<term>" in xml
    assert "<integerConstant> 10 </integerConstant>" in xml

def test_parse_expression():
    code = "10 + 20"
    tokens = [t for t in Scanner(code).tokenize() if t.type != TokenType.EOF]
    parser = Parser(tokens)
    parser.parse_expression()
    xml = parser.get_xml()
    assert "<expression>" in xml
    assert "<integerConstant> 10 </integerConstant>" in xml
    assert "<symbol> + </symbol>" in xml
    assert "<integerConstant> 20 </integerConstant>" in xml

def test_parse_let():
    code = "let x = 10;"
    tokens = [t for t in Scanner(code).tokenize() if t.type != TokenType.EOF]
    parser = Parser(tokens)
    parser.parse_let()
    xml = parser.get_xml()
    assert "<letStatement>" in xml
    assert "<keyword> let </keyword>" in xml
    assert "<identifier> x </identifier>" in xml

def test_parse_if():
    code = "if (x) { let y = 1; }"
    tokens = [t for t in Scanner(code).tokenize() if t.type != TokenType.EOF]
    parser = Parser(tokens)
    parser.parse_if()
    xml = parser.get_xml()
    assert "<ifStatement>" in xml
    assert "<keyword> if </keyword>" in xml

def test_parse_while():
    code = "while (x) { let y = 1; }"
    tokens = [t for t in Scanner(code).tokenize() if t.type != TokenType.EOF]
    parser = Parser(tokens)
    parser.parse_while()
    xml = parser.get_xml()
    assert "<whileStatement>" in xml
    assert "<keyword> while </keyword>" in xml

def test_parse_do():
    code = "do draw();"
    tokens = [t for t in Scanner(code).tokenize() if t.type != TokenType.EOF]
    parser = Parser(tokens)
    parser.parse_do()
    xml = parser.get_xml()
    assert "<doStatement>" in xml
    assert "<keyword> do </keyword>" in xml

def test_parse_return():
    code = "return x;"
    tokens = [t for t in Scanner(code).tokenize() if t.type != TokenType.EOF]
    parser = Parser(tokens)
    parser.parse_return()
    xml = parser.get_xml()
    assert "<returnStatement>" in xml
    assert "<keyword> return </keyword>" in xml

def test_parse_class_simple():
    code = "class Main { }"
    tokens = Scanner(code).tokenize()
    parser = Parser(tokens)
    parser.parse_class()
    xml = parser.get_xml()
    assert "<class>" in xml
    assert "<keyword> class </keyword>" in xml
    assert "<identifier> Main </identifier>" in xml

def test_parse_class_with_field():
    code = "class Foo { field int x; }"
    tokens = Scanner(code).tokenize()
    parser = Parser(tokens)
    parser.parse_class()
    xml = parser.get_xml()
    assert "<classVarDec>" in xml
    assert "<keyword> field </keyword>" in xml

def test_parse_class_with_subroutine():
    code = "class Foo { function void bar() { return; } }"
    tokens = Scanner(code).tokenize()
    parser = Parser(tokens)
    parser.parse_class()
    xml = parser.get_xml()
    assert "<subroutineDec>" in xml
    assert "<subroutineBody>" in xml
    assert "<parameterList>" in xml


# ==================================================================
# Testes de Validação com Projetos Oficiais (Nand2Tetris)
# ==================================================================

class TestValidationNand2Tetris:
    """Validação final comparando com arquivos .xml de referência."""

    @pytest.mark.parametrize("project_dir, jack_file", [
        ("Square", "Main.jack"),
        ("Square", "Square.jack"),
        ("Square", "SquareGame.jack"),
        ("ArrayTest", "Main.jack"),
    ])
    def test_official_files(self, project_dir, jack_file):
        base_path = f'tests/nand2tetris/{project_dir}'
        jack_path = os.path.join(base_path, jack_file)
        xml_ref_path = os.path.join(base_path, jack_file.replace('.jack', '.xml'))

        if not os.path.exists(jack_path) or not os.path.exists(xml_ref_path):
            pytest.skip(f"Arquivos não encontrados em {base_path}")

        with open(jack_path, 'r', encoding='utf-8') as f:
            code = f.read()

        tokens = Scanner(code).tokenize()
        parser = Parser(tokens)
        parser.parse_class()

        xml_output = _normalize_xml(parser.get_xml())
        with open(xml_ref_path, 'r', encoding='utf-8') as f:
            xml_ref = _normalize_xml(f.read())

        assert xml_output == xml_ref, f"Falha na validação de {jack_file}"
