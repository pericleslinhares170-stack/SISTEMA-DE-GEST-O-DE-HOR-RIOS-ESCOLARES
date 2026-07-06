from pickle import dump, load
cor_do_terminal = "\033[1;92;47m"  # 1=Negrito, 92=Verde Claro, 47=Fundo Branco
reset = "\033[0m"
def option_relatory(serie, professores, alunos):
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

        professor_encontrado = False
        horario_encontrado = False
        soma_horarios = 0
        print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
        print(cor_do_terminal+"║                           Relatório do Sistema                             ║"+reset)
        print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [1] Capacidade Restante da Turma                                         ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [2] Choque de Horários                                                   ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        opcao2 = int(input("\tDigite a opção que deseja acessar: "))
        
        if opcao2 == 1:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                            CAPACIDADE RESTANTE                             ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            lista_turma = []
            for chave in serie:
                 lista_turma.append(chave)
            print('\tEssas são as turmas disponíveis: {}'.format(lista_turma))
            turma = input('\tDigite uma dessas turmas: ').strip()
            print()

            if turma in serie:
                capacidade_turma = serie[turma]['capacidade']
                for item in capacidade_turma:
                    capa_sep = item.split(' ')
                capa_tur_int = int(capa_sep[0])

                qntd_alunos = len(serie[turma]['alunos'])
                capa_rest = capa_tur_int - qntd_alunos

                print('\tEssa é a quantidade de vagas restantes no {}: {}'.format(turma,capa_rest))
                print()

                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                            RELATÓRIO CONCLUÍDO                             ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)                
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                input("\tAPERTE >ENTER< PARA CONTINUAR ") 
            else:
                 print('\tTurma inexistente')
                 input("\tAPERTE >ENTER< PARA CONTINUAR ") 

        elif opcao2 == 2:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                            CHOQUE DE HORÁRIOS                              ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            senha_acesso = input('\tDigite a sua senha de acesso: ').strip()
            
            if senha_acesso in professores:
                senha_encontrada = True

            if senha_encontrada:
                nome_professor = input('\tDigite o seu nome: ').strip()
                dia = input('\tDigite o dia da aula: ').strip()
                horario = input('\tDigite o horário da aula: ').strip()
                print()

                for turma in serie:
                    print(professores[senha_acesso][-1])
                    print(serie[turma]['professores'][-1])
                    qntd_professores = len(serie[turma]['professores'])

                    for i in range(qntd_professores):
                        if professores[senha_acesso][-1] == serie[turma]['professores'][i][-1]:
                            professor_encontrado = True
                            
                            qntd_horarios = len(serie[turma]['horarios'])
                            for j in range(qntd_horarios):
                                if horario == serie[turma]['horarios'][j][0] and dia == serie[turma]['horarios'][j][1]:
                                    horario_encontrado = True
                                    print('Turma: {}'.format(turma))
                                    print('\tHorário: {}'.format(serie[turma]['horarios'][j][0]))
                                    print('\tDia: {}'.format(serie[turma]['horarios'][j][1]))
                                    print('\tMatéria: {}'.format(serie[turma]['horarios'][j][-1]))
                                    print()
                                    soma_horarios += 1

                                    print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                                    print(cor_do_terminal+"║                                                                            ║"+reset)
                                    print(cor_do_terminal+"║                            RELATÓRIO CONCLUÍDO                             ║"+reset)
                                    print(cor_do_terminal+"║                                                                            ║"+reset)                
                                    print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                                    print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                                    print(cor_do_terminal+"║                                                                            ║"+reset)
                                    print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                                    print(cor_do_terminal+"║                                                                            ║"+reset)
                                    print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                                    input("\tAPERTE >ENTER< PARA CONTINUAR ") 
                            
                                
                    if not professor_encontrado:
                        print('\tProfessor não encontrado')
                        input("\tAPERTE >ENTER< PARA PULAR ")

                    elif not horario_encontrado:
                        print('\tHorário não encontrado')
                        input("\tAPERTE >ENTER< PARA PULAR ")

                    if soma_horarios == 1:
                        print('\tVocê não apresenta choque de horários')
                        input("\tAPERTE >ENTER< PARA PULAR ")
                    elif soma_horarios > 1:
                        print('\tVocê apresenta choque de horários')
                        input("\tAPERTE >ENTER< PARA PULAR ")
                    