# Arquivo: tela_menu_bibliotecario.py

import tkinter as tk
from tkinter import Toplevel
from config_estilos_telas import *
import tela_menu_funcoes_bibliotecario 

def criar_tela_menu_bibliotecario(janela_pai):
    janela_menu = Toplevel(janela_pai)
    janela_menu.title("Menu do Bibliotecário")
    janela_menu.state('zoomed')
    janela_menu.config(bg=COR_FUNDO)

    frame_conteudo = tk.Frame(janela_menu, bg=COR_FUNDO)
    frame_conteudo.pack(expand=True)

    label_titulo = tk.Label(frame_conteudo, text="Painel do Bibliotecário", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_titulo.pack(pady=PADDING_GERAL)

    btn_add_livro = tk.Button(frame_conteudo, text="Adicionar Livro", 
                              command=lambda: tela_menu_funcoes_bibliotecario.criar_tela_adicionar_livro(janela_menu),
                              width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_add_livro.pack(pady=PADDING_BOTOES)

    btn_remover_livro = tk.Button(frame_conteudo, text="Remover Livro", 
                                  command=lambda: tela_menu_funcoes_bibliotecario.criar_tela_remover_livro(janela_menu),
                                  width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_remover_livro.pack(pady=PADDING_BOTOES)

    btn_listar_livros = tk.Button(frame_conteudo, text="Listar Todos os Livros", 
                                  command=lambda: tela_menu_funcoes_bibliotecario.criar_tela_listar_todos_livros(janela_menu),
                                  width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_listar_livros.pack(pady=PADDING_BOTOES)

    btn_add_usuario = tk.Button(frame_conteudo, text="Adicionar Novo Usuário", 
                                command=lambda: tela_menu_funcoes_bibliotecario.criar_tela_adicionar_usuario(janela_menu),
                                width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_add_usuario.pack(pady=PADDING_BOTOES)
    
    btn_listar_usuarios = tk.Button(frame_conteudo, text="Listar Usuários", 
                                    command=lambda: tela_menu_funcoes_bibliotecario.criar_tela_listar_usuarios(janela_menu),
                                    width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_listar_usuarios.pack(pady=PADDING_BOTOES)
    
    btn_voltar = tk.Button(frame_conteudo, text="Voltar", command=janela_menu.destroy, width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_voltar.pack(pady=PADDING_BOTOES*2)

    janela_menu.grab_set()