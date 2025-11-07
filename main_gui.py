import tkinter as tk
from config_estilos_telas import *
import tela_login_bibliotecario
import tela_login_usuario

def criar_janela_principal():
    janela = tk.Tk()
    janela.title("Sistema da Biblioteca")
    janela.state('zoomed')
    janela.config(bg=COR_FUNDO)
    return janela

def abrir_tela_bibliotecario():
    tela_login_bibliotecario.criar_tela_login(janela_principal)

def abrir_tela_usuario():
    tela_login_usuario.criar_tela_login(janela_principal)

def sair_do_programa(janela_para_fechar):
    janela_para_fechar.destroy()

janela_principal = criar_janela_principal()

frame_topo = tk.Frame(janela_principal, bg=COR_FUNDO)

frame_topo.pack(side="top", fill="x", padx=PADDING_GERAL, pady=PADDING_GERAL, anchor="nw")


label_titulo = tk.Label(frame_topo, text="Sistema da Biblioteca",
font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_LETRA_TITULO)
label_titulo.pack(side="left")

frame_central = tk.Frame(janela_principal, bg=COR_FUNDO)
frame_central.pack(expand=True)

btn_bibliotecario = tk.Button(frame_central, text="Bibliotecário", command=abrir_tela_bibliotecario,
width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
btn_bibliotecario.pack(side="left", padx=PADDING_BOTOES)

btn_usuario = tk.Button(frame_central, text="Usuário", command=abrir_tela_usuario,
                        width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
btn_usuario.pack(side="left", padx=PADDING_BOTOES)

btn_sair = tk.Button(frame_central, text="Sair", command=janela_principal.destroy, width=LARGURA_BOTAO, font=FONTE_BOTAO, bg=COR_BOTAO_FUNDO, fg=COR_BOTAO_LETRA)
btn_sair.pack(pady=PADDING_BOTOES*2)

janela_principal.mainloop()