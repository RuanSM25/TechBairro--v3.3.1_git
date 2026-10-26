# TechBairro - Cadastro de Clientes
import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente

VERSAO = "3.3.2"
# ============================================================
# CLASSES E BANCO DE DADOS
# ============================================================
# ============================================================
# JANELA PRINCIPAL
# ============================================================
janela = tk.Tk()
janela.title("TechBairro — Cadastro de Cliente")
janela.geometry("480x460")
janela.resizable(False, False)
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
print(f"Banco em uso: {CAMINHO_BANCO}")
gerenciador = GerenciadorClientes(CAMINHO_BANCO)
validador = ValidadorCliente()
id_em_edicao = None

cabecalho = tk.Frame(janela, bg="#2c3e50")
cabecalho.pack(side="top", fill="x")
tk.Label(cabecalho, text="Cadastro de Cliente", fg="white", bg="#2c3e50",
         font=("Arial", 14, "bold"), pady=12).pack()

form = tk.Frame(janela)
form.pack(pady=20)
campos = ["Nome", "Telefone", "E-mail", "Endereço"]
entradas = {}
for i, campo in enumerate(campos):
    tk.Label(form, text=f"{campo}:").grid(row=i, column=0, sticky="e", padx=5, pady=6)
    entrada = tk.Entry(form, width=30)
    entrada.grid(row=i, column=1, padx=5, pady=6)
    entradas[campo] = entrada

status = tk.Label(janela, text="Nenhum cliente cadastrado ainda", fg="gray",
                  wraplength=440, justify="left")
status.pack(pady=(0, 5))
contador = tk.Label(janela, text=f"Clientes cadastrados: {gerenciador.total()}")
contador.pack()


def atualizar_contador():
    contador.config(text=f"Clientes cadastrados: {gerenciador.total()}")


def limpar_campos():
    global id_em_edicao
    for entrada in entradas.values():
        entrada.delete(0, tk.END)
    id_em_edicao = None
    # Volta ao modo de cadastro.
    botao_salvar.config(text="Salvar")


def salvar():
    global id_em_edicao
    valores = {campo: entradas[campo].get().strip() for campo in campos}
    cliente = Cliente(valores["Nome"], valores["Telefone"],
                      valores["E-mail"], valores["Endereço"])
    # As regras de cadastro agora ficam na classe ValidadorCliente.
    erro = validador.validar(cliente)
    if erro is not None:
        status.config(text=erro, fg="red")
        return

    try:
        if id_em_edicao is None:
            gerenciador.adicionar(cliente)
            status.config(text=f"Cliente '{cliente.nome}' salvo com sucesso!", fg="green")
        else:
            # Verifica a resposta do UPDATE.
            alterou = gerenciador.atualizar(id_em_edicao, cliente)
            if not alterou:
                status.config(text="Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.",
                              fg="red")
                limpar_campos()
                atualizar_contador()
                return
            status.config(text=f"Cliente '{cliente.nome}' atualizado com sucesso!", fg="green")
    except sqlite3.Error as erro:
        status.config(text=f"Erro ao salvar no banco: {erro}", fg="red")
        return
    atualizar_contador()
    limpar_campos()


def cancelar():
    # Verifica antes de limpar, pois limpar zera o id.
    estava_editando = id_em_edicao is not None
    limpar_campos()
    if estava_editando:
        status.config(text="Edição cancelada. Nada foi alterado.", fg="gray")
    else:
        status.config(text="Formulário limpo", fg="gray")


