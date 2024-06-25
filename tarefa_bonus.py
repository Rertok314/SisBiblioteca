
lista_documentos = []
lista_documentos_emprestados = []
historico_documentos_emprestados = []
lista_usuarios = []
visitas_guiadas = []
figuras = []
autores = []


#PESQUISA DE DOCUMENTOS - 1
def pesquisar_documentos():
    nome_doc = input('Digite o nome do documento que deseja encontrar: ')
    if len(lista_documentos) == 0:
        print('\nNÃO EXISTEM DOCUMENTOS CADASTRADOS!\n')
        main()
    else:
        for docs in lista_documentos:
            if nome_doc == docs['titulo']:
                print('SEGUE INFORMAÇÕES DO DOCUMENTO PESQUISADO')
                for x in docs:
                    print(f'{x} = {docs[x]}')
            else:
                print('DOCUMENTO NÃO ENCONTRADO!')
        main()

#CADASTRO DE USUÁRIOS - 2
def cadastrar_usuarios():
    usuario = input('\nDigite o nome do usuário: ')
    senha = input('Digite a senha do usuário: ')
    usuarios = dict(usuario = usuario, senha = senha)
    lista_usuarios.append(usuarios)
    print(f'\nUsuário: {usuario} e senha: {senha} cadastrado com sucesso!')
    opcao = int(input('''
    Deseja cadastrar outro usuário?
    
    1. SIM
    2. NÃO
        
    Escolha: '''))
    if opcao == 1:
        cadastrar_usuarios()
    else:
        main()

#CADASTRO DE DOCUMENTOS - 3        
def cadastrar_documentos():  
    titulo = input('\nDigite o título do documento: ')
    data_producao = input('Digite a data de produção do documento: ')
    tema = input('Digite o tema do documento: ')
    contexto_historico = input('Digite o contexto histórico do documento: ')
    descricao = input('Digite a descrição do documento: ')
    autor = input('Digite o autor do documento: ')
    localizacao_biblioteca = input('Digite a localização na biblioteca do documento: ')
    
    documentos = dict(titulo = titulo, data_producao = data_producao,tema = tema, contexto_historico = contexto_historico, descricao = descricao, autor = autor, localizacao_biblioteca = localizacao_biblioteca)
    
    while True:
        material_relacionado = int(input('''
    Deseja cadastrar material relacionado?
        
    1. SIM
    2. NÃO
        
    Resposta: '''))
        
        if material_relacionado == 1:
            material = int(input('''
    Escolha o tipo de material: 
                
    1. CORRESPONDÊNCIA
    2. FOTOGRAFIA
    3. ENTREVISTA
                
    Resposta: '''))
            if material == 1:
                material = input('Digite o nome da correspondência: ')
                documentos.update(correspondência = material)
            elif material == 2:
                material = input('Digite o nome da fotografia: ')
                documentos.update(fotografia = material)
            else:
                material = input('Digite o nome da entrevista: ')
                documentos.update(entrevista = material)
        else:
            break
    opcao = int(input('''
    Deseja cadastrar outro documento? 
        
    1. SIM
    2. NÃO
        
    Escolha: '''))
    
    lista_documentos.append(documentos)
    
    if opcao == 1:
        cadastrar_documentos()
    else:
        main()

# GERENCIAMENTO DE EMPRÉSTIMOS - 4
def gerenciar_emprestimos():
    
    opcao = int(input('''
        Escolha uma opção: 
        1. CADASTRAR EMPRÉSTIMO
        2. HISTÓRICO DE EMPRÉSTIMOS
        3. ACOMPANHAR DOCUMENTOS FORA DA BIBLIOTECA
        4. CADASTRAR DEVOLUÇÃO DE DOCUMENTO EMPRESTADO
        
        Resposta: 
        '''))
    
    #CADASTRAR EMPRÉSTIMO
    if opcao == 1:
        #dados dos documentos
        nome_documento = input('Digite o nome do documento a ser emprestado: ')
        periodo_emprestimo = input('Digite quantos dias o documento ficará emprestado: ')
        evento = input('Digite o nome do evento: ')
        responsavel = input('Digite o nome do responsável: ')
        tema = input('Digite o tema do evento: ')
        
        #cadastro em lista
        doc_emprestado = dict(nome_documento = nome_documento, periodo_emprestimo = periodo_emprestimo + 'dias', evento = evento, responsavel = responsavel, tema = tema)
        lista_documentos_emprestados.append(doc_emprestado)
        historico_documentos_emprestados.append(doc_emprestado)
        
        #cadastro em arquivo
        try:
            with open('lista documentos.txt', 'a') as arquivo:
                arquivo.write(doc_emprestado)
        except Exception as erro:
            print(f'Erro encontrado = {erro}')
    
    #HISTÓRICO DE EMPRÉSTIMOS
    elif opcao == 2:
        for emp in historico_documentos_emprestados:
            print(emp)
    
    #ACOMPANHAR DOCS EMPRESTADOS
    elif opcao == 3:
        print('SEGUE LISTA DE DOCUMENTOS EMPRESTADOS')
        for i, emp in enumerate(lista_documentos_emprestados):
            print(f'{i} - Documento {emp}')
    
    #CADASTRAR DEVOLUÇÃO
    elif opcao == 4:
        doc_devolvido = input('Digite o nome do documento devolvido: ')
        for dev in lista_documentos_emprestados:
            if doc_devolvido == dev['nome_documento']:
                lista_documentos_emprestados.remove(dev)
                print('Devolução de documento cadastrada com sucesso!')
                gerenciar_emprestimos()
            else:
                print('NOME INVÁLIDO')
                gerenciar_emprestimos()

