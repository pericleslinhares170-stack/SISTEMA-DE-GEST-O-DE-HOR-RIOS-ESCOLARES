from random import randint
from pickle import dump, load

from validacao_email import verificacao
from validacao_telefone import validacao
from validacao_data_nasc import certification

cor_do_terminal = "\033[1;92;47m"  # 1=Negrito, 92=Verde Claro, 47=Fundo Branco
reset = "\033[0m"
def modulo_direcao(professores, alunos, serie):
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
    
                Arq_series = open('series.txt', 'wb')
                dump(serie, Arq_series)
                Arq_series.close()



                print('Essas são as turmas atualizadas: {}'.format(serie))
                print()
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                         TURMA CRIADA COM SUCESSO                           ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)                
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
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
                print('\tEssa é a série: {}'.format(chave))
                print('\tEssa é a sala da série: {}'.format(serie[chave]['sala']))
                print('\tEssa é a capacidade da sala: {}'.format(serie[chave]['capacidade']))
                print()

            print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"║                       TURMAS LISTADAS COM SUCESSO                          ║"+reset)
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
        

                    Arq_series = open('series.txt', 'wb')
                    dump(serie, Arq_series)
                    Arq_series.close()

                    print(f'\tNova capacidade: {serie[turma]['capacidade']}')
                    print()
                    print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                    print(cor_do_terminal+"║                                                                            ║"+reset)
                    print(cor_do_terminal+"║                     ALTERAÇÃO DA CAPACIDADE CONCLUÍDA                      ║"+reset)
                    print(cor_do_terminal+"║                                                                            ║"+reset)                
                    print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                    print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                    print(cor_do_terminal+"║                                                                            ║"+reset)
                    print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                    print(cor_do_terminal+"║                                                                            ║"+reset)
                    print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")
                else:
                    print('\tEssa turma não está cadastrada')
                    input("\tAPERTE >ENTER< PARA CONTINUAR ")

            elif opcao3 == 2:
                turma = input('\tDigite a turma que deseja alterar a sala: ').strip()

                if turma in serie:
                    nova_sala = input('\tDigite a nova sala: ').strip()
                    serie[turma]['sala'] = [nova_sala]

              
                    Arq_series = open('series.txt', 'wb')
                    dump(serie, Arq_series)
                    Arq_series.close()


                    print(f'\tEssa é a nova sala de aula: {serie[turma]['sala']} ')
                    print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                    print(cor_do_terminal+"║                                                                            ║"+reset)
                    print(cor_do_terminal+"║                       ALTERAÇÃO DE SALA CONCLUÍDA                          ║"+reset)
                    print(cor_do_terminal+"║                                                                            ║"+reset)                
                    print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                    print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                    print(cor_do_terminal+"║                                                                            ║"+reset)
                    print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                    print(cor_do_terminal+"║                                                                            ║"+reset)
                    print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
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

            print()

            if turma in serie:
                del serie[turma]
        
                Arq_series = open('series.txt', 'wb')
                dump(serie, Arq_series)
                Arq_series.close()


                for chave in serie: 
                    
                    print('Turma: {}'.format(chave)) 
                    print('Professores: {}'.format(serie[chave]['professores']))
                    print('Alunos: {}'.format(serie[chave]['alunos']))
                    print('Horários: {}'.format(serie[chave]['horarios']))
                    print('Capacidade: {}'.format(serie[chave]['capacidade']))
                    print('Sala: {}'.format(serie[chave]['sala']))
                    print()
                
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                       REMOÇÃO DE TURMA CONCLUÍDA                           ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)                
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
                print(cor_do_terminal+"╔════════════════════════════════════════════════════════════════════════════╗"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"║                 \u26A0 Atenção! Isso é apenas uma simulação!                    ║"+reset)
                print(cor_do_terminal+"║                                                                            ║"+reset)
                print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
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
            print(cor_do_terminal+"║                 \U0001F6A9 VOLTE AO MENU PRINCIPAL E REFAÇA A OPERAÇÃO             ║"+reset)
            print(cor_do_terminal+"║                                                                            ║"+reset)
            print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)