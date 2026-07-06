from pickle import dump, load
def exibir_menu_principal(serie,alunos,professores):
    cor_do_terminal = "\033[1;92;47m"  # 1=Negrito, 92=Verde Claro, 47=Fundo Branco
    reset = "\033[0m"

    
    
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
    print(cor_do_terminal+"║   [5] Relatório do Sistema                                                 ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"║   [0] Sair do Sistema                                                      ║"+reset)
    print(cor_do_terminal+"║                                                                            ║"+reset)
    print(cor_do_terminal+"╚════════════════════════════════════════════════════════════════════════════╝"+reset)
    

    return serie, alunos, professores