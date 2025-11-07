import json
import os

NOME_ARQUIVO = 'usuarios.json'



def carregar_usuarios():
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



def salvar_usuarios(lista_de_usuarios):
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_de_usuarios, arquivo, indent=4)



def adicionar_usuario(nome, senha):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario['nome'].lower() == nome.lower():
            # Em vez de print, retorna a mensagem de erro
            return False, f"Erro: O nome de usuário '{nome}' já existe."

    if usuarios:
        novo_id = max(u['id'] for u in usuarios) + 1
    else:
        novo_id = 1
    
    novo_usuario = {
        'id': novo_id,
        'nome': nome,
        'senha': senha
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    return True, f"Usuário '{nome}' criado com sucesso!"



def verificar_usuario(nome, senha):
    usuarios = carregar_usuarios()
    print(usuarios)
    for usuario in usuarios:
        if usuario['nome'].lower() == nome.lower() and usuario['senha'] == senha:
            return usuario
    return None