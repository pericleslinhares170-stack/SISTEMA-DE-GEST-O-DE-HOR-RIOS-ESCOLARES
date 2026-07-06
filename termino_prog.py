cor_do_terminal = "\033[1;92;47m"  # 1=Negrito, 92=Verde Claro, 47=Fundo Branco
reset = "\033[0m"
def finish_program():
    print(cor_do_terminal+'╔════════════════════════════════════════════════════════════════════════════╗'+reset)
    print(cor_do_terminal+'║                                                                            ║'+reset)
    print(cor_do_terminal+'║                       O PROGRAMA FOI ENCERRADO                             ║'+reset)
    print(cor_do_terminal+'║                                                                            ║'+reset)
    print(cor_do_terminal+'╚════════════════════════════════════════════════════════════════════════════╝'+reset)