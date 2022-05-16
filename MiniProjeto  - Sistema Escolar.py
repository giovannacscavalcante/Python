print("                ()\n");
print("                /\\  \n");          
print("               |==| \n");         
print("               ==== \n");         
print("                XX  \n");        
print("               xXXx \n");       
print("               XXXX \n");       
print("               XXXX \t\t            Bem-Vindo - Welcome - Bienvenido - Bienvenue\n"); 
print("               XXXX \n");       
print("              xXXXXx\t                        * Sistema de Administração Escolar *\n");
print("              XXXXXX\n");
print("              XXXXXX\t\t                       - Escola de Idiomas -\n");
print("             xXXXXXXx\n");
print("             XXXXXXXX\n");
print("            xXXXXXXXXx\n");
print("            XXXXXXXXXX                      	           \n");
print("           XXXXX  XXXXX                   	      	  \n");
print("          xXXXX    XXXXx                   	         \n");
print("         XXXXXxxxxxxXXXXX                  	        \n");
print("       xXXXXX--------XXXXXx                 	        \n");
print("    xXXXXXX           XXXXXXx\n");
print(" xxXXXXXXX             XXXXXXXxx\t\t  \n");
print("				                 ");
print("\n\n");

cadastro_alunos = [] #Lista Principal
todos=[cadastro_alunos] #Todos os cadastros

def cadastrar(indice_existente = None): #função cadastrar/matricular aluno
    #matriculando alunos
    
        aluno =  {           #dicionario informando as principais variaveis
        "Matrícula do aluno": "",
        "Nome do aluno": "",
        "Data de nascimento": "",
        "CPF": "",
        "Telefone": "" ,
        "Idioma": "",
        "Módulo": "",    
        "Turno": ""
        }
        print("Digite os campos abaixo para cadastrar um aluno: \n")
        for chave in aluno: 
            aluno[chave] = input(chave + ": ") #Desse modo não precisa colocar input para todos os atributos
            
          
        if indice_existente is None:
            cadastro_alunos.append(aluno) #Acumula as informações inseridas pelo usuario nesse append
            print("Aluno cadastrado com sucesso.")
        else:
            cadastro_alunos[indice_existente] = aluno
            print("Aluno atualizado com sucesso.")
   
        return

def pesquisar(): #funcao pesquisar um aluno especifico pela matricula
    
    termo_pesquisa = input("Digite a matrícula do aluno: ").lower()
     
    for elemento in cadastro_alunos:
        if elemento["Matrícula do aluno"].lower() == termo_pesquisa: #se corresponder com oq existe vai printar o aluno
            print()
            for chave in elemento:
                print(f"{chave}: {elemento[chave]}") 
            print("-"*50)    #aqui foi estipulado um numero de cadastros
    
    return
       
        
def imprimir(): #funcao para imprimir todos os alunos matriculados
    print(todos)
'''

   #imprimindo lista de alunos matriculados
    if len(cadastro_alunos) > 0:
           # print('Alunos matriculados')
           # print("Nr")
           # print("Matrícula do aluno")
           # print("Nome do aluno")
           # print("Data de nascimento")
           # print("CPF")
           # print("Telefone")
           # print("Idioma")
           # print("Turno")
        

        for posicao_e_aluno in list(enumerate(cadastro_alunos, start=1)):
            
            posicao = posicao_e_aluno[0]
            aluno = posicao_e_aluno[1]
            
            print(str(posicao))
            print(str(aluno['Matrícula do aluno\n']))
            print(str(aluno['Nome do aluno\n']))
            print(str(aluno['Data de nascimento\n']))
            print(str(aluno['CPF\n']))
            print(str(aluno['Telefone\n']))
            print(str(aluno['Idioma\n']))
            print(str(aluno['Módulo\n']))
            print(str(aluno['Turno\n\n']))
    else:
        print("Não há alunos matriculados\n")
    
    return
'''
def remover(): #funcao para remover um aluno do sistema
    
    if len(cadastro_alunos) > 0:
        
        matricula_informada = input("\n\nDigite o número de matrícula para remover o aluno do sistema: ")
        alunos_encontrados_por_matricula = [aluno for aluno in cadastro_alunos if matricula_informada == str(aluno['Matrícula do aluno'])]
        
        if len(alunos_encontrados_por_matricula) > 0:
            for aluno_encontrado in alunos_encontrados_por_matricula:
                cadastro_alunos.remove(aluno_encontrado)
            
            print(f"Foram removidos {len(alunos_encontrados_por_matricula)} alunos com a matrícula {matricula_informada}")
        else:
            print(f"Não foram encontrados alunos com a matrícula {matricula_informada}")
                            
    else:
        print("Não é possível remover nenhum aluno porque não há alunos matriculados.")
        
    return

def atualizar(): #funcao para atualizar dados de um aluno
    
    quantidade_alunos_sistema = len(cadastro_alunos)
    
    if quantidade_alunos_sistema > 0:
        
        imprimir()
        
        indice_informado = int(input("\n\nDigite o número do índice da matrícula do aluno para atualizar o cadastro: "))
        
        if indice_informado > quantidade_alunos_sistema or indice_informado < 1:
            print("O número do índice precisa ser maior que zero e existir no sistema.")
        else:
            cadastrar(indice_informado-1)                            
    else:
        print("Não é possível atualizar nenhum cadastro porque não há alunos matriculados.") 
                                
    return

def tela_menu(): #função exibe menu principal
    print("\n\t\t\t  [1] >> Matricular Aluno");
    print("\n\t\t\t  [2] >> Pesquisar Aluno ");
    print("\n\t\t\t  [3] >> Listar Alunos Matriculados");
    print("\n\t\t\t  [4] >> Apagar Registro de Aluno");
    print("\n\t\t\t  [5] >> Atualizar Registro de Aluno");
    print("\n\t\t\t  ===================================\n");
    print("\n\t\t\t  [0] >> Sair");
    
tela_menu()
opcao = int(input())

while 0 <= opcao <= 5: #chama a opcao escolhida
    
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        pesquisar()
    elif opcao == 3:
        imprimir()    
    elif opcao == 4:
        remover()
    elif opcao == 5:
        atualizar()
    elif opcao == 0:
        print('Programa encerrado')
        exit()
    
    tela_menu()
    opcao = int(input())
    
else:
        print('Opção inválida, programa encerrado')