#VISITAS GUIADAS - 5
def visitas():
    dados_visita = dict(tema = tema, descrição = descricao)
    tema = input('Digite o tema da visita guiada: ')
    descricao = input('Digite o tema da visita guiada: ')
    
    qt_documentos = int(input('Digite a quantidade de documentos visitados: '))
    
    i = 0    
    for doc in range(qt_documentos):
        doc = input('Digite o tema da visita guiada: ')
        i+=1
        dados_visita['documento'+str(i)] = doc
    
    try:
        with open('visitasGuiadas.txt', 'w') as arquivo:
            arquivo.write(dados_visita)
    except Exception as erro:
        print(f'Erro encontrado {erro}')

#CADASTRO DE FIGURAS PROEMINENTES - 6
def figuras_proeminentes():
    opcao = int(input('''
    Digite sua opção:
    1. CADASTRAR FIGURA PROEMINENTE
    2. PESQUISAR FIGURA PROEMINENTE
    
    Resposta: 
    '''))
    
    if opcao == 1:  
        nome = input('Digite o nome da figura proeminente: ')
        categoria = input('''Digite a categoria: 
            1. LÍDER POLÍTICO
            2. FIGURA CULTURAL
            
            Resposta:
            ''')
        if categoria == 1:
            categoria = 'LÍDER POLÍTICO'
        else:
            categoria = 'FIGURA CULTURAL'
        figura = dict(nome = nome, categoria = categoria)
        figuras.append(figura)
        main()
        
    elif opcao == 2:
        nome = input('Digite o nome para pesquisa: ')
        for fig in figuras:
            x = fig['nome']
            y = fig['categoria']
            if fig['nome'] == nome:
                print(f'Segue informações da figura proeminente pesquisada: nome = {x} e categoria = {y}\n')
                opc = int(input('''
                Deseja cadastrar a figura proeminente como parte das informações de um documento?
                1. SIM
                2. NÃO
                
                Resposta: 
                '''))
                if opc == 1:
                    nome_doc = input('Digite o nome do documento: ')
                    for doc in lista_documentos:
                        if doc['nome'] == nome_doc:
                            doc.update(fig)
        main()

#CADASTRO DE AUTORES - 7                
def cadastrar_autores():
    while True:
        nome = input('Digite o nome do autor: ')
        data_nascimento = input('Digite a data de nascimento do autor: ')
        local_nascimento = input('Digite o local de nascimento do autor: ')
        biografia = input('Digite a biografia do autor: ')
        
        autor = dict(nome = nome, data_nascimento = data_nascimento, local_nascimento = local_nascimento, biografia = biografia)
        
        area_pesquisa = int(input('''
    Deseja adicionar área de pesquisa? 
    1. SIM
    2. NÃO
    Escolha: '''))
        if area_pesquisa == 1:
            areas_pesquisas(autor)
        autores.append(autor)
        novo_autor = int(input('''
    Deseja cadastrar outro autor? 
    1. SIM
    2. NÃO
    Escolha: '''))
        if novo_autor == 1:
            cadastrar_autores()
        else:
            main()
        
def areas_pesquisas(autor):
    denominacao = input('Digite a denominação da área de pesquisa: ')
    periodo_estudo = input('Digite o período de estudo da área de pesquisa: ')
    descricao_caracteristicas = input('Digite a característica da área de pesquisa: ')
    obra_representativa = input('Digite a obra representativa da área de pesquisa: ')
        
    x = autor.update(denominação = denominacao, periodo_estudo = periodo_estudo, caracteristicas = descricao_caracteristicas, obra_representativa = obra_representativa)
    return x

