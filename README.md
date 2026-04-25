# PROJETO_COMPILADOR
## Projeto de Compilador da linguagem Jack para disciplina de Compiladores 2026.1 - UFMA

### NOMES DOS INTEGRANTES :
- FERNANDO DA SILVA COSTA
- DAVI OLIVEIRA CORTES

### LINGUAGEM DE PROGRAMAÇÃO USADA:
- Python
---

## 🧠 Como Funciona

O analisador léxico lê o código-fonte Jack e transforma em uma sequência de **tokens**, ignorando espaços em branco e comentários.

### Tipos de Tokens Suportados

| Tipo | Exemplos |
|------|----------|
| `keyword` | `class`, `if`, `while`, `return` |
| `symbol` | `{`, `}`, `+`, `;`, `<`, `>` |
| `identifier` | `myVar`, `Main`, `SquareGame` |
| `integerConstant` | `0`, `42`, `289` |
| `stringConstant` | `"hello world"` |

### Saída XML

Para cada token, o scanner gera uma linha XML no formato:

```xml
<tokens>
<keyword> class </keyword>
<identifier> Main </identifier>
<symbol> { </symbol>
<integerConstant> 42 </integerConstant>
<stringConstant> hello world </stringConstant>
</tokens>
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.12+
- pytest

### Instalando o pytest

```bash
pip install pytest
```

### Rodando os Testes

```bash
# Todos os testes
python -m pytest tests/test_scanner.py -v -s

# Um teste específico
python -m pytest tests/test_scanner.py::test_number -v -s
```

---

## 🧪 Testes

O projeto segue a metodologia **TDD (Test Driven Development)**. Os testes cobrem:

- ✅ Números inteiros
- ✅ Símbolos
- ✅ Keywords
- ✅ Identificadores
- ✅ Strings
- ✅ Comentários de linha (`//`)
- ✅ Comentários de bloco (`/* */`)
- ✅ Validação com arquivos reais do nand2tetris (Square, SquareGame, Main)

---

## 📦 Arquivos Principais

### `jacktoken.py`
Define `TokenType` (enum com todos os tipos de tokens) e `Token` (dataclass com `type`, `lexeme` e `line`).

### `xml_generator.py`
Responsável por converter tokens em XML, incluindo escape de caracteres especiais (`&`, `<`, `>`, `"`).

### `scanner.py`
Coração do projeto. Lê o código-fonte caractere por caractere e produz a lista de tokens.

---

## 📚 Referências

- [Nand2Tetris](https://www.nand2tetris.org/)
- [The Elements of Computing Systems — Nisan & Schocken](https://www.nand2tetris.org/book)
