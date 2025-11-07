# Arquivo: tela_menu_funcoes.py (VERSÃO COM BOTÕES DE FECHAR)

import tkinter as tk
from tkinter import Toplevel
from config_estilos_telas import *
import bibliotecario
from datetime import date, timedelta

def criar_tela_listar_livros(janela_pai):
    janela_lista = Toplevel(janela_pai)
    janela_lista.title("Livros Disponíveis")
    janela_lista.geometry("800x600")
    janela_lista.config(bg=COR_FUNDO)

    livros = bibliotecario.carregar_livros()
    livros_disponiveis = [livro for livro in livros if livro['status']['estado'] == 'disponivel']

    if not livros_disponiveis:
        frame_aviso = tk.Frame(janela_lista, bg=COR_FUNDO)
        frame_aviso.pack(expand=True)
        label_aviso = tk.Label(frame_aviso, text="Nenhum livro disponível no momento.", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
        label_aviso.pack(pady=PADDING_BOTOES)

        btn_voltar = tk.Button(frame_aviso, text="Voltar", command=janela_lista.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_GERAL)
    else:
        frame_lista = tk.Frame(janela_lista, bg=COR_FUNDO)
        frame_lista.pack(fill="both", expand=True, padx=PADDING_GERAL, pady=PADDING_GERAL)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")

        listbox_livros = tk.Listbox(frame_lista, font=FONTE_PADRAO, bg="#2c313a", fg=COR_LETRA_TITULO,
                                    selectbackground=COR_BOTAO_FUNDO, selectforeground=COR_BOTAO_LETRA,
                                    borderwidth=0, highlightthickness=0)
        
        listbox_livros.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_livros.yview)
        listbox_livros.pack(side="left", fill="both", expand=True)

        listbox_livros.insert(tk.END, "--- Livros Disponíveis para Empréstimo ---")
        for livro in livros_disponiveis:
            texto_livro = f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']}"
            listbox_livros.insert(tk.END, texto_livro)
        listbox_livros.insert(tk.END, "-----------------------------------------")
        
        btn_voltar = tk.Button(janela_lista, text="Voltar", command=janela_lista.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_BOTOES)

    janela_lista.grab_set()

