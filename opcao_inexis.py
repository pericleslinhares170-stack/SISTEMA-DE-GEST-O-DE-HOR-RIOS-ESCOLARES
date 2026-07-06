cor_do_terminal = "\033[1;92;47m"  # 1=Negrito, 92=Verde Claro, 47=Fundo Branco
reset = "\033[0m"
def option_ine():
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