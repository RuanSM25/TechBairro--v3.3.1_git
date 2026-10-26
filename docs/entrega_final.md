# Entrega final da TechBairro

**Aluno(a):** Ruan Marques  
**Versão preparada:** 3.3.2  
**Por que esse número de versão:** a versão anterior era 3.3.1 e esta entrega consolida documentação e registro de testes, sem adicionar uma nova funcionalidade à aplicação.

| # | Item | Evidência / situação |
|---|---|---|
| 1 | A aplicação funciona: os seis casos de teste passaram | [Registro dos testes](registro_de_testes.md) — CT01 a CT06 passaram; seis testes automáticos também passaram. |
| 2 | A versão aparece na janela e é a mesma do CHANGELOG e do README | `techbairro.py` usa `VERSAO = "3.3.2"`; README e CHANGELOG registram 3.3.2. A janela foi verificada no teste automatizado da interface. |
| 3 | O pacote foi testado numa pasta limpa | `dist/TechBairro-3.3.2.zip` foi gerado e testado em uma pasta isolada. O teste confirmou versão 3.3.2, contador inicial em 0 e criação de `techbairro.db` somente dentro da pasta extraída. |
| 4 | Tag e release publicadas no GitHub, com o ZIP anexado | **Pendente de publicação no site do GitHub.** Depois de criar a tag `v3.3.2`, publicar a release `TechBairro 3.3.2` e anexar `TechBairro-3.3.2.zip`, substituir esta nota pelo link da release. Página para publicar: https://github.com/RuanSM25/techbairro/releases/new?tag=v3.3.2 |
| 5 | O repositório não tem banco, __pycache__ nem dist | Conferido na árvore do GitHub após o commit: não há arquivos `.db`, pasta `__pycache__`, pasta `dist` ou arquivos `.pyc` versionados. O `.gitignore` também inclui regras para esses itens. |
| 6 | O histórico tem commits com mensagens claras | https://github.com/RuanSM25/techbairro/commits/main |
| 7 | README, manual de uso e requirements.txt estão no repositório | [README](../README.md) · [Manual de uso](manual_de_uso.md) · [requirements.txt](../requirements.txt) |
| 8 | A Issue “Teste do README” (Aula 26) está fechada | https://github.com/RuanSM25/techbairro/issues/1 |

## Roteiro da apresentação (até 3 minutos)

| Bloco | Tempo | O que mostrar ou dizer |
|---|---:|---|
| 1. Problema e solução | 30 s | “A TechBairro ajuda uma associação de moradores a cadastrar e organizar os dados dos clientes. A versão apresentada é a 3.3.2.” |
| 2. Demonstração ao vivo | 1 min 30 s | Com dados fictícios: cadastrar um cliente; consultar; editar o telefone e salvar; demonstrar uma tentativa de salvar telefone com espaços; consultar novamente e excluir, respondendo primeiro Não e depois Sim. |
| 3. Como foi construída | 30 s | “A interface usa Tkinter, os dados são salvos em SQLite e o código foi separado em módulos: tela, modelo de cliente, banco e validação. Git registra as alterações e GitHub hospeda o repositório e a release.” |
| 4. Aprendizado | 30 s | “Uma dificuldade foi garantir que editar e excluir afetassem o cliente correto. O sistema usa o identificador do cliente e verifica se a operação realmente alterou um registro. Isso ajuda a evitar mensagens de sucesso incorretas.” |

### Plano B

Se o programa não abrir na sala, abrir o repositório e a release no GitHub e mostrar a imagem `docs/img/tela_principal.png`. Explicar que a captura é apenas uma alternativa visual e que a demonstração planejada é ao vivo.

## Autoavaliação (preencher depois da apresentação)

- O que funcionou bem na minha apresentação: **preencher após apresentar**.
- O que eu mudaria na próxima apresentação: **preencher após apresentar**.
- Comentário de colega que foi mais útil: **preencher depois de receber a ficha de avaliação**.

## Nota sobre o teste

Os seis casos foram executados com os callbacks reais da interface em ambiente gráfico virtual (Linux, Python 3.13.5, Tkinter 8.6). As confirmações “Não” e “Sim” foram simuladas pelo teste para validar os dois caminhos sem depender de cliques manuais. Antes da apresentação, abra o pacote no computador da sala para confirmar o funcionamento naquele ambiente.
