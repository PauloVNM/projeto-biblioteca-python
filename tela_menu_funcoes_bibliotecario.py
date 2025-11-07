# Arquivo: tela_menu_funcoes_bibliotecario.py

import tkinter as tk
from tkinter import Toplevel
from config_estilos_telas import *
import bibliotecario
import gerenciador_usuarios

def criar_tela_adicionar_livro(janela_pai):
    janela_adicionar = Toplevel(janela_pai)
    janela_adicionar.title("Adicionar Novo Livro")
    janela_adicionar.geometry("400x400")
    janela_adicionar.config(bg=COR_FUNDO)

    def realizar_adicao():
        titulo = entry_titulo.get()
        autor = entry_autor.get()

        if titulo and autor:
            bibliotecario.adicionar_livro(titulo, autor)
            label_status.config(text=f"Livro '{titulo}' adicionado!", fg="green")

            entry_titulo.delete(0, tk.END)
            entry_autor.delete(0, tk.END)
            entry_titulo.focus_set()
        else:
            label_status.config(text="Erro: Título e Autor são obrigatórios.", fg="red")

    # --- Widgets ---
    frame_adicionar = tk.Frame(janela_adicionar, bg=COR_FUNDO)
    frame_adicionar.pack(expand=True, padx=PADDING_GERAL, pady=PADDING_GERAL)

    label_titulo = tk.Label(frame_adicionar, text="Título do Livro:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_titulo.pack(pady=5)
    entry_titulo = tk.Entry(frame_adicionar, font=FONTE_PADRAO, width=40)
    entry_titulo.pack()

    label_autor = tk.Label(frame_adicionar, text="Autor do Livro:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_autor.pack(pady=5)
    entry_autor = tk.Entry(frame_adicionar, font=FONTE_PADRAO, width=40)
    entry_autor.pack()

    btn_confirmar = tk.Button(frame_adicionar, text="Adicionar Livro", command=realizar_adicao, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_confirmar.pack(pady=PADDING_GERAL)

    label_status = tk.Label(frame_adicionar, text="", font=FONTE_PADRAO, bg=COR_FUNDO)
    label_status.pack(pady=5)

    btn_voltar = tk.Button(frame_adicionar, text="Voltar", command=janela_adicionar.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO-10)
    btn_voltar.pack(pady=PADDING_BOTOES)

    janela_adicionar.grab_set()

def criar_tela_remover_livro(janela_pai):
    janela_remover = Toplevel(janela_pai)
    janela_remover.title("Remover Livro")
    janela_remover.geometry("400x300")
    janela_remover.config(bg=COR_FUNDO)

  
    def realizar_remocao():
        id_texto = entry_id_livro.get()
        try:
            id_remover = int(id_texto)
            sucesso = bibliotecario.remover_livro(id_remover)

            if sucesso:
                label_status.config(text=f"Livro ID {id_remover} removido com sucesso!", fg="green")
                entry_id_livro.delete(0, tk.END)
            else:
                label_status.config(text=f"Erro: Livro com ID {id_remover} não encontrado.", fg="red")

        except ValueError:
            label_status.config(text="Erro: ID inválido. Digite apenas números.", fg="red")

  
    frame_remover = tk.Frame(janela_remover, bg=COR_FUNDO)
    frame_remover.pack(expand=True, padx=PADDING_GERAL, pady=PADDING_GERAL)

    label_instrucao = tk.Label(frame_remover, text="Digite o ID do livro a ser removido:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_instrucao.pack(pady=5)

    entry_id_livro = tk.Entry(frame_remover, font=FONTE_PADRAO, width=30)
    entry_id_livro.pack()

    btn_confirmar = tk.Button(frame_remover, text="Remover Livro", command=realizar_remocao, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_confirmar.pack(pady=PADDING_GERAL)

    label_status = tk.Label(frame_remover, text="", font=FONTE_PADRAO, bg=COR_FUNDO)
    label_status.pack(pady=5)

    btn_voltar = tk.Button(frame_remover, text="Voltar", command=janela_remover.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO-10)
    btn_voltar.pack(pady=PADDING_BOTOES)

    janela_remover.grab_set()


def criar_tela_listar_todos_livros(janela_pai):
    janela_lista_completa = Toplevel(janela_pai)
    janela_lista_completa.title("Lista Completa de Livros")
    janela_lista_completa.geometry("1000x600")
    janela_lista_completa.config(bg=COR_FUNDO)

    livros = bibliotecario.carregar_livros()

    if not livros:
        frame_aviso = tk.Frame(janela_lista_completa, bg=COR_FUNDO)
        frame_aviso.pack(expand=True)
        label_aviso = tk.Label(frame_aviso, text="Não há livros cadastrados na biblioteca.", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
        label_aviso.pack(pady=PADDING_BOTOES)
        btn_voltar = tk.Button(frame_aviso, text="Voltar", command=janela_lista_completa.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_GERAL)
    else:
        frame_lista = tk.Frame(janela_lista_completa, bg=COR_FUNDO)
        frame_lista.pack(fill="both", expand=True, padx=PADDING_GERAL, pady=PADDING_GERAL)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")

        listbox_livros = tk.Listbox(frame_lista, font=FONTE_PADRAO, bg="#2c313a", fg=COR_LETRA_TITULO,
                                    selectbackground=COR_BOTAO_FUNDO, selectforeground=COR_BOTAO_LETRA,
                                    borderwidth=0, highlightthickness=0)
        
        listbox_livros.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_livros.yview)
        listbox_livros.pack(side="left", fill="both", expand=True)

        listbox_livros.insert(tk.END, "--- Lista Completa de Livros ---")
        for livro in livros:
            status_info = livro['status']
            estado = status_info['estado']
            info = f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Status: {estado}"
            if estado == 'emprestado':
                info += f" (Emprestado para ID: {status_info['emprestado_para_id']}, Devolução: {status_info['data_devolucao']})"
            
            listbox_livros.insert(tk.END, info)
        listbox_livros.insert(tk.END, "---------------------------------")
        
        btn_voltar = tk.Button(janela_lista_completa, text="Voltar", command=janela_lista_completa.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_BOTOES)

    janela_lista_completa.grab_set()


def criar_tela_listar_todos_livros(janela_pai):
    janela_lista_completa = Toplevel(janela_pai)
    janela_lista_completa.title("Lista Completa de Livros")
    janela_lista_completa.geometry("1000x600")
    janela_lista_completa.config(bg=COR_FUNDO)

    livros = bibliotecario.carregar_livros()

    if not livros:
        frame_aviso = tk.Frame(janela_lista_completa, bg=COR_FUNDO)
        frame_aviso.pack(expand=True)
        label_aviso = tk.Label(frame_aviso, text="Não há livros cadastrados na biblioteca.", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
        label_aviso.pack(pady=PADDING_BOTOES)
        btn_voltar = tk.Button(frame_aviso, text="Voltar", command=janela_lista_completa.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_GERAL)
    else:
        frame_lista = tk.Frame(janela_lista_completa, bg=COR_FUNDO)
        frame_lista.pack(fill="both", expand=True, padx=PADDING_GERAL, pady=PADDING_GERAL)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")

        listbox_livros = tk.Listbox(frame_lista, font=FONTE_PADRAO, bg="#2c313a", fg=COR_LETRA_TITULO,
                                    selectbackground=COR_BOTAO_FUNDO, selectforeground=COR_BOTAO_LETRA,
                                    borderwidth=0, highlightthickness=0)
        
        listbox_livros.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_livros.yview)
        listbox_livros.pack(side="left", fill="both", expand=True)

        listbox_livros.insert(tk.END, "--- Lista Completa de Livros ---")
        for livro in livros:
            status_info = livro['status']
            estado = status_info['estado']
            info = f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Status: {estado}"
            if estado == 'emprestado':
                info += f" (Emprestado para ID: {status_info['emprestado_para_id']}, Devolução: {status_info['data_devolucao']})"
            
            listbox_livros.insert(tk.END, info)
        listbox_livros.insert(tk.END, "---------------------------------")
        
        btn_voltar = tk.Button(janela_lista_completa, text="Voltar", command=janela_lista_completa.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_BOTOES)

    janela_lista_completa.grab_set()

def criar_tela_adicionar_usuario(janela_pai):
    janela_add_user = Toplevel(janela_pai)
    janela_add_user.title("Adicionar Novo Usuário")
    janela_add_user.geometry("400x400")
    janela_add_user.config(bg=COR_FUNDO)

    def realizar_cadastro():
        nome = entry_nome.get()
        senha = entry_senha.get()

        if nome and senha:
       
            sucesso, mensagem = gerenciador_usuarios.adicionar_usuario(nome, senha)
            
            cor = "green" if sucesso else "red"
            label_status.config(text=mensagem, fg=cor)

            if sucesso:
                entry_nome.delete(0, tk.END)
                entry_senha.delete(0, tk.END)
                entry_nome.focus_set()
        else:
            label_status.config(text="Erro: Nome e Senha são obrigatórios.", fg="red")


    frame_add_user = tk.Frame(janela_add_user, bg=COR_FUNDO)
    frame_add_user.pack(expand=True, padx=PADDING_GERAL, pady=PADDING_GERAL)

    label_nome = tk.Label(frame_add_user, text="Nome do Usuário:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_nome.pack(pady=5)
    entry_nome = tk.Entry(frame_add_user, font=FONTE_PADRAO, width=40)
    entry_nome.pack()

    label_senha = tk.Label(frame_add_user, text="Senha:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_senha.pack(pady=5)
    entry_senha = tk.Entry(frame_add_user, font=FONTE_PADRAO, width=40, show="*")
    entry_senha.pack()

    btn_confirmar = tk.Button(frame_add_user, text="Adicionar Usuário", command=realizar_cadastro, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_confirmar.pack(pady=PADDING_GERAL)

    label_status = tk.Label(frame_add_user, text="", font=FONTE_PADRAO, bg=COR_FUNDO)
    label_status.pack(pady=5)

    btn_voltar = tk.Button(frame_add_user, text="Voltar", command=janela_add_user.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO-10)
    btn_voltar.pack(pady=PADDING_BOTOES)

    janela_add_user.grab_set()

def criar_tela_listar_usuarios(janela_pai):
    janela_lista_usr = Toplevel(janela_pai)
    janela_lista_usr.title("Lista de Usuários Cadastrados")
    janela_lista_usr.geometry("800x600")
    janela_lista_usr.config(bg=COR_FUNDO)

    usuarios = gerenciador_usuarios.carregar_usuarios()

    if not usuarios:
        frame_aviso = tk.Frame(janela_lista_usr, bg=COR_FUNDO)
        frame_aviso.pack(expand=True)
        label_aviso = tk.Label(frame_aviso, text="Não há usuários cadastrados no sistema.", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
        label_aviso.pack(pady=PADDING_BOTOES)
        btn_voltar = tk.Button(frame_aviso, text="Voltar", command=janela_lista_usr.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_GERAL)
    else:
        frame_lista = tk.Frame(janela_lista_usr, bg=COR_FUNDO)
        frame_lista.pack(fill="both", expand=True, padx=PADDING_GERAL, pady=PADDING_GERAL)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")

        listbox_usuarios = tk.Listbox(frame_lista, font=FONTE_PADRAO, bg="#2c313a", fg=COR_LETRA_TITULO,
                                    selectbackground=COR_BOTAO_FUNDO, selectforeground=COR_BOTAO_LETRA,
                                    borderwidth=0, highlightthickness=0)
        
        listbox_usuarios.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_usuarios.yview)
        listbox_usuarios.pack(side="left", fill="both", expand=True)

        listbox_usuarios.insert(tk.END, "--- Lista de Usuários ---")
        for usuario in usuarios:
            # A regra de ouro: NUNCA mostrar a senha.
            info_usuario = f"ID: {usuario['id']} | Nome: {usuario['nome']}"
            listbox_usuarios.insert(tk.END, info_usuario)
        listbox_usuarios.insert(tk.END, "-------------------------")
        
        btn_voltar = tk.Button(janela_lista_usr, text="Voltar", command=janela_lista_usr.destroy, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA, width=LARGURA_BOTAO)
        btn_voltar.pack(pady=PADDING_BOTOES)

    janela_lista_usr.grab_set()