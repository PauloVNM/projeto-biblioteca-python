import json
import os
import datetime

NOME_ARQUIVO = 'livrosTest.json'

def carregar_livros():
    if not os.path.exists(NOME_ARQUIVO):
        return []
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        try:
            if os.path.getsize(NOME_ARQUIVO) > 0:
                return json.load(arquivo)
            else:
                return []
        except json.JSONDecodeError:
            return []

def salvar_livros(lista_de_livros):
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_de_livros, arquivo, indent=4)

def adicionar_livro(titulo, autor):
    livros = carregar_livros()
    novo_id = max(livro['id'] for livro in livros) + 1 if livros else 1
    novo_livro = {
        'id': novo_id, 'titulo': titulo, 'autor': autor,
        'status': {
            "estado": "disponivel", "emprestado_para_id": None,
            "data_emprestimo": None, "data_devolucao": None
        }
    }
    livros.append(novo_livro)
    salvar_livros(livros)
    print(f"Livro '{titulo}' (ID: {novo_id}) adicionado com sucesso!")

def buscar_livro_por_id(id_do_livro):
    for livro in carregar_livros():
        if livro['id'] == id_do_livro:
            return livro
    return None

def emprestar_livro(livro_id, usuario_id):
    livros = carregar_livros()
    livro_encontrado = False
    for livro in livros:
        if livro['id'] == livro_id and livro['status']['estado'] == 'disponivel':
            hoje = datetime.date.today()
            data_devolucao = hoje + datetime.timedelta(days=14)
            
            livro['status']['estado'] = 'emprestado'
            livro['status']['emprestado_para_id'] = usuario_id
            livro['status']['data_emprestimo'] = hoje.strftime('%Y-%m-%d')
            livro['status']['data_devolucao'] = data_devolucao.strftime('%Y-%m-%d')
            
            livro_encontrado = True
            break
            
    if livro_encontrado:
        salvar_livros(livros)
        return True
    return False

def devolver_livro(livro_id):
    livros = carregar_livros()
    livro_encontrado = False
    for livro in livros:
        if livro['id'] == livro_id and livro['status']['estado'] == 'emprestado':
            livro['status']['estado'] = 'disponivel'
            livro['status']['emprestado_para_id'] = None
            livro['status']['data_emprestimo'] = None
            livro['status']['data_devolucao'] = None
            livro_encontrado = True
            break
            
    if livro_encontrado:
        salvar_livros(livros)
        return True
    return False

def buscar_livros_do_usuario(usuario_id):
    livros = carregar_livros()
    livros_do_usuario = [livro for livro in livros if livro['status']['emprestado_para_id'] == usuario_id]
    return livros_do_usuario