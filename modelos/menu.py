class Menu:

    @staticmethod
    def exibir_a_mensagem_inicial():
        print('*'*28)
        print('▀▄▀▄▀▄★彡[ᴊᴏɢᴏꜱ]彡★▀▄▀▄▀▄')
        print('*'*28)


    @staticmethod
    def valida_a_opcao():
        pass

    @staticmethod
    def escolher_o_jogo():
        print('Seja bem-vindx!!!')
        print('1. Adivinhe o número')
        print('2. Forca')
        print('3. Jogo da velha')
        print('4. Sair')
        opcao_escolhida = int(input('Por favor, escolha a opção desejada: '))

        while True:
            if opcao_escolhida in [1, 2, 3, 4]:
                print('validado')
                break

            else:
                opcao_escolhida = int(input('Você digitou uma opção inválida, porfavor, digite novamente.'))

    @staticmethod
    def exibir_o_menu():
        Menu.exibir_a_mensagem_inicial()
        Menu.escolher_o_jogo()
        