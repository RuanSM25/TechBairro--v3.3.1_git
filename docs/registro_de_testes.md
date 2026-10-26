# Registro de testes da TechBairro

**Versão testada:** 3.3.2  
**Data:** 26/10/2026  
**Responsável:** Ruan Marques  
**Ambiente de teste:** Linux, Python 3.13.5, Tkinter 8.6, interface executada com display virtual Xvfb. Os testes da interface chamaram os comandos reais da aplicação; as respostas dos diálogos de confirmação foram controladas pelo teste para verificar os caminhos “Não” e “Sim”.

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar Ana Silva com telefone `61999990001`, e-mail `ana@email.com` e endereço fictício `Rua Fictícia 123`. | O cadastro é salvo, a mensagem de sucesso aparece e o contador passa a 1. | `Cliente 'Ana Silva' salvo com sucesso!`; total de clientes: 1. | Passou |
| CT02 | RF01 | Deixar Nome e Endereço vazios, preencher Telefone e E-mail e clicar em Salvar. | O programa informa que os campos Nome e Endereço precisam ser preenchidos. | `Preencha o(s) campo(s): Nome, Endereço` | Passou |
| CT03 | RF02 | Preencher os demais campos corretamente e usar telefone `61 9999 0000`. | O programa rejeita o telefone com espaços. | `Telefone inválido: use somente números.` | Passou |
| CT04 | RF03 | Preencher os demais campos corretamente e usar e-mail `ana@email`. | O programa rejeita o e-mail sem ponto no domínio. | `E-mail inválido: use o formato nome@dominio.com` | Passou |
| CT05 | RF05 | Consultar Ana Silva, selecionar Editar selecionado, trocar o telefone para `61988880002` e salvar a edição. | O programa informa sucesso e o telefone novo fica gravado. | `Cliente 'Ana Silva' atualizado com sucesso!`; telefone consultado no banco: `61988880002`. | Passou |
| CT06 | RF06 | Selecionar Ana Silva para exclusão, responder Não; repetir e responder Sim. | Com Não, o cliente permanece; com Sim, o cadastro é removido. | Depois de Não: 1 cliente permaneceu. Depois de Sim: 0 clientes; mensagem `Cliente 'Ana Silva' excluído com sucesso!`. | Passou |

## Testes automáticos

**Comando executado:** `python testar_validacao.py`

**Saída obtida:**

```text
OK teste_cliente_valido
OK teste_endereco_vazio
OK teste_telefone_com_letras
OK teste_email_sem_ponto
OK teste_nome_e_telefone_vazios
OK teste_email_sem_usuario
Todos os testes passaram.
```

**Resultado:** 6 de 6 testes automáticos passaram.

**Dependências:** `python -m pip install -r requirements.txt` terminou sem instalar pacotes externos nem apresentar erro de instalação.

## Defeitos encontrados

Nenhum defeito foi identificado nos seis casos funcionais e nos seis testes automáticos executados no ambiente indicado acima. A demonstração usa dados fictícios e um banco temporário. Como o teste automatizado da interface foi feito em Linux com display virtual, recomenda-se também abrir o pacote final no computador Windows que será usado na apresentação, caso seja esse o ambiente da sala.
