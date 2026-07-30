# QA-Brazil_Automação_Python

Projeto desenvolvido durante minha formação em **Quality Assurance** na **TripleTen**, com o objetivo de automatizar testes da aplicação **Urban Routes** utilizando Python, Selenium WebDriver e Pytest.

---

## 🎯 Objetivo

Automatizar os principais fluxos da aplicação Urban Routes para validar funcionalidades críticas, reduzir a execução manual de testes e aplicar boas práticas de automação utilizando o padrão **Page Object Model (POM)**.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Selenium WebDriver
- Pytest
- Git
- GitHub
- Page Object Model (POM)

---

## 📂 Estrutura do Projeto

```text
QA-Brazil_Automação_Python/
│
├── data.py          # Dados utilizados nos testes
├── helpers.py       # Funções auxiliares
├── pages.py         # Métodos da Page Object Model
├── main.py          # Casos de teste automatizados
├── requirements.txt # Dependências do projeto
└── README.md
```

---

## ✅ Cenários Automatizados

- Definição da origem e do destino da corrida.
- Seleção da categoria Comfort.
- Cadastro e validação do número de telefone.
- Cadastro da forma de pagamento.
- Adição de cartão de crédito.
- Inclusão de mensagem para o motorista.
- Solicitação de cobertor e lenços.
- Adição de dois sorvetes ao pedido.
- Validação do fluxo completo de solicitação de corrida.

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto pude:

- Aplicar o padrão **Page Object Model (POM)**.
- Criar testes automatizados utilizando Selenium WebDriver.
- Organizar o código para facilitar sua manutenção.
- Utilizar Git e GitHub para versionamento.
- Automatizar fluxos completos de uma aplicação web.

---


## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/PalomaMoraess/QA-Brazil_Automação_Python.git
```

### 2. Acesse a pasta do projeto

```bash
cd QA-Brazil_Automação_Python
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute os testes

```bash
pytest
```
