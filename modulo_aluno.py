from random import randint
from validacao_email import verificacao
from validacao_telefone import validacao
from validacao_data_nasc import certification
from pickle import dump, load

cor_do_terminal = "\033[1;92;47m"  # 1=Negrito, 92=Verde Claro, 47=Fundo Branco
reset = "\033[0m"

def portal_alunos(professores, alunos, serie):
        try:
            Arq_series = open('series.txt', 'rb')
            serie = load(Arq_series)
            Arq_series.close()
        except:
            Arq_series = open('series.txt', 'wb')
            Arq_series.close()
            
        try:
            Arq_professores = open('professores.txt', 'rb')
            professores = load(Arq_professores)
            Arq_professores.close()
        except:
            Arq_professores = open('professores.txt', 'wb')
            Arq_professores.close()

        try:
            Arqalunos = open('Alunos.txt', 'rb')
            alunos = load(Arqalunos)
            Arqalunos.close()
        except:
            Arqalunos = open('Alunos.txt', 'wb')
            Arqalunos.close()
        
        print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
        print(cor_do_terminal+"║                           PORTAL DO ALUNO                                  ║"+reset)
        print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [1] Cadastro de Alunos                                                   ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [2] Atualizar Dados do Aluno                                             ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [3] Exclusão do Aluno                                                    ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [4] Ver Grade Diária de Aulas                                            ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        opcao2 = int(input("\tDigite a opção que deseja acessar: "))

        if opcao2 == 1:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                           CADASTRO DE ALUNOS                               ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
           
            matricula = randint(20260000, 20269999)
            while matricula in alunos:
                matricula = randint(20260000, 20269999)
            matricula_str = str(matricula)

            print()
            nome_aluno = input('\tDigite o nome do aluno: ').title().strip()
            print()
            
            while True:
                data_nasc = input('\tDigite a data de nascimento do aluno(xx/xx/xxxx): ').strip()
                print()
                if certification(data_nasc) == True:
                    break
                else:
                    print('\t[Error] Data de nascimento inválida')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")

            while True:        
                email = input('\tDigite o email do aluno: ').strip()
                print()
                if verificacao(email) == True:
                    break
                else:
                    print('\t[Error] Email inválido')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")

            turma = input('\tDigite a turma que vai cursar: ').strip()
            print()


            alunos[matricula_str] = [nome_aluno, data_nasc, email]
            print('\tEsses são os alunos cadastrados: {}'.format(alunos))
            print()
            print('\tEssa é sua senha de acesso: {}'.format(matricula))

            Arq_alunos = open('Alunos.txt','wb')
            dump(alunos,Arq_alunos)
            Arq_alunos.close()

            turma_encontrada = False
            if turma in serie:
                turma_encontrada = True
                qntd_alunos = len(serie[turma]['alunos'])

                aluno_encontrado = False
                for i in range (qntd_alunos):
                    if nome_aluno != serie[turma]['alunos'][i][0]:
                        aluno_encontrado = True
         
                    if not aluno_encontrado:
                        print('Aluno já cadastrado na turma') 
                        input("\tAPERTE >ENTER< PARA CONTINUAR ")  

                serie[turma]['alunos'].append([nome_aluno, data_nasc, email])
                Arq_series = open('series.txt', 'wb')
                dump(serie, Arq_series)
                Arq_series.close()
                print()
                print('\tEsses são os alunos do {}: {}'.format(turma,serie[turma]['alunos']))
                print()
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                     ALUNO CADASTRADO COM SUCESSO                           ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)                
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                input("\tAPERTE >ENTER< PARA CONTINUAR ") 
                
            if not turma_encontrada:
                print('\tNão existe essa turma na escola')
                input("\tAPERTE >ENTER< PARA CONTINUAR ")
            
        
            

        if opcao2 == 2:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                       ATUALIZAR DADOS DOS ALUNOS                           ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)

            matricula = input('\tDigite a matrícula do aluno: ').strip()
            turma = input('\tDigite a turma que o aluno estuda: ').strip()
            print()


            if matricula in alunos:
                if turma in serie:
                    qntd_alunos = len(serie[turma]['alunos'])
                    
                    for i in range (qntd_alunos):
                        if alunos[matricula][0] in serie[turma]['alunos'][i]:
                            novo_nome = input('\tDigite o novo nome do aluno: ').strip().title()
                            while True:
                                data_nas = input('\tDigite a nova data de nascimento(xx/xx/xxxx): ').strip()
                                if certification(data_nas) == True:
                                    break
                                else:
                                    print('\t[Error] Data de nascimento inválida')
                                    input("\tAPERTE >ENTER< PARA CONTINUAR ")

                            while True:           
                                email = input('\tDigite o novo email do aluno: ').strip()
                                print()
                                if verificacao(email) == True:
                                    break
                                else:
                                    print('\t[Error] Email inválido')
                                    input("\tAPERTE >ENTER< PARA CONTINUAR ")


                            alunos[matricula] = [novo_nome, data_nas, email]

                            Arq_alunos = open('Alunos.txt', 'wb')
                            dump(alunos, Arq_alunos)
                            Arq_alunos.close()

                            serie[turma]['alunos'][i] = alunos[matricula]

                            Arq_series = open('series.txt', 'wb')
                            dump(serie, Arq_series)
                            Arq_series.close()

                            print()
                            print('\tTodos os dados dos alunos: {}'.format(alunos))
                            print()
                            print('\tDados do aluno atuzalizado na turma: {}'.format(serie[turma]['alunos'][i]))
                            print()
                            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                            print(cor_do_terminal+"║                                                                            ║"+reset)
                            print(cor_do_terminal+"║                       ATUALIZAÇÃO DE DADOS CONCLUÍDA                       ║"+reset)
                            print(cor_do_terminal+"║                                                                            ║"+reset)                
                            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                            print(cor_do_terminal+"║                                                                            ║"+reset)
                            print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                            print(cor_do_terminal+"║                                                                            ║"+reset)
                            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                            print()
                            input("\tAPERTE >ENTER< PARA CONTINUAR ")

                    print('\tAluno não cadastrado na série')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")

                else: 
                    print('\tTurma inexistente')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")
            else:
                print('\tNão tem nenhum aluno cadastrado com esse nome')
                input("\tAPERTE >ENTER< PARA CONTINUAR ")




        elif opcao2 == 3:
            
            
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                            EXCLUSÃO DE ALUNOS                              ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            print()
            matricula = input('\tDigite a matrícula do aluno: ').strip()
            turma = input('\tDigite a turma que ele estuda: ').strip()


            if matricula in alunos:

                if turma in serie:
                    tam = len(serie[turma]['alunos'])

                    for i in range(tam):
                        nome_aluno = alunos[matricula][0]
                        if nome_aluno in serie[turma]['alunos'][i]:
                            del alunos[matricula]
                            print('\tAlunos da escola: {}'.format(alunos))  

                            del serie[turma]['alunos'][i]

                            Arq_alunos = open('Alunos.txt', 'wb')
                            dump(alunos, Arq_alunos)
                            Arq_alunos.close()


                            Arq_series = open('series.txt', 'wb')
                            dump(serie, Arq_series)
                            Arq_series.close()



                            print('\tAlunos do {}: {}'.format(turma, serie[turma]['alunos']))
                            print()
                            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                            print(cor_do_terminal+"║                                                                            ║"+reset)
                            print(cor_do_terminal+"║                         EXCLUSÃO DE ALUNO CONCLUÍDA                        ║"+reset)
                            print(cor_do_terminal+"║                                                                            ║"+reset)                
                            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                            print(cor_do_terminal+"║                                                                            ║"+reset)
                            print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                            print(cor_do_terminal+"║                                                                            ║"+reset)
                            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                            print()
                            input("\tAPERTE >ENTER< PARA CONTINUAR ")
                            
                        
                    else:
                        print()
                        print('\tNão tem esse aluno cadastrado na turma')
                        input("\tAPERTE >ENTER< PARA CONTINUAR ")
            else:
                print()
                print('\tNão tem esse aluno cadastrado')    
                input("\tAPERTE >ENTER< PARA CONTINUAR ")
        
        elif opcao2 == 4:
            
                
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                            GRADE DIÁRIA DE AULAS                           ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                matricula = input('\tDigite a sua matrícula: ').strip()
                nome_aluno = input('\tDigite o seu nome: ').strip().title()
                turma = input('\tDigite a turma que você estuda: ').strip()
                dia = input('\tDigite o dia que você quer ver a grade: ').strip().title()


                if matricula in alunos:
                    nome_valido = alunos[matricula][0]
                    lista_alunos = serie[turma]['alunos']
                    tam_lista_alunos = len(lista_alunos)

                    for j in range(tam_lista_alunos):

                        if lista_alunos[j][0] == nome_valido:
                            lista_horarios = serie[turma]['horarios']
                            tam = len(lista_horarios)
                    
                            for i in range(tam):
                    
                                if lista_horarios[i][1] == dia:
                                    print()
                                    print(f'\tDia: {lista_horarios[i][1]}')
                                    print(f'\tMatéria: {lista_horarios[i][2]}')
                                    print(f'\tHorário: {lista_horarios[i][0]}')
                                    print()
                                    input("\tAPERTE >ENTER< PARA CONTINUAR ")
                    else:
                        print()
                        print('\tAluno não cadastrado na turma')  
                        input("\tAPERTE >ENTER< PARA CONTINUAR ")      
                else:
                    print()
                    print('\tAluno não cadastrado na escola')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")




        elif opcao2 > 4:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                             OPÇÃO INEXISTENTE                              ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            input("\tAPERTE >ENTER< PARA PULAR ")