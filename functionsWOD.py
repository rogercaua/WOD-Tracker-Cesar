# treinos = [
#     {'data':'12/10/2023','tipo':'AMRAP' ,'tempo':'00:24:12','exercicio': ['Supino reto', 'Supino inclinado', 'fly']},
#     ...
# ]

def adicionar_treino(treinos): # OK
    data = input('Digite a data do treino (dd/mm/aaaa): ')
    tipo = input('Digite o tipo de treino: ')
    tempo = input('Digite o tempo do treino: (hh:mm:ss) ')
    exercicio = input('Digite os exercícios separados por vírgula: ').strip().split(',')
    
    exercicio = [ item.strip() for item in exercicio ]
    
    treino = {
        'data': data,
        'tipo': tipo,
        'tempo': tempo,
        'exercicio': exercicio
    }
    
    treinos.append(treino)
    print('Treino adicionado com sucesso!')
           
#-------------------------------------------------->
            
def importar_treinos(): #OK
    treinos = []
    try:
        with open('AQUIVO_DE_SAVE', 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                dados = linha.strip().split(';')
                
            if not linhas:
                return []
    except FileNotFoundError:
        return []
    
    return treinos
    
#-------------------------------------------------->
    
def salvar_treinos_em_csv(treinos): #OK
    try:
        with open('ARQUIVO', 'r')as file:  
            for treino in treinos:
                file.write(f'{treino['data']};{treino['tipo']};{treino['exercicio']}')
            
    except Exception as e:
        print(f'Erro ao exportar treinos: \n{e}')
    
#-------------------------------------------------->

def listar_treinos(treinos):# OK
    try:
        if treinos:
           for i, treino in enumerate(treinos):
            print(f'{i} - {treino['data']} | {treino['tipo']} | {treino['tempo']} | {treino['exercicio']}')
                
        if not treinos:
            print('Não existe nenhum treino registrado. Adicione Algum!')
    except Exception as e:
        print(f'Houve um erro ao listar os treinos \n{e}')



#-------------------------------------------------->
    
def imprimir_menu():
    treinos = importar_treinos()
    
    print("\n ---Menu WodTracker--- ")
    print("1. Adicionar treino")
    print("2. Listar treinos")
    print("3. Excluir treino")
    print("4. Editar treino")
    print("5. Buscar treino por data")
    print("6. Exportar Treinos")
    print("7. Sair")
    
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        adicionar_treino(treinos)
    elif escolha == '2':
        listar_treinos(treinos)
    elif escolha == '3':
        excluir_treino(treinos) #falta 
    elif escolha == '4':
        editar_treino_por_indice() #falta
    elif escolha == '5':
        treino_por_data() #falta
    elif escolha == '6'
        treino_por_tipo() # falta
    elif escolha == '7':
        salvar_treinos_em_csv(treinos)
    elif escolha == '8':
        print("Saindo do programa...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
            
