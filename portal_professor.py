from random import randint
from validacao_email import verificacao
from validacao_telefone import validacao
from validacao_data_nasc import certification
from pickle import dump, load
def prof_portal(professores, alunos, serie):
    
    cor_do_terminal = "\033[1;92;47m"  # 1=Negrito, 92=Verde Claro, 47=Fundo Branco
    reset = "\033[0m"


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
    
    print(professores)
    print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
    print(cor_do_terminal+"║                           PORTAL DO PROFESSOR                              ║"+reset)
    print(cor_do_terminal+"╠════════════════════════════════════════════════════════════════════════════╣"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [1] Cadastro do Professor                                                ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [2] Cadastro do Professor na Turma                                       ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [3] Cadastro de Horários                                                 ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [4] Exclusão de Aulas                                                    ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [5] Minhas Turmas                                                        ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [6] Atualizar Dados do Professor                                         ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
    
    opcao2 = int(input("\tDigite a opção que deseja acessar: "))
        
    if opcao2 == 1:
        
           
        print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"║                           CADASTRO DO PROFESSOR                            ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        nome = input("\tDigite o nome do professor: ").strip().title()    
        print()

        while True:
            data_nasc = input('\tDigite a sua data de nascimento(xx/xx/xxxx): ').strip()
            print()
            if certification(data_nasc) == True:
                break
            else:
                print('\t[Error] Data inválida!')
                input("\tAPERTE >ENTER< PARA CONTINUAR")

        while True:
                telefone = input('\tDigite o seu telefone para contato: ').strip()
                print()
                if validacao(telefone) == True:
                    break
                else:
                    print('\t[Error] Telefone inválido')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")
                    print()

        while True:
                email = input("\tDigite o email do professor: ").strip()
                print()
                if verificacao(email) == True:
                    break
                else:
                    print('\t[Error] Email inválido. Digite um email com @ e um domíno válido, como .com')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")
                    print()

        disciplina = input("\tDigite a disciplina que irá lecionar: ").strip().title()
        print()

        digito = randint(1001,9999)
        digito_str = str(digito)
        while digito_str in professores:
            digito = randint(1001,9999)
            digito_str = str(digito)

        professores[digito_str] = [nome, data_nasc, telefone, email, disciplina]

        Arq_professores = open('professores.txt', 'wb')
        dump(professores, Arq_professores)
        Arq_professores.close()     

        print('\tEssa é sua senha de acesso para o programa: {}'.format(digito_str))
            
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
        print(cor_do_terminal+"║                   CADASTRO DO PROFESSOR NA TURMA                           ║"+reset)
        print(cor_do_terminal+"║                                                                            ║"+reset)
        print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
        senha_acesso = input('\tDigite a sua senha de acesso: ').strip()
        print()
        if senha_acesso in professores:
            turma = input('\tDigite a turma: ').strip()

            if turma in serie:
                serie[turma]['professores'].append(professores[senha_acesso])

                Arq_series = open('series.txt', 'wb')
                dump(serie, Arq_series)
                Arq_series.close()

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
            else:
                print('\tTurma não encontrada')
                input("\tAPERTE >ENTER< PARA CONTINUAR ")
        else:
            print('\tSenha não encontrada')
            input("\tAPERTE >ENTER< PARA CONTINUAR ")


    elif opcao2 == 3:

            
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                           CADASTRO DE HORÁRIOS                             ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)

            nome_professor = input('\tDigite o nome do professor: ').strip().title()
            print()
            turma = input("\tDigite a turma da aula: ").strip()
            print()
            materia = input('\tDigite a matéria que será lecionada: ').strip().title()
            print()
            dia = input('\tDigite o dia da aula: ').strip().title()
            print()
            horario = input("\tDigite o horário de começo da aula: ").strip()
            print()
            senha = input('\tDigite a sua chave de acesso: ').strip()
            
            
            
            chave_cadastrada = False
            for chave in professores:
                if senha == chave:
                        chave_cadastrada = True
                        qntd_prof = len(serie[turma]['professores'])
                        professor_cadastrado = False
                        for i in range(qntd_prof):
                            
                            if nome_professor in serie[turma]['professores'][i]:
                                professor_cadastrado = True
                                serie[turma]['horarios'].append([ horario, dia, materia])
                                serie[turma]['horarios'].sort()
                                print('Horários do {}: {}'.format(turma, serie[turma]['horarios']))

                                Arq_series = open('series.txt', 'wb')
                                dump(serie, Arq_series)
                                Arq_series.close()

                                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                                print(cor_do_terminal+"║                                                                            ║"+reset)
                                print(cor_do_terminal+"║                      CADASTRO DE HORÁRIOS CONCLUÍDO                        ║"+reset)
                                print(cor_do_terminal+"║                                                                            ║"+reset)
                                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                                print(cor_do_terminal+"║                                                                            ║"+reset)
                                print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                                print(cor_do_terminal+"║                                                                            ║"+reset)
                                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                                input("\tAPERTE >ENTER< PARA CONTINUAR ")
                                break

                        if not professor_cadastrado:
                            print('\tO professor não está cadastrado na turma')
                            input("\tAPERTE >ENTER< PARA CONTINUAR ")

            if not chave_cadastrada:
                print('\tNão temos professor com esse nome')
                input("\tAPERTE >ENTER< PARA CONTINUAR ")

            

    elif opcao2 == 4:
            
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                           EXCLUSÃO DE HORÁRIOS                             ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            nome_professor = input('\tDigite o nome do professor: ').strip().title()
            print()
            turma = input("\tDigite a turma da aula: ").strip()
            print()
            disciplina = input("\tDigite o nome da disciplina: ").strip().title()
            print()
            horario = input("\tDigite o horário que a aula iria começar: ").strip()
            print()
            senha_acesso = input('\tDigite a sua chave de acesso: ').strip()

            
            senha_encontrada = False
            disciplina_encontrada = False
            if turma in serie and senha_acesso in professores:
                senha_encontrada = True
                
                for aula in serie[turma]['horarios']:

                    if aula[0] == horario and aula[2] == disciplina:
                        disciplina_encontrada = True

                        serie[turma]['horarios'].remove(aula)
                        print(f'Essas são as aulas da turma: {serie[turma]['horarios']}')
                        Arq_series = open('series.txt', 'wb')
                        dump(serie, Arq_series)
                        Arq_series.close()

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

                if not disciplina_encontrada:
                    print('\tNão tem essa disciplina e horário cadastrada na turma')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")

            if not senha_encontrada:
                print('\tNão existe essa turma e senha')
                input("\tAPERTE >ENTER< PARA CONTINUAR ")

            
    elif opcao2 == 5:
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                             MINHAS TURMAS                                  ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            
            nome_professor = input('\tDigite o nome do professor: ').strip().title()
            print()
            disciplina = input("\tDigite a disciplina: ").strip().title()
            print()
            senha_acesso = input('\tDigite a sua senha de acesso: ').strip()

        
            turma_encontrada = False
            professor_encontrado = False

            for senha in professores:
                 if senha == senha_acesso:
                    professor_encontrado = True
                    for chave, dados_serie in serie.items():
                        for professor in dados_serie['professores']:
                            if professor[0] == nome_professor and professor[-1] == disciplina:
                                print('\tEssa é sua turma: {}'.format(chave))
                                print()
                                turma_encontrada = True
                        
            if not professor_encontrado:
                    print('\tProfessor não encontrado')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ") 

                    if not turma_encontrada:
                        print('\tO professor não está cadastrado em nenhuma turma')
                        input("\tAPERTE >ENTER< PARA CONTINUAR ")    
                
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                     VERIFICAÇÃO DE TURMAS CONCLUÍDA                        ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                            
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            print()
            input("\tAPERTE >ENTER< PARA CONTINUAR ")

    elif opcao2 == 6:
            
            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                    ATUALIZAÇÃO DE DADOS DO PROFESSOR                       ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
            print()
            nome_professor = input('\tDigite o nome do professor: ').strip().title()
            print()
            disciplina = input('\tDigite a disciplina que leciona: ').strip().title()
            print()
            matricula_professor = input('\tDigite a sua chave: ').strip()
            print()
           
            senha_encontrada = False
            for chave in professores:
                if matricula_professor == chave:
                    senha_encontrada = True

                    if professores[matricula_professor][0] == nome_professor and professores[matricula_professor][-1] == disciplina:
                        novo_nome = input('\tDigite o novo nome: ').strip().title()
                        print()

                        while True: 
                            email = input('\tDigite o novo email: ').strip()
                            verificacao(email)
                            print()

                            if verificacao(email) == True:
                                break
                            else:
                                print('\tEmail inválido. Tente novamente')
                                input("\tAPERTE >ENTER< PARA PULAR ")
                        nova_disciplina = input('\tDigite a disciplina atualizada: ').strip().title()
                        
                        professores[matricula_professor] = [novo_nome,email,nova_disciplina]

                        Arq_professores = open('professores.txt', 'wb')
                        dump(professores, Arq_professores)
                        Arq_professores.close()

                        print()
                        print('\tLista dos professores com os dados atualizados: {}'.format(professores))

                        print()
                        print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                        print(cor_do_terminal+"║                                                                            ║"+reset)
                        print(cor_do_terminal+"║                     DADOS ATUALIZADOS COM SUCESSO                          ║"+reset)
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
                        print('\t[Error] Dados errados')
                        input("\tAPERTE >ENTER< PARA PULAR")  
            if not senha_encontrada:
                print('\tMatrícula inexistente')  
                input("\tAPERTE >ENTER< PARA PULAR")  


    elif opcao2 > 6:
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
    return serie, alunos, professores