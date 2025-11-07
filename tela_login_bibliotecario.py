# Arquivo: tela_login_bibliotecario.py

import tkinter as tk
from tkinter import Toplevel
from config_estilos_telas import *
import tela_menu_bibliotecario

SENHA_MESTRA = "1234"

def criar_tela_login(janela_pai):
    janela_login = Toplevel(janela_pai)
    janela_login.title("bibliotecario")
    janela_login.geometry("300x200")
    janela_login.config(bg=COR_FUNDO)

    janela_pai.update_idletasks()
    width = janela_login.winfo_width()
    height = janela_login.winfo_height()
    x = (janela_pai.winfo_screenwidth() // 2) - (width // 2)
    y = (janela_pai.winfo_screenheight() // 2) - (height // 2)
    janela_login.geometry(f'+{x}+{y}')

    def tentar_login():
        senha = entry_senha.get()
        
        if senha == SENHA_MESTRA:
            janela_login.destroy()
            tela_menu_bibliotecario.criar_tela_menu_bibliotecario(janela_pai) # Abre o menu

        else:
            label_status.config(text="senha inválida.", fg="red")
        
    frame_login = tk.Frame(janela_login, bg=COR_FUNDO)
    frame_login.pack(expand=True)

    label_senha = tk.Label(frame_login, text="Senha:", font=FONTE_PADRAO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
    label_senha.pack(padx=PADDING_GERAL, pady=5)
 
    entry_senha = tk.Entry(frame_login, font=FONTE_PADRAO, width=30, show="*")
    entry_senha.pack()

    btn_login = tk.Button(frame_login, text="Login", command=tentar_login, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
    btn_login.pack(pady=PADDING_GERAL)

    label_status = tk.Label(frame_login, text="", font=FONTE_PADRAO, bg=COR_FUNDO)
    label_status.pack()