# Arquivo: tela_menu_usuario.py

import tkinter as tk
from tkinter import Toplevel
from config_estilos_telas import *
from tela_menu_funcoes_usuarios import *

def criar_tela_menu_usuario(janela_pai, usuario):
    janela_menu = Toplevel(janela_pai)
    janela_menu.title("Menu do Usuário")
    janela_menu.state('zoomed')
    janela_menu.config(bg=COR_FUNDO)

    frame_conteudo = tk.Frame(janela_menu, bg=COR_FUNDO)
    frame_conteudo.pack(expand=True)

    label_bem_vindo = tk.Label(frame_conteudo, text=f"Bem-vindo, {usuario['nome']}!", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_bem_vindo.pack(pady=PADDING_GERAL*2)

    btn_listar = tk.Button(frame_conteudo, text="Listar Livros Disponíveis", 
                           command = lambda: criar_tela_listar_livros(janela_menu), 
                           width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_listar.pack(pady=PADDING_BOTOES)

    btn_emprestar = tk.Button(frame_conteudo, text="Emprestar Livro", 
                            command=lambda: criar_tela_emprestar_livro(janela_menu, usuario),
                            width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_emprestar.pack(pady=PADDING_BOTOES)

    btn_devolver = tk.Button(frame_conteudo, text="Devolver Livro", 
                             command=lambda: criar_tela_devolver_livro(janela_menu, usuario),
                             width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_devolver.pack(pady=PADDING_BOTOES)
    
    btn_meus_livros = tk.Button(frame_conteudo, text="Ver Meus Empréstimos", 
                                command=lambda: criar_tela_meus_emprestimos(janela_menu, usuario),
                                width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_meus_livros.pack(pady=PADDING_BOTOES)
    
    btn_sair = tk.Button(frame_conteudo, text="Sair", command=janela_menu.destroy, width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_sair.pack(pady=PADDING_BOTOES)

    janela_menu.grab_set()