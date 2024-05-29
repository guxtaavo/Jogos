from modelos.jogo_da_adivinhacao import JogoDaAdivinhacao
from modelos.jogo_da_forca import JogoDaForca
from modelos.pong.pong_game import PongGame
import os

class Menu:
    def _exibir_a_mensagem_inicial(self):
        print('*'*28)
        print('▀▄▀▄▀▄★彡[ᴊᴏɢᴏꜱ]彡★▀▄▀▄▀▄')
        print('*'*28)


    def _valida_a_opcao(self, opcao):
        while True:
            if opcao in [1, 2, 3, 4]:
                match opcao:
                    case 1:
                        return JogoDaAdivinhacao.rodar_o_jogo()
                    case 2: 
                        return JogoDaForca.rodar_o_jogo()
                    case 3: 
                        return print('Jogo da velha')
                    case 4: 
                        return PongGame.rodar_o_jogo()
                    case 5:
                        return print('Saindo do programa... Volte sempre!')

            else:
                opcao = int(input('Você digitou uma opção inválida, porfavor, digite novamente: '))

    
    def _escolher_o_jogo(self):
        print('Seja bem-vindx!!!')
        print('1. Adivinhe o número')
        print('2. Forca')
        print('3. Jogo da velha')
        print('4. Pong')
        print('5. Sair')
        try:
            opcao_escolhida = int(input('Por favor, escolha a opção desejada: '))
            self._valida_a_opcao(opcao_escolhida)
        except:
            print(f'Você digitou algo inválido. Porfavor, tente novamente mais tarde.')

    def exibir_o_menu(self):
        self._exibir_a_mensagem_inicial()
        self._escolher_o_jogo()
        