# CHANGELOG — TechBairro

## v3.3.2 (Aula 27)

### Adicionado
- README com requisitos, instalação e configuração do banco.
- Arquivo requirements.txt com explicação das dependências.
- Manual de uso em docs/manual_de_uso.md.
- Registro dos seis testes da avaliação final em docs/registro_de_testes.md.
- Registro de entrega e roteiro de apresentação em docs/entrega_final.md.

### Conferido
- Os seis casos funcionais passaram no ambiente de teste descrito em docs/registro_de_testes.md.
- Os seis testes automáticos de validação passaram.

## v3.3.1 (Aula 21)

### Alterado
- Projeto reorganizado em quatro módulos: techbairro.py (tela), cliente.py (modelo), banco.py (dados) e validacao.py (regras).
- Validações do cadastro transferidas para ValidadorCliente, mantendo as mesmas mensagens e a ordem das verificações da versão 3.3.0.
- Importações ajustadas para a nova organização, sem alteração intencional no comportamento da interface.

### Adicionado
- testar_validacao.py com seis testes automáticos independentes da janela e do banco.
- Desafio extra: scripts/importar_planilha_antiga.py importa CSV usando Cliente, ValidadorCliente e GerenciadorClientes, com planilha_exemplo.csv para demonstração.


## v3.3.0 (Aula 20)

### Adicionado
- Botão **Salvar edição** quando um cliente está sendo editado.
- Mensagens diferentes ao cancelar uma edição e ao limpar um formulário.
- Duplo clique sobre um cliente na Consulta para editar.
- **Desafio extra:** tecla Delete para excluir o cliente selecionado, com confirmação mostrando nome, telefone e e-mail.

### Corrigido
- Edição e exclusão passam a usar o cliente realmente mostrado e selecionado na Consulta, mesmo com outras janelas abertas.
- Linhas de aviso, como **Nenhum cliente cadastrado**, não podem ser editadas ou excluídas.
- O sistema verifica se o UPDATE alterou um registro antes de informar sucesso.
- O sistema verifica se o DELETE removeu um registro e atualiza a lista quando o cliente já havia sido excluído.

## v3.2.1 (Aula 18)
### Alterado
- O número da versão passou a ficar em um único lugar no arquivo techbairro.py.

### Adicionado
- Script scripts/gerar_pacote.py, que gera o pacote da versão sem incluir o banco de dados e arquivos gerados pelo Python.
- Arquivo COMO_EXECUTAR.txt, com os requisitos e as instruções para executar a TechBairro.
