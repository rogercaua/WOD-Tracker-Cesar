#Guilherme
def adicionar_treino(treinos):
    data = input('>>>Digite a data do treino (dd/mm/aaaa): ').strip()
    tipo = input('>>>Digite o tipo de treino (AMRAP, EMOM, For Time): ').strip()
    tempo = input('>>>Digite o tempo do treino (hh:mm:ss): ').strip()
    exercicios = input('>>>Digite os exercícios separados por vírgula: ').strip().split(',')
    exercicios = [e.strip() for e in exercicios]
    
    treino = [data, tipo, tempo, exercicios]
    treinos.append(treino)
    print('Treino adicionado com sucesso!')

#-------------------------------------------------->
# Joshua
def importar_treinos(ARQUIVO):
    treinos = []
    try:
        with open(ARQUIVO, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                dados = linha.strip().split(';')
                if len(dados) >= 4:
                    data = dados[0]
                    tipo = dados[1]
                    tempo = dados[2]
                    exercicios = dados[3].split(',')
                    treino = [data, tipo, tempo, exercicios]
                    treinos.append(treino)
    except FileNotFoundError:
        pass
    return treinos

#-------------------------------------------------->

def salvar_treinos_em_csv(treinos, ARQUIVO):
    try:
        with open(ARQUIVO, 'w') as file:
            for treino in treinos:
                exercicios = ','.join(treino[3])
                file.write(f'{treino[0]};{treino[1]};{treino[2]};{exercicios}\n')
    except Exception as e:
        print(f'Erro ao exportar treinos: \n{e}')

#-------------------------------------------------->

def listar_treinos(treinos):
    if treinos:
        for i, treino in enumerate(treinos):
            print(f'{i} - {treino[0]} | {treino[1]} | {treino[2]} | {treino[3]}')
    else:
        print('Não existe nenhum treino registrado. Adicione algum!')

#-------------------------------------------------->
#guilherme
def excluir_treino(treinos):
    listar_treinos(treinos)
    try:
        indice = int(input('Digite o índice do treino que deseja excluir: '))
        if 0 <= indice < len(treinos):
            treinos.pop(indice)
            print('Treino excluído com sucesso!')
        else:
            print('Índice inválido.')
    except Exception as e:
        print(f'Houve um erro ao excluir o treino \n{e}')

#-------------------------------------------------->
#João
def editar_treino_por_indice(treinos):
    listar_treinos(treinos)
    try:
        indice = int(input('>>>Digite o índice do treino que deseja editar: '))
        if 0 <= indice < len(treinos):
            data = input('>>>Digite a nova data (dd/mm/aaaa): ').strip()
            tipo = input('>>>Digite o novo tipo: ').strip()
            tempo = input('>>>Digite o novo tempo (hh:mm:ss): ').strip()
            exercicios = input('>>>Digite os exercícios separados por vírgula: ').strip().split(',')
            exercicios = [e.strip() for e in exercicios]
            
            treino = [data, tipo, tempo, exercicios]
            treinos[indice] = treino
            print('Treino editado com sucesso!')
        else:
            print('Índice inválido.')
    except Exception as e:
        print(f'Houve um erro ao editar o treino \n{e}')

#-------------------------------------------------->

def query_treinos_por_data(treinos):
    if treinos:
        data = input('>>>Digite a data (dd/mm/aaaa): ').strip()
        encontrados = [treino for treino in treinos if treino[0] == data]
        if encontrados:
            for i, treino in enumerate(encontrados):
                print(f'{i} - {treino[0]} | {treino[1]} | {treino[2]} | {treino[3]}')
        else:
            print('Nenhum treino encontrado para esta data.')
    else:
        print('>>>Nenhum treino existente. Adicione algum!')

#-------------------------------------------------->

def query_treinos_por_tipo(treinos):
    if treinos:
        tipo = input('>>>Digite o tipo de treino (AMRAP, EMOM, For Time): ').strip()
        encontrados = [(i, treino) for i, treino in enumerate(treinos) if treino[1] == tipo]
        if encontrados:
            for i, treino in encontrados:
                print(f'{i} - {treino[0]} | {treino[1]} | {treino[2]} | {treino[3]}')
        else:
            print('Nenhum treino encontrado para esse tipo.')
    else:
        print('>>>Nenhum treino existente. Adicione algum!')

#-------------------------------------------------->


def contar_treinos_por_tipo(treinos):
    if not treinos:
        print("Nenhum treino registrado.")
        return

    contagem = {'AMRAP': 0, 'EMOM': 0, 'For Time': 0}
    for treino in treinos:
        tipo = treino[1]
        if tipo in contagem:
            contagem[tipo] += 1
        else:
            contagem[tipo] = 1  # Caso haja outro tipo digitado

    print("\n--- Quantidade de treinos por tipo ---")
    for tipo, qtd in contagem.items():
        print(f"{tipo}: {qtd}")


#-------------------------------------------------->
#Rafael
def imprimir_menu(ARQUIVO):
    treinos = importar_treinos(ARQUIVO)

    while True:
        print("\n ---Menu WodTracker--- ")
        print("1. Adicionar treino")
        print("2. Listar treinos")
        print("3. Excluir treino")
        print("4. Editar treino")
        print("5. Buscar treinos por data")
        print('6. Buscar treinos por tipo')
        print("7. Exportar Treinos")
        print("8. Sair")

        escolha = input(">>>Escolha uma opção: ")

        if escolha == '1':
            adicionar_treino(treinos)
        elif escolha == '2':
            listar_treinos(treinos)
        elif escolha == '3':
            excluir_treino(treinos)
        elif escolha == '4':
            editar_treino_por_indice(treinos)
        elif escolha == '5':
            query_treinos_por_data(treinos)
        elif escolha == '6':
            query_treinos_por_tipo(treinos)
        elif escolha == '7':
            salvar_treinos_em_csv(treinos, ARQUIVO)
        elif escolha == '8':
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
