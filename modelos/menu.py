from modelos.jogo_da_adivinhacao import JogoDaAdivinhacao
from modelos.jogo_da_forca import JogoDaForca
import os

class Menu:
    def _exibir_a_mensagem_inicial():
        print('*'*28)
        print('▀▄▀▄▀▄★彡[ᴊᴏɢᴏꜱ]彡★▀▄▀▄▀▄')
        print('*'*28)


    def _valida_a_opcao(opcao):
        while True:
            if opcao in [1, 2, 3, 4]:
                match opcao:
                    case 1:
                        return JogoDaAdivinhacao.rodar_o_jogo()
                    case 2: 
                        return JogoDaForca.rodar_o_jogo()
                    case 3: 
                        return print('3')
                    case 4:
                        return print('Saindo do programa... Volte sempre!')

            else:
                opcao_escolhida = int(input('Você digitou uma opção inválida, porfavor, digite novamente: '))

    
    def _escolher_o_jogo():
        print('Seja bem-vindx!!!')
        print('1. Adivinhe o número')
        print('2. Forca')
        print('3. Jogo da velha')
        print('4. Sair')
        try:
            opcao_escolhida = int(input('Por favor, escolha a opção desejada: '))
            Menu._valida_a_opcao(opcao_escolhida)
        except:
            print(f'Você digitou algo inválido. Porfavor, tente novamente mais tarde.')


    @staticmethod
    def exibir_o_menu():
        os.system('cls')
        Menu._exibir_a_mensagem_inicial()
        Menu._escolher_o_jogo()
        