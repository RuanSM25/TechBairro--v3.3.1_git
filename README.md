# TechBairro

A TechBairro é um programa de computador para cadastrar, consultar, alterar e excluir clientes da associação de moradores. A ideia é facilitar o trabalho da pessoa que atende na secretaria.

**Versão atual:** 3.3.2 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastrar clientes com nome, telefone, e-mail e endereço.
- Consultar, alterar e excluir clientes cadastrados, com avisos de preenchimento e confirmação de exclusão.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows, macOS ou Linux com ambiente gráfico. |
| Python | Python 3; versão conferida no ambiente de preparação: **3.13.5**. |
| Tkinter | Necessário para abrir as janelas. No Ubuntu/Debian, se faltar, instale com `sudo apt install python3-tk`. |
| Bibliotecas externas | Nenhuma. O arquivo [requirements.txt](requirements.txt) registra isso e cita os módulos usados. |
| Internet | Necessária para baixar o projeto. Depois do download, o programa funciona sem internet. |

## Instalação

Use uma das opções para baixar o projeto.

### Opção A — Baixar com Git

1. Instale o Git e o Python 3, caso ainda não estejam instalados.
2. Abra o terminal e execute:

```bash
git clone https://github.com/RuanSM25/techbairro.git
cd techbairro
python --version
python -m tkinter
```

O comando `python --version` mostra a versão do Python. O comando `python -m tkinter` deve abrir uma pequena janela de demonstração; feche essa janela depois de conferir. Em seguida, execute:

```bash
python -m pip install -r requirements.txt
python techbairro.py
```

### Opção B — Baixar pelo botão Code / Download ZIP

1. Abra o [repositório TechBairro no GitHub](https://github.com/RuanSM25/techbairro).
2. Clique em **Code** e depois em **Download ZIP**. Extraia o arquivo.
3. Abra um terminal dentro da pasta extraída, onde está o arquivo `techbairro.py`.
4. Execute:

```bash
python --version
python -m tkinter
```

Feche a pequena janela de demonstração do Tkinter e execute:

```bash
python -m pip install -r requirements.txt
python techbairro.py
```

Se o Windows não reconhecer `python`, tente usar `py` no lugar, por exemplo `py techbairro.py` e `py -m tkinter`.

O comando de instalação lê o arquivo `requirements.txt`. Ele não instala pacotes externos porque a TechBairro usa módulos da biblioteca padrão do Python. Em algumas instalações do Linux, o Tkinter precisa ser instalado separadamente pelo sistema.

### O que deve aparecer ao abrir

Será aberta uma janela chamada **TechBairro — Cadastro de Cliente**, com os campos Nome, Telefone, E-mail e Endereço, os botões Salvar, Cancelar e Consultar e o contador de clientes. No terminal aparecerá uma linha começando com `Banco em uso:` e o caminho do arquivo `techbairro.db`.

## Configuração do banco de dados

Na primeira execução, o programa cria o arquivo `techbairro.db` na mesma pasta de `techbairro.py`, se ele ainda não existir. O arquivo guarda os cadastros realizados. Para conferir qual banco está em uso, veja no terminal a mensagem `Banco em uso:`, seguida do caminho completo.

O banco não fica no repositório porque pode conter nomes, telefones, e-mails e endereços de pessoas. Esses dados são pessoais e não devem ser publicados. O arquivo `.gitignore` contém a regra `*.db` para ajudar a evitar que arquivos de banco sejam adicionados ao Git por engano.

Para fazer uma cópia de segurança, feche o programa primeiro e copie `techbairro.db` para um local protegido. Não envie essa cópia ao GitHub nem a compartilhe com pessoas não autorizadas. Se o programa for instalado em outro computador sem esse arquivo, ele criará um banco novo e vazio.

## Como usar

O passo a passo está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

- `techbairro.py`: abre a janela e coordena as ações da tela.
- `cliente.py`: reúne os dados de cada cliente.
- `banco.py`: grava, consulta, altera e exclui os registros.
- `validacao.py`: verifica os campos obrigatórios, o telefone e o e-mail.
- `testar_validacao.py`: testa as regras de preenchimento.
- `scripts/`: contém ferramentas auxiliares.
- `docs/`: contém documentos de apoio e o manual de uso.
- `requirements.txt`: informa que não há dependências externas.
- `CHANGELOG.md`: registra as mudanças entre versões.

## Autor

Ruan Marques — estudante do Técnico em Desenvolvimento de Sistemas, Senac DF.
