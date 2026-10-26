# Entrega final da TechBairro

**Aluno(a):** Ruan Marques  
**Versão preparada:** 3.3.2  
**Motivo da versão:** a versão anterior era 3.3.1. Esta versão reúne documentação e registros de teste, sem acrescentar uma nova funcionalidade ao programa.

## Checklist de entrega

| # | Item | Evidência |
|---|---|---|
| 1 | A aplicação funciona: os seis casos de teste foram executados | [Registro dos testes](registro_de_testes.md), com esperado, obtido e status de CT01 a CT06. |
| 2 | A versão da janela, do CHANGELOG e do README é a mesma | [Código com VERSAO = "3.3.2"](../techbairro.py) · [CHANGELOG](../CHANGELOG.md) · [README](../README.md). |
| 3 | O pacote foi testado numa pasta limpa | [Registro de testes](registro_de_testes.md), seção “Teste do pacote em pasta limpa”. O ZIP testado é `TechBairro-3.3.2.zip`. |
| 4 | Tag e release publicadas no GitHub, com o ZIP anexado | **PENDENTE:** publicar a tag `v3.3.2` e a release `TechBairro 3.3.2`, anexando `TechBairro-3.3.2.zip`. Depois, substituir por [link da release](https://github.com/RuanSM25/techbairro/releases). |
| 5 | O repositório não tem banco, __pycache__ nem dist | Conferência da árvore do repositório: nenhum arquivo `.db`, pasta `__pycache__`, pasta `dist` ou arquivo `.pyc` versionado. O [.gitignore](../.gitignore) exclui esses itens. |
| 6 | O histórico tem commits com mensagens claras | [Histórico de commits](https://github.com/RuanSM25/techbairro/commits/main). |
| 7 | README, manual de uso e requirements.txt estão no repositório | [README](../README.md) · [Manual de uso](manual_de_uso.md) · [requirements.txt](../requirements.txt). |
| 8 | A Issue “Teste do README” (Aula 26) está fechada | [Issue #1](https://github.com/RuanSM25/techbairro/issues/1), já fechada. |
| 9 | O vídeo está publicado e o link abre sem pedir login | **PENDENTE:** publicar o vídeo e colar aqui o link: `[cole o link do vídeo]`. Testar o link numa janela anônima antes de entregar. |

## Roteiro do vídeo (até 3 minutos)

| Bloco | Tempo | O que mostrar ou dizer |
|---|---:|---|
| 1. Problema e solução | 30 s | “A TechBairro ajuda uma associação de moradores a cadastrar e organizar os dados dos clientes. Estou apresentando a versão 3.3.2.” |
| 2. Demonstração | 1 min 30 s | Com dados fictícios: cadastrar um cliente; consultar; editar o telefone e salvar; tentar salvar um telefone com espaços para mostrar a validação; consultar novamente e excluir, respondendo primeiro Não e depois Sim. |
| 3. Como foi construída | 30 s | “A interface usa Tkinter, os dados são guardados em SQLite e o código foi separado em módulos: tela, cliente, banco e validação. O Git registra as alterações e o GitHub hospeda o repositório e a release.” |
| 4. Aprendizado | 30 s | “Uma dificuldade foi garantir que a edição e a exclusão afetassem o cliente certo. O programa usa o identificador do cliente e verifica se a operação realmente aconteceu.” |

### Antes de gravar

- Use somente dados fictícios.
- Feche e-mail, WhatsApp e outras janelas pessoais e desative notificações.
- Deixe a TechBairro pronta para demonstrar as tarefas, com clientes fictícios na Consulta.
- Fale enquanto mostra as etapas. Mostrar o rosto é opcional.
- Assista ao vídeo inteiro: confira se a voz está clara, se a tela é legível e se dura até 3 minutos.
- Publique como vídeo **Não listado** no YouTube ou com acesso “Qualquer pessoa com o link” no Google Drive. Teste o link em uma janela anônima.

### Plano B

Se a aplicação não abrir durante a gravação, mostre a captura de tela `docs/img/tela_principal.png` e a página do repositório. O vídeo ainda deve explicar a solução com sua voz.

## Perguntas por escrito

### 1. Por que o arquivo techbairro.db não está no GitHub?

O arquivo `techbairro.db` pode guardar nomes, telefones, e-mails e endereços de clientes, que são dados pessoais. Por isso, ele deve ficar no computador onde o programa é usado e não deve ser publicado no repositório. O arquivo `.gitignore` contém a regra `*.db` para ajudar a evitar o envio acidental.

### 2. Qual caso de teste pegou um defeito de verdade? Qual era o defeito?

Nos testes da versão 3.2.1, foi observado um problema durante a edição: o cliente podia ser excluído em outra janela enquanto o formulário de edição continuava aberto. Ao salvar depois disso, o programa podia informar que a atualização tinha sido feita, mesmo sem existir mais um cadastro para atualizar. A correção foi verificar se o comando de atualização realmente alterou um registro e avisar quando o cliente não é encontrado.

### 3. Se o voluntário tiver somente o link do repositório, como ele instala e executa a TechBairro?

Ele abre o repositório no GitHub, clica em **Code → Download ZIP** e extrai o arquivo. Depois abre um terminal dentro da pasta extraída, confere o Python com `python --version`, verifica o Tkinter com `python -m tkinter`, executa `python -m pip install -r requirements.txt` e inicia o programa com `python techbairro.py`. No Windows, se o comando `python` não funcionar, pode tentar `py`.

## Autoavaliação (preencher depois de gravar e assistir ao vídeo)

- **O que ficou bom no meu vídeo:** [escreva o que realmente funcionou bem].
- **O que eu mudaria:** [escreva o que você melhoraria depois de assistir].
- **O que aprendi de mais importante nesta UC:** Aprendi a organizar o código em arquivos com responsabilidades diferentes, validar os dados, registrar alterações com Git e publicar o projeto e a documentação no GitHub.

## Status final

A documentação e os registros de teste estão preparados. Para concluir a entrega da Aula 27, ainda é necessário publicar a tag/release `v3.3.2`, anexar o ZIP, gravar e publicar o vídeo, inserir o link acima e preencher a autoavaliação com base no vídeo real.
