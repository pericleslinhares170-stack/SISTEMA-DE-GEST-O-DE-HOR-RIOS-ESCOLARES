cor_do_terminal = "\033[1;92;47m"  # 1=Negrito, 92=Verde Claro, 47=Fundo Branco
reset = "\033[0m"

professores = { 'Orlanildo' : ['Orlanildo', 'orlanildo@gmail.com', 'Português'], 
                'Cleilson' : ['Cleilson','cleilson@gmail.com', 'Ciências']}


alunos = {'111' : ['Péricles Rafael', '16/09/2009', 'pericles@gmail.com'],
          '222' : ['Pedro', '17/04/2017', 'pedro@gmail.com']}


serie = {'1ano' : {'professores' : [professores['Orlanildo']], 'alunos' : [['Péricles Rafael', '16/09/2009', 'pericles@gmail.com'],['Pedro', '17/04/2017', 'pedro@gmail.com']], 'horarios': [['13:00','Segunda', 'História']], 'capacidade': ['30 alunos'], 'sala':['A1']},
                   '2ano' : {'professores' : [professores['Orlanildo']], 'alunos' : [['Pedro', '17/04/2017', 'pedro@gmail.com']], 'horarios': [['13:00','Segunda', 'História'], ['14:00', 'Terça', 'Português'], ['14:55', 'Segunda', 'Português']], 'capacidade': ['45 alunos'], 'sala':['A2']}}