def abrir_consulta():
    consulta = tk.Toplevel(janela)
    consulta.title("Consulta de Clientes")
    consulta.geometry("500x380")
    consulta.resizable(False, False)

    lista = tk.Listbox(consulta, width=65, height=12)
    lista.pack(padx=10, pady=10)
    scrollbar = tk.Scrollbar(consulta)
    scrollbar.pack(side="right", fill="y", pady=10)
    lista.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lista.yview)

    # Guarda exatamente os clientes exibidos na Listbox.
    clientes_na_tela = []

    def atualizar_lista():
        lista.delete(0, tk.END)
        # As duas listas permanecem na mesma ordem.
        clientes_na_tela.clear()
        try:
            clientes_cadastrados = gerenciador.listar()
        except sqlite3.Error as erro:
            lista.insert(tk.END, f"Erro ao ler o banco: {erro}")
            return
        if not clientes_cadastrados:
            lista.insert(tk.END, "Nenhum cliente cadastrado")
            return
        for cliente in clientes_cadastrados:
            lista.insert(tk.END, cliente.resumo())
            clientes_na_tela.append(cliente)

    # Posição só pode apontar para um cliente da tela.
    def cliente_selecionado(acao):
        selecionado = lista.curselection()
        if not selecionado or selecionado[0] >= len(clientes_na_tela):
            messagebox.showwarning("Atenção", f"Selecione um cliente antes de {acao}.", parent=consulta)
            return None
        return clientes_na_tela[selecionado[0]]

    def editar_cliente():
        global id_em_edicao
        # Não consulta novamente por índice.
        cliente = cliente_selecionado("editar")
        if cliente is None:
            return
        id_em_edicao = cliente.id
        for campo, valor in (("Nome", cliente.nome), ("Telefone", cliente.telefone),
                             ("E-mail", cliente.email), ("Endereço", cliente.endereco)):
            entradas[campo].delete(0, tk.END)
            entradas[campo].insert(0, valor)
        status.config(text=f"Editando cliente: {cliente.nome}", fg="blue")
        # Modo de edição visível.
        botao_salvar.config(text="Salvar edição")
        consulta.destroy()

    def excluir_cliente():
        cliente = cliente_selecionado("excluir")
        if cliente is None:
            return
        # Exibe telefone e e-mail.
        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja excluir o cadastro de {cliente.nome}?\n"
            f"Telefone: {cliente.telefone}\nE-mail: {cliente.email}\n\n"
            "Essa ação não pode ser desfeita.", parent=consulta
        )
        if not confirmar:
            return
        try:
            # Confere se DELETE removeu uma linha.
            removeu = gerenciador.remover(cliente.id)
        except sqlite3.Error as erro:
            messagebox.showerror("Erro no banco", f"Não foi possível excluir o cliente.\n{erro}", parent=consulta)
            return
        if not removeu:
            # Cliente já foi removido por outra consulta.
            messagebox.showwarning("Cliente não encontrado",
                                   f"{cliente.nome} já não está mais no banco.\nA lista será atualizada.",
                                   parent=consulta)
            atualizar_lista()
            atualizar_contador()
            return
        atualizar_lista()
        atualizar_contador()
        status.config(text=f"Cliente '{cliente.nome}' excluído com sucesso!", fg="green")

    botoes_consulta = tk.Frame(consulta)
    botoes_consulta.pack(pady=10)

    tk.Button(botoes_consulta, text="Editar selecionado", width=18,
              command=editar_cliente).grid(row=0, column=0, padx=5)
    
    tk.Button(botoes_consulta, text="Excluir selecionado", width=18,
              command=excluir_cliente).grid(row=0, column=1, padx=5)

    # Duplo clique edita o cliente selecionado.
    lista.bind("<Double-Button-1>", lambda evento: editar_cliente())
    # Tecla Delete usa a mesma confirmação do botão.
    lista.bind("<Delete>", lambda evento: excluir_cliente())
    atualizar_lista()
    return consulta


# ============================================================
# BOTÕES E VERSÃO
# ============================================================
botoes = tk.Frame(janela)
botoes.pack(pady=10)
# Não coloca grid() na mesma linha da criação.
botao_salvar = tk.Button(botoes, text="Salvar", width=13, command=salvar)
botao_salvar.grid(row=0, column=0, padx=5)

tk.Button(botoes, text="Cancelar", width=12, command=cancelar).grid(row=0, column=1, padx=5)
tk.Button(botoes, text="Consultar", width=12, command=abrir_consulta).grid(row=0, column=2, padx=5)
tk.Label(janela, text=f"v{VERSAO}", fg="gray").place(relx=0.97, rely=0.97, anchor="se")

janela.mainloop()