def criar_tela_emprestar_livro(janela_pai, usuario):
    janela_emprestar = Toplevel(janela_pai)
    janela_emprestar.title("Emprestar Livro")
    janela_emprestar.geometry("400x350")
    janela_emprestar.config(bg=COR_FUNDO)

    def realizar_emprestimo():
        id_texto = entry_id_livro.get()
        try:
            id_livro = int(id_texto)
            sucesso = bibliotecario.emprestar_livro(id_livro, usuario['id'])
            if sucesso:
                data_devolucao = date.today() + timedelta(days=14)
                data_formatada = data_devolucao.strftime("%d/%m/%Y")
                msg = f"Livro ID {id_livro} emprestado!\nDevolução até {data_formatada}."
                label_status.config(text=msg, fg="green")
            else:
                label_status.config(text=f"Erro: Livro não encontrado ou já emprestado.", fg="red")
        except ValueError:
            label_status.config(text="Erro: ID inválido. Digite apenas números.", fg="red")

    frame_emprestar = tk.Frame(janela_emprestar, bg=COR_FUNDO)
    frame_emprestar.pack(expand=True, padx=PADDING_GERAL, pady=PADDING_GERAL)

    label_instrucao = tk.Label(frame_emprestar, text="Digite o ID do livro para emprestar:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_instrucao.pack(pady=PADDING_GERAL)

    entry_id_livro = tk.Entry(frame_emprestar, font=FONTE_PADRAO, width=30)
    entry_id_livro.pack()

    btn_confirmar = tk.Button(frame_emprestar, text="Confirmar Empréstimo", command=realizar_emprestimo, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_confirmar.pack(pady=PADDING_GERAL)

    btn_voltar = tk.Button(frame_emprestar, text="Voltar", command=janela_emprestar.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO-10)
    btn_voltar.pack(pady=PADDING_BOTOES)
    
    label_status = tk.Label(frame_emprestar, text="", font=FONTE_PADRAO, bg=COR_FUNDO)
    label_status.pack(pady=5)
    
    janela_emprestar.grab_set()


def criar_tela_devolver_livro(janela_pai, usuario):

    janela_devolver = Toplevel(janela_pai)
    janela_devolver.title("Devolver Livro")
    janela_devolver.geometry("800x600")
    janela_devolver.config(bg=COR_FUNDO)

    def realizar_devolucao():

        id_texto = entry_id_livro.get()
        try:
            id_livro = int(id_texto)
            sucesso = bibliotecario.devolver_livro(id_livro)
            if sucesso:
                label_status.config(text=f"Livro ID {id_livro} devolvido com sucesso!", fg="green")
            else:
                label_status.config(text=f"Erro: ID não corresponde a um livro em seu nome.", fg="red")
        except ValueError:
            label_status.config(text="Erro: ID inválido. Digite apenas números.", fg="red")

    meus_livros = bibliotecario.buscar_livros_do_usuario(usuario['id'])

    if not meus_livros:
        frame_aviso = tk.Frame(janela_devolver, bg=COR_FUNDO)
        frame_aviso.pack(expand=True)
        label_aviso = tk.Label(frame_aviso, text="Você não possui livros para devolver.", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
        label_aviso.pack(pady=PADDING_BOTOES)
        btn_voltar = tk.Button(frame_aviso, text="Voltar", command=janela_devolver.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_GERAL)
    else:
        frame_superior = tk.Frame(janela_devolver, bg=COR_FUNDO)
        frame_superior.pack(fill="x", padx=PADDING_GERAL, pady=PADDING_GERAL)
        label_meus_livros = tk.Label(frame_superior, text="Estes são os seus livros:", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
        label_meus_livros.pack(pady=5)
        listbox_livros = tk.Listbox(frame_superior, font=FONTE_PADRAO, bg="#2c313a", fg=COR_LETRA_TITULO, height=10)
        listbox_livros.pack(fill="x", pady=5)
        for livro in meus_livros:
            texto_livro = f"ID: {livro['id']} | Título: {livro['titulo']} | Devolução em: {livro['status']['data_devolucao']}"
            listbox_livros.insert(tk.END, texto_livro)

        frame_inferior = tk.Frame(janela_devolver, bg=COR_FUNDO)
        frame_inferior.pack(padx=PADDING_GERAL, pady=PADDING_GERAL)
        label_instrucao = tk.Label(frame_inferior, text="Digite o ID do livro a devolver:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
        label_instrucao.pack(pady=5)
        entry_id_livro = tk.Entry(frame_inferior, font=FONTE_PADRAO, width=30)
        entry_id_livro.pack()
        btn_confirmar = tk.Button(frame_inferior, text="Confirmar Devolução", command=realizar_devolucao, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
        btn_confirmar.pack(pady=PADDING_GERAL)

        btn_voltar = tk.Button(frame_inferior, text="Voltar", command=janela_devolver.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
        btn_voltar.pack(pady=PADDING_BOTOES)
        label_status = tk.Label(frame_inferior, text="", font=FONTE_PADRAO, bg=COR_FUNDO)
        label_status.pack()

    janela_devolver.grab_set()


def criar_tela_meus_emprestimos(janela_pai, usuario):
    janela_emprestimos = Toplevel(janela_pai)
    janela_emprestimos.title("Meus Empréstimos")
    janela_emprestimos.geometry("800x600")
    janela_emprestimos.config(bg=COR_FUNDO)

    meus_livros = bibliotecario.buscar_livros_do_usuario(usuario['id'])

    if not meus_livros:
        frame_aviso = tk.Frame(janela_emprestimos, bg=COR_FUNDO)
        frame_aviso.pack(expand=True)
        label_aviso = tk.Label(frame_aviso, text="Você não tem nenhum livro emprestado no momento.", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
        label_aviso.pack(pady=PADDING_BOTOES)

        btn_voltar = tk.Button(frame_aviso, text="Voltar", command=janela_emprestimos.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_GERAL)
    else:
        frame_lista = tk.Frame(janela_emprestimos, bg=COR_FUNDO)
        frame_lista.pack(fill="both", expand=True, padx=PADDING_GERAL, pady=PADDING_GERAL)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")

        listbox_livros = tk.Listbox(frame_lista, font=FONTE_PADRAO, bg="#2c313a", fg=COR_LETRA_TITULO,
                                    selectbackground=COR_BOTAO_FUNDO, selectforeground=COR_BOTAO_LETRA,
                                    borderwidth=0, highlightthickness=0)
        
        listbox_livros.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_livros.yview)
        listbox_livros.pack(side="left", fill="both", expand=True)

        listbox_livros.insert(tk.END, "--- Meus Empréstimos ---")
        for livro in meus_livros:
            texto_livro = f"ID: {livro['id']} | Título: {livro['titulo']} | Devolver até: {livro['status']['data_devolucao']}"
            listbox_livros.insert(tk.END, texto_livro)
        listbox_livros.insert(tk.END, "------------------------")
        
        btn_voltar = tk.Button(janela_emprestimos, text="Voltar", command=janela_emprestimos.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_BOTOES)

    janela_emprestimos.grab_set()