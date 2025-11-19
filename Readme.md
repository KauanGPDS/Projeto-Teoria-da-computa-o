## 🤖 Compilador "K-Lang" (Trabalho de Teoria da Computação)

Este projeto é um compilador para a disciplina de Teoria da Computação e Compiladores. O programa foi desenvolvido para analisar e validar códigos-fonte escritos em uma linguagem proprietária, apelidada de **"K-Lang"**.

O compilador implementa a análise léxica, sintática e semântica, identificando erros de sintaxe (comandos malformados) e erros semânticos (como uso de variáveis não declaradas ou incompatibilidade de tipos).

---

## 👨‍💻 Autores (Exemplo)

* **Kauan Guilherme Pinto Dos Santos - 12724228176**
* **Juliana Gleice Silva de Farias- 1262420824.**
* **Mariaclara Gomes Mejía - 825232067**
* **Luiz Henrique dos Santos Vaz - 325115678**
* **Matheus Sant'Ana Oliveira - 825243151**

---

## 🛠️ Tecnologias e Bibliotecas

Este projeto foi construído usando as seguintes tecnologias:

* **Python 3:** Foi a linguagem de programação escolhida para "orquestrar" o compilador e implementar a análise semântica.
* **ANTLR 4 (Ferramenta):** Utilizada para gerar automaticamente o analisador léxico e sintático a partir do arquivo de gramática (`.g4`).
* **ANTLR 4 (Runtime para Python):** A biblioteca `antlr4-python3-runtime` é essencial para executar os analisadores gerados em ambiente Python.

### Por que optamos pelo Python?

A escolha pelo Python foi estratégica pelos seguintes motivos:

1.  **Integração com ANTLR:** O ANTLR gera código Python nativo (`.py`), simplificando o desenvolvimento.
2.  **Facilidade e Legibilidade:** Python é uma linguagem de alto nível, o que facilitou a implementação da lógica de verificação de tipos e escopo.
3.  **Estruturas de Dados:** A **Tabela de Símbolos**, essencial para o projeto, foi implementada de forma eficiente e legível usando dicionários nativos do Python.

---

## 🚀 Especificação da Linguagem: "K-Lang"

A "K-Lang" é uma linguagem imperativa simples, com tipagem estática e sintaxe baseada em C.

### 1. Tipos de Variáveis (Requisito Mínimo)

A linguagem suporta **3 tipos de dados** primitivos:

* `int`: Utilizado para números inteiros (ex: `10`, `42`).
* `float`: Utilizado para números de ponto flutuante/decimais (ex: `3.14`, `15.5`).
* `string`: Utilizado para textos (ex: `"ola mundo"`).

### 2. Comandos e Palavras-Chave

| Categoria | Palavra-Chave | Sintaxe de Exemplo |
| :--- | :--- | :--- |
| **Declaração** | `int`, `float`, `string` | `int a;` |
| **Condicional** | `if`, `else` | `if (a > 5) { ... } else { ... }` |
| **Repetição (Loop)** | `for`, `while` | `for (a=0; a<10; a=a+1) { ... }` |
| **I/O** | `scanf`, `printf` | `scanf(variavel);` `printf("msg");` |
| **Atribuição** | `=` | `a = 10;` |

### 3. Precedência de Operadores

A gramática foi construída para respeitar a **precedência matemática padrão**:

* **Maior Precedência:** Multiplicação (`*`) e Divisão (`/`)
* **Menor Precedência:** Adição (`+`) e Subtração (`-`)
* **Controle de Fluxo:** Parênteses `()` forçam a precedência.

---

## ✅ Critérios de Avaliação (Diferenciais Implementados)

Os seguintes diferenciais, que constituem a **Análise Semântica**, foram implementados:

* **Verificação de Declaração:** O compilador verifica se uma variável foi declarada antes de ser utilizada em qualquer comando (`printf`, `scanf`, ou expressão).
* **Verificação de Tipos:** O compilador verifica a compatibilidade de tipos durante atribuições (ex: não permite `int a = "texto"`). Permite apenas conversão de `int` para `float`.
* **Tabela de Símbolos:** Utilizada para armazenar o nome, tipo, linha e escopo (implícito, global) de cada variável declarada.

---

## ⚡ Como Executar o Compilador

### 1. Requisitos

* **Python 3.x** instalado.
* Biblioteca **ANTLR 4 Runtime para Python**.

(Caso não tenha a biblioteca, instale com o comando):
```bash
pip install antlr4-python3-runtime
```

### 2. Execução

* Para compilar e analisar um arquivo (.minhalang), use o seguinte comando no terminal:

```bash
python compilador.py <caminho_do_arquivo>
```

### 3. Exemplos de Teste
# 📋 Especificação do Compilador

## 🧪 Arquivos de Teste

| Arquivo | Resultado Esperado | Comando |
|---------|-------------------|---------|
| `testes/codigo_correto.minhalang` | COMPILAÇÃO BEM-SUCEDIDA (Passa na Sintaxe e Semântica) | `python compilador.py testes/codigo_correto.minhalang` |
| `testes/codigo_com_erros.minhalang` | ERRO DE COMPILAÇÃO (Falha na Análise Semântica, apontando erros de declaração e tipos) | `python compilador.py testes/codigo_com_erros.minhalang` |

## 📦 Arquivos para Entrega

A entrega deve conter a pasta completa com os seguintes itens:

- `compilador.py` (Programa principal)
- `MeuVisitor.py` (Implementação da Tabela de Símbolos e Análise Semântica)
- `MinhaLinguagem.g4` (A gramática ANTLR)
- Arquivos Python gerados pelo ANTLR (`MinhaLinguagemLexer.py`, `MinhaLinguagemParser.py`, etc.)
- `README.md` (Esta documentação)
- Pasta `testes/` (Contendo `codigo_correto.minhalang` e `codigo_com_erros.minhalang`)