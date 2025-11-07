# Arquivo: tela_login_usuario.py

import tkinter as tk
from tkinter import Toplevel
from config_estilos_telas import *
import gerenciador_usuarios
import tela_menu_usuario

def criar_tela_login(janela_pai):
    janela_login = Toplevel(janela_pai)
    janela_login.title("Login de Usuário")
    janela_login.geometry("400x300")
    janela_login.config(bg=COR_FUNDO)

    janela_pai.update_idletasks()
    width = janela_login.winfo_width()
    height = janela_login.winfo_height()
    x = (janela_pai.winfo_screenwidth() // 2) - (width // 2)
    y = (janela_pai.winfo_screenheight() // 2) - (height // 2)
    janela_login.geometry(f'+{x}+{y}')

    def tentar_login():
        nome = entry_usuario.get()
        senha = entry_senha.get()
        usuario_logado = gerenciador_usuarios.verificar_usuario(nome, senha)

        if usuario_logado:
            janela_login.destroy()
            tela_menu_usuario.criar_tela_menu_usuario(janela_pai, usuario_logado)
        else:
            label_status.config(text="Usuário ou senha inválidos.", fg="red")

    frame_login = tk.Frame(janela_login, bg=COR_FUNDO)
    frame_login.pack(expand=True)

    label_usuario = tk.Label(frame_login, text="Usuário:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_usuario.pack(padx=PADDING_GERAL, pady=5)
    entry_usuario = tk.Entry(frame_login, font=FONTE_PADRAO, width=30)
    entry_usuario.pack()

    label_senha = tk.Label(frame_login, text="Senha:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_senha.pack(padx=PADDING_GERAL, pady=5)
 
    entry_senha = tk.Entry(frame_login, font=FONTE_PADRAO, width=30, show="*")
    entry_senha.pack()

    btn_login = tk.Button(frame_login, text="Login", command=tentar_login, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_login.pack(pady=PADDING_GERAL)

    label_status = tk.Label(frame_login, text="", font=FONTE_PADRAO, bg=COR_FUNDO)
    label_status.pack()