opcao = ''
while opcao != 0: 
    
    print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║              SISTEMA DE GESTÃO DE HORÁRIOS ESCOLARES                       ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
    print(cor_do_terminal+"║                            MENU PRINCIPAL                                  ║"+reset)
    print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [1] Portal do Professor                                                  ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [2] Portal do Aluno                                                      ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [3] Portal da Direção Escolar                                            ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [4] Informações do Sistema                                               ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [0] Sair do Sistema                                                      ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
    opcao = int(input("\tDigite a opção que deseja acessar: "))
    print()
    
    if opcao == 1:
        print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
        print(cor_do_terminal+"║                           PORTAL DO PROFESSOR                              ║"+reset)
        print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [1] Cadastro do Professor                                                ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [2] Cadastro de Horários                                                 ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [3] Exclusão de Aulas                                                    ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [4] Minhas Turmas                                                        ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        opcao2 = int(input("\tDigite a opção que deseja acessar: "))
        
        if opcao2 == 1:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                           CADASTRO DO PROFESSOR                            ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)

            nome = input("\tDigite o nome do professor: ")    
            print()
            data_nasc = input('\tDigite a sua data de nascimento(xx/xx/xxxx): ')
            print()
            telefone = input('\tDigite o seu telefone para contato: ')
            print()
            email = input("\tDigite o email do professor: ")
            print()
            disciplina = input("\tDigite a disciplina que irá lecionar: ")
            print()
            qntd_turmas = int(input('\tDigite quantas turmas irá lecionar: '))

            professores[nome] = [nome, data_nasc, telefone, email, disciplina]
            for j in range(qntd_turmas):
                turma = input('Digite a turma: ')
                if turma in serie:
                    serie[turma]['professores'].append(professores[nome])
                    print()
                    print('Essa é a lista de profesores do {}: {}'.format(turma, serie[turma]['professores']))
                else: 
                    print('Não temos o {} cadastrado nas turmas'.format(turma))
            
            print()
            print(professores)
            print()
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                           CADASTRO CONCLUÍDO                               ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            input("\tAPERTE >ENTER< PARA CONTINUAR ")

        elif opcao2 == 2:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                           CADASTRO DE HORÁRIOS                             ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
      
            nome_professor = input('\tDigite o nome do professor: ').strip()
            print()
            turma = input("\tDigite a turma da aula: ").strip()
            print()
            materia = input('\tDigite a matéria que será lecionada: ').strip()
            print()
            dia = input('\tDigite o dia da aula: ').strip()
            print()
            horario = input("\tDigite o horário de começo da aula: ")
            print()
           
            if nome_professor in professores:
                    if turma in serie and nome_professor not in serie[turma]:
                        serie[turma]['horarios'].append([ horario, dia, materia])
                        serie[turma]['horarios'].sort()
                        serie[turma]['professores'].append(professores[nome_professor])
                        print(serie)
                    elif turma in serie and nome_professor in serie[turma]:
                        serie[turma]['horarios'].append([ horario, dia, materia])
                        serie[turma]['horarios'].sort()
                        print(serie)
                    else:
                        print('\tNão temos essa turma cadastrada')
            else:
                print('\tNão temos professor com esse nome')

            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                           CADASTRO CONCLUÍDO                               ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            input("\tAPERTE >ENTER< PARA CONTINUAR ")

        elif opcao2 == 3:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                           EXCLUSÃO DE HORÁRIOS                             ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            nome_professor = input('\tDigite o nome do professor: ').strip()
            print()
            turma = input("\tDigite a turma da aula: ").strip()
            print()
            disciplina = input("\tDigite o nome da disciplina: ").strip()
            print()
            horario = input("\tDigite o horário que a aula iria começar(1,6): ").strip()
            print()
            if turma in serie:
                for aula in serie[turma]['horarios']:
                    if aula[1] == disciplina and aula[2] == horario:
                        serie[turma]['horarios'].remove(aula)
                        print(serie)
            else:
                print('\tNão existe essa turma na escola')


            
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                        EXCLUSÃO DE HORÁRIOS CONCLUÍDA                      ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            input("\tAPERTE >ENTER< PARA CONTINUAR ")

        elif opcao2 == 4:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                             MINHAS TURMAS                                  ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            
            nome_professor = input('\tDigite o nome do professor: ').strip()
            print()
            disciplina = input("\tDigite a disciplina: ").strip()
            print()
            for chave, dados_serie in serie.items():
                for professor in dados_serie['professores']:
                    if professor[0] == nome_professor and professor[-1] == disciplina:
                        print(chave)
                else:
                    print('\tO professor não está cadastrado em nenhuma turma')    

            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                     VERIFICAÇÃO DE TURMAS CONCLUÍDA                      ║"+reset)
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
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                             OPÇÃO INEXISTENTE                              ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                 \U0001F6A9 VOLTE AO MENU PRINCIPAL E REFAÇA A OPERAÇÃO             ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            input("\tAPERTE >ENTER< PARA PULAR ")
    
    elif opcao == 2:
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
            matricula = input('\tDigite a matrícula do aluno: ').strip()
            print()
            nome_aluno = input('\tDigite o nome do aluno: ').title().strip()
            print()
            data_nasc = input('\tDigite a data de nascimento do aluno(xx/xx/xxxx): ').strip()
            print()
            email = input('\tDigite o email do aluno: ').strip()
            print()
            turma = input('\tDigite a turma que vai cursar: ').strip()
            print()
            if matricula not in alunos:
                alunos[matricula] = [nome_aluno, data_nasc, email]
                print(alunos)
                if turma in serie:
                    serie[turma]['alunos'].append([nome_aluno, data_nasc, email])
                    print()
                    print(serie[turma]['alunos'])
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
                    print()
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")
                else:
                    print('\tNão existe essa turma na escola')
            else:
                print('\tJá tem aluno com essa matrícula')
        
            

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
                            novo_nome = input('\tDigite o novo nome do aluno: ').strip()
                            data_nas = input('\tDigite a nova data de nascimento(xx/xx/xxxx): ').strip()
                            email = input('\tDigite o novo email do aluno: ').strip()

                            alunos[matricula] = [novo_nome, data_nas, email]
                            serie[turma]['alunos'][i] = alunos[matricula]
                            serie[turma]

                            print()
                            print(alunos)
                            print(serie[turma]['alunos'][i])
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
            nome_aluno = input('\tDigite o seu nome: ').strip()
            turma = input('\tDigite a turma que você estuda: ').strip()
            dia = input('\tDigite o dia que você quer ver a grade: ').strip()
            if matricula in alunos:
                nome_valido = alunos[matricula][0]
                lista_alunos = serie[turma]['alunos']
                tam_lista_alunos = len(lista_alunos)
                for j in range(tam_lista_alunos):
                    if lista_alunos[j][0] == nome_aluno:
                        if nome_aluno == nome_valido:
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




        else:
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
    elif opcao == 3:
        print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
        print(cor_do_terminal+"║                           PORTAL DA DIREÇÃO ESCOLAR                        ║"+reset)
        print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [1] Cadastro de Nova Turma                                               ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [2] Listar Turmas, Salas e Capacidade                                    ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [3] Alterar Dados da Sala                                                ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║   [4] Remover Turma                                                        ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        opcao2 = int(input("\tDigite a opção que deseja acessar: "))
        if opcao2 == 1:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                            CADASTRO DE NOVA TURMA                          ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            turma = input('\tDigite o nome da turma: ').strip()
            sala = input('\tDigite a sala da turma: ').strip()
            capacidade = input('\tDigite a capacidade da turma: ').strip()
            if turma not in serie:
                serie[turma] = {'professores': [], 'alunos': [], 'horários': [], 'capacidade': [capacidade], 'sala': [sala]}
                print('\tTurma cadastrada com sucesso')
                print(serie)
                input("\tAPERTE >ENTER< PARA CONTINUAR ")
            else:
                print('\tEssa turma já existe')
                input("\tAPERTE >ENTER< PARA CONTINUAR ")
        elif opcao2 == 2:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                            LISTA DE TURMAS, SALAS E CAPACIDADE             ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            for chave in serie:
                print(f'\tEssa é a série: {chave}')
                print(f'\tEssa é a sala da série: {serie[chave]['sala']}')
                print(f'\tEssa é a capacidade da sala: {serie[chave]['capacidade']}')
                print()
            input("\tAPERTE >ENTER< PARA CONTINUAR ")
        elif opcao2 == 3:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                        ALTERAR DADOS DA TURMA (SALA)                       ║"+reset)
            print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║   [1] Alteração da Capacidade da Sala                                      ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║   [2] Alteração de Sala                                                    ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            opcao3 = int(input("\tDigite a opção que deseja acessar: "))
            if opcao3 == 1:
                turma = input('\tDigite a turma que deseja alterar a capacidade: ').strip()
                if turma in serie:
                    nova_capacidade = input('\tDigite a nova capacidade: ').strip()
                    serie[turma]['capacidade'] = [nova_capacidade]
                    print('\tCapacidade alterada com sucesso')
                    print()
                    print(f'\tNova capacidade: {serie[turma]['capacidade']}')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")
                else:
                    print('\tEssa turma não está cadastrada')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")

            elif opcao3 == 2:
                turma = input('\tDigite a turma que deseja alterar a sala: ').input()

                if turma in serie:
                    nova_sala = input('\tDigite a nova sala: ').strip()
                    serie[turma]['sala'] = [nova_sala]
                    print('\tSala alterada com sucesso')
                    print()
                    print(f'\tEssa é a nova sala de aula: {serie[turma]['sala']} ')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")

                else:
                    print('\tEssa turma não está cadastrada')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")
            else:
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                             OPÇÃO INEXISTENTE                              ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                 \U0001F6A9 VOLTE AO MENU PRINCIPAL E REFAÇA A OPERAÇÃO            +reset ║")
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        elif opcao2 == 4:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                            REMOÇÃO DE TURMA                                ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            turma = input('\tDigite a turma que deseja remover: ').strip()

            if turma in serie:
                del serie[turma]
                print('\tTurma removida com sucesso')
                print()
                print(serie)  
                input("\tAPERTE >ENTER< PARA CONTINUAR ")

            else:
                print('\tTurma não existente')
                input("\tAPERTE >ENTER< PARA CONTINUAR ")

        elif opcao2 > 4:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                             OPÇÃO INEXISTENTE                              ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                 \U0001F6A9 VOLTE AO MENU PRINCIPAL E REFAÇA A OPERAÇÃO            +reset ║")
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)


    elif opcao == 4:
        print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║                         INFORMAÇÕES DO SISTEMA                             ║"+reset)
        print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
        print(cor_do_terminal+"║   SISTEMA DE GESTÃO PARA CONTROLE DE HORÁRIOS                              ║"+reset)
        print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
        print(cor_do_terminal+"║   PROGRAMADOR: PÉRICLES RAFAEL A. LINHARES                                 ║"+reset)
        print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
        print(cor_do_terminal+"║   EMAIL: pericles.linhares.170@ufrn.edu.br                                 ║"+reset)
        print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
        print(cor_do_terminal+"║   LICENÇA PÚBLICA GERAL - GNU | www.gnu.org/licenses/gpl.html              ║"+reset)
        print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        input("\tAPERTE >ENTER< PARA PULAR ")
        
    elif opcao > 4:
        print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║                             OPÇÃO INEXISTENTE                              ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║                 \U0001F6A9 VOLTE AO MENU PRINCIPAL E REFAÇA A OPERAÇÃO            +reset ║")
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        input("\tAPERTE >ENTER< PARA PULAR ")

print(cor_do_terminal+'╔════════════════════════════════════════════════════════════════════════════╗'+reset)
print(cor_do_terminal+'║                                                                            ║'+reset)
print(cor_do_terminal+'║                       O PROGRAMA FOI ENCERRADO                             ║'+reset)
print(cor_do_terminal+'║                                                                            ║'+reset)
print(cor_do_terminal+'╚════════════════════════════════════════════════════════════════════════════╝'+reset)

