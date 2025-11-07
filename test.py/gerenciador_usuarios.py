import json
import os


NOME_ARQUIVO = 'usuarios.json' #<------- 1
# A variável com o nome do arquivo, para não termos que repetir o nome em todo lugar.

def salvar_usuarios(lista_de_usuarios): #<------- 2

    # 2
    #Recebe uma lista COMPLETA de usuários (em formato de dicionários Python)
    #e a salva no arquivo JSON, substituindo totalmente o conteúdo anterior.


   
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo: #<------- 3

    # 3
    # Usa o 'with open' novamente pela segurança de que o arquivo será fechado.
    # A grande e perigosa diferença aqui é o modo 'w' (write/escrever).

    # O modo 'w' é DESTRUTIVO. Antes de escrever qualquer coisa, ele APAGA
    # tudo que existia no arquivo. É como limpar um quadro branco antes de
    # escrever de novo. Por isso, é CRUCIAL que a 'lista_de_usuarios' que
    # passamos para esta função contenha TODOS os usuários, e não apenas um.

       
        json.dump(lista_de_usuarios, arquivo, indent=4) #<------- 4

        # 4
        # Esta é a linha que faz a mágica acontecer. É o oposto do json.load().
        # json.dump() significa "despejar" ou "largar" os dados no arquivo.
        #
        # Ele recebe 3 argumentos principais aqui:
        # 1. lista_de_usuarios: O objeto Python que queremos salvar. A fonte dos dados.
        # 2. arquivo: O objeto do arquivo onde os dados serão escritos. O destino.
        # 3. indent=4: Este é um argumento de "embelezamento". Ele diz para o
        #    JSON formatar o arquivo com uma indentação de 4 espaços, para que
        #    fique fácil de um humano ler. Sem isso, o JSON inteiro seria salvo
        #    em uma única linha gigante e ilegível. Para o computador, não faz
        #    diferença, mas para nós, faz toda.






def adicionar_usuario(nome, senha):
    """
    Coordena a operação de adicionar um novo usuário, garantindo que não haja duplicatas.
    Recebe um nome e senha e retorna (True, "mensagem de sucesso") ou (False, "mensagem de erro").
    """

    # --- ATO 1: LER ---
    # A primeira coisa a se fazer é carregar o estado atual do banco de dados para a memória.
    # A variável 'usuarios' agora é uma lista de dicionários Python com todos os usuários.
    usuarios = carregar_usuarios()


    # --- ATO 2: VALIDAR (A parte "pensante") ---
    # Antes de sair adicionando, a função é desconfiada. Ela verifica se o nome já existe.
    # É um loop simples que passa por cada dicionário de usuário na lista.
    for usuario in usuarios:
        # A verificação é feita em minúsculas (.lower()) para evitar que "Paulo" e "paulo"
        # sejam considerados usuários diferentes. Torna a checagem de nome insensível a maiúsculas.
        if usuario['nome'].lower() == nome.lower():
            # "SAÍDA ANTECIPADA": Se encontrar um nome igual, a função para IMEDIATAMENTE.
            # Ela nem tenta criar um ID novo ou salvar. Já retorna o fracasso e a mensagem.
            return False, f"Erro: O nome de usuário '{nome}' já existe."


    # --- ATO 3: MODIFICAR (Se a validação passou) ---

    # 3.1: Gerar um novo ID único.
    # Primeiro, ele checa se a lista de usuários NÃO está vazia.
    if usuarios:
        # Se existem usuários, ele executa uma mágica do Python para achar o maior ID:
        # (u['id'] for u in usuarios) -> "pegue o 'id' de cada usuário 'u' na lista 'usuarios'"
        # max(...) -> "encontre o maior número (o ID máximo) entre todos eles"
        # + 1 -> "some 1 para garantir que o novo ID seja único e sequencial"
        novo_id = max(u['id'] for u in usuarios) + 1
    else:
        # Se a lista está vazia, não há ID máximo. O primeiro usuário é, por definição, o ID 1.
        novo_id = 1
    
    # 3.2: Criar o dicionário do novo usuário.
    # Ele monta o objeto Python que representa o novo usuário, usando os dados recebidos.
    novo_usuario = {
        'id': novo_id,
        'nome': nome,
        'senha': senha
    }

    # 3.3: Adicionar o novo usuário à lista em memória.
    # .append() simplesmente coloca o dicionário 'novo_usuario' no final da lista 'usuarios'.
    # ATENÇÃO: Neste ponto, o arquivo .json AINDA NÃO FOI MODIFICADO. A mudança só existe na memória RAM.
    usuarios.append(novo_usuario)


    # --- ATO 4: SALVAR ---
    # Agora sim. Chamamos nossa função 'salvar_usuarios' para pegar a lista 'usuarios'
    # (agora com um item a mais) e sobrescrever o arquivo .json no disco.
    # É neste momento que a mudança se torna permanente.
    salvar_usuarios(usuarios)


    # --- ATO 5: RETORNAR SUCESSO ---
    # Se o código chegou até aqui, significa que tudo deu certo.
    # A função retorna o sucesso e uma mensagem amigável para a interface mostrar.
    return True, f"Usuário '{nome}' criado com sucesso!"



def verificar_usuario(nome, senha):
    usuarios = carregar_usuarios()
    print(usuarios)
    for usuario in usuarios:
        if usuario['nome'].lower() == nome.lower() and usuario['senha'] == senha:
            return usuario
    return None