def relacao_autores():
    if len(autores) == 0:
        print('\n\tNÃO HÁ AUTORES CADASTRADOS!\n')
    print('SEGUE LISTA DE AUTORES ORDENADA')
    for aut in autores:
        print(aut)
    main()

def relacao_usuarios():
    if len(lista_usuarios) == 0:
        print('\n\tNÃO HÁ AUTORES CADASTRADOS!\n')
    print('SEGUE LISTA DE USUÁRIOS ORDENADA')
    for aut in lista_usuarios:
        print(aut)
    main()

#SUBMENUS
def submenu_cadastro():
    opcao = int(input('''
    Escolha uma opção

    1. CADASTRAR USUÁRIO
    2. CADASTRAR DOCUMENTO HISTÓRICO
    3. CADASTRAR VISITA GUIADA
    4. CADASTRAR AUTOR
    5. MENU PRINCIPAL
    
    Escolha: '''))
    if opcao == 1:
        cadastrar_usuarios()
    elif opcao == 2:
        cadastrar_documentos()
    elif opcao == 3:
        visitas()
    elif opcao == 4:
        cadastrar_autores()
    else:
        main()

def submenu_gerenciamento():
    opcao = int(input('''
    Escolha uma opção

    1. GERENCIAR EMPRÉSTIMOS
    2. GERENCIAR FIGURAS PROEMINENTES
    3. RELAÇÃO DE AUTORES
    4. RELAÇÃO DE USUÁRIOS
    4. MENU PRINCIPAL
    
    Escolha: '''))
    if opcao == 1:
        gerenciar_emprestimos()
    elif opcao == 2:
        figuras_proeminentes()
    elif opcao == 3:
        relacao_autores()
    elif opcao == 4:
        relacao_usuarios()
    else:
        main()

#SISTEMA DE ORDENAÇÃO DE LISTAS
def ordenacao_listas():
    opcao = int(input('''
    Digite qual listagem deseja ordenar:
    1. LISTA DE USUÁRIOS
    2. LISTA DE DOCUMENTOS
    3. LISTA DE AUTORES
    4. RETORNAR AO MENU PRINCIPAL
    '''))
    if opcao == 1:
        if len(lista_usuarios) == 0:
            print('\nNÃO EXISTE USUÁRIO CADASTRADO')
        else:
            print(f'Segue lista desordenada {lista_usuarios}')
            selection_sort(lista_usuarios, 'usuario')
            print(f'\nSegue lista de usuários ordenada {lista_usuarios}')
        ordenacao_listas()
    if opcao == 2:
        if len(lista_documentos) == 0:
            print('\nNÃO EXISTE DOCUMENTO CADASTRADO')
        else:
            print(f'Segue lista desordenada {lista_documentos}')
            selection_sort(lista_documentos, 'titulo')
            print(f'\nSegue lista de documentos ordenada {lista_documentos}')
        ordenacao_listas()
    if opcao == 3:
        if len(autores) == 0:
            print('NÃO EXISTE AUTOR CADASTRADO')
        else:
            print(f'Segue lista desordenada {autores}')
            selection_sort(autores, 'nome')
            print(f'\nSegue lista de autores ordenada {autores}')
        ordenacao_listas()
    else:
        main()
        
def selection_sort(lista, chave):
    n = len(lista)
    for i in range(n):
        menor_indice = i
        for j in range(i+1, n):
            if lista[j][chave] < lista[menor_indice][chave]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

    print(lista)

def main():
    print('\n>> SISTEMA DE BIBLIOTECA DE HISTÓRIA <<')
    print('\nESCOLHA UMA OPÇÃO')
    opcao = int(input('''
    
    1. SISTEMA DE CADASTROS
    2. SISTEMA DE GERENCIAMENTO
    3. SISTEMA DE PESQUISA DE DOCUMENTO
    4. SISTEMA DE ORDENAÇÃO DE LISTAS
    5. SAIR
    
    Escolha: '''))
    if opcao == 1:
        submenu_cadastro()
    elif opcao == 2:
        submenu_gerenciamento()
    elif opcao == 3:
        pesquisar_documentos()
    elif opcao == 4:
        ordenacao_listas()
    elif opcao == 5:
        exit()
    else:
        main()


if __name__ == '__main__':
    main()