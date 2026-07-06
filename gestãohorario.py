from random import randint
from pickle import dump, load

from validacao_email import verificacao
from validacao_telefone import validacao
from validacao_data_nasc import certification

from menu_principal import exibir_menu_principal
from portal_professor import prof_portal
from modulo_aluno import portal_alunos
from menu_direcao import modulo_direcao
from sistema_info import info_system
from opcao_inexis import option_ine
from termino_prog import finish_program
from relatorio import option_relatory

cor_do_terminal = "\033[1;92;47m"  # 1=Negrito, 92=Verde Claro, 47=Fundo Branco
reset = "\033[0m"
        
professores = { '1001' : ['Orlanildo', 'orlanildo@gmail.com', 'Português'], 
                '1002' : ['Cleilson','cleilson@gmail.com', 'Ciências']}

alunos = {'20260000' : ['Péricles Rafael', '16/09/2009', 'pericles@gmail.com'],
          '20260001' : ['Pedro', '17/04/2017', 'pedro@gmail.com']}

serie = {'1ano' : {'professores' : [['Orlanildo', 'orlanildo@gmail.com', 'Português']], 'alunos' : [['Péricles Rafael', '16/09/2009', 'pericles@gmail.com'],['Pedro', '17/04/2017', 'pedro@gmail.com']], 'horarios': [['13:00','Segunda', 'História']], 'capacidade': ['30 alunos'], 'sala':['A1']},
                   '2ano' : {'professores' : [['Orlanildo', 'orlanildo@gmail.com', 'Português'],['Cleilson','cleilson@gmail.com', 'Ciências']], 'alunos' : [['Pedro', '17/04/2017', 'pedro@gmail.com']], 'horarios': [['13:00','Segunda', 'História'], ['14:00', 'Terça', 'Português'], ['14:55', 'Segunda', 'Português']], 'capacidade': ['45 alunos'], 'sala':['A2']}}

opcao = ''
while opcao != 0: 
    exibir_menu_principal(serie,alunos,professores)
    opcao = int(input("\tDigite a opção que deseja acessar: "))
    print()
    
    if opcao == 1:
        prof_portal(professores, alunos, serie)
        
    elif opcao == 2:
        portal_alunos(professores, alunos, serie)
    
    elif opcao == 3:
        modulo_direcao(professores, alunos, serie)

    elif opcao == 4:
        info_system()

    elif opcao == 5:
        option_relatory(serie, professores, alunos)
                                 
    elif opcao > 5:
        option_ine()
finish_program()