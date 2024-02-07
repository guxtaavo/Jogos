from random import randint
import os

class JogoDaAdivinhacao:
    def _exibir_a_mensagem_inicial():
        os.system('cls')
        print('𝐉𝐎𝐆𝐎 𝐃𝐀 𝐀𝐃𝐈𝐕𝐈𝐍𝐇𝐀ÇÃ𝐎')
        print('Olá, você escolheu a opção de jogar o jogo da adivinhação!')

    def _valida_a_opcao(opcao):
        while True:
            if opcao in [1, 2, 3, 4]:
                match opcao:
                    case 1:
                        print('Você escolheu o nível fácil...\n')
                        return 1
                    case 2: 
                        print('Você escolheu o nível médio...\n')
                        return 2
                    case 3: 
                        print('Você escolheu o nível díficil...\n')
                        return 3
            else:
                opcao = int(input('Você digitou uma opção inválida, porfavor, digite novamente: '))

    def _exibir_mensagem_final_de_jogo():
        print()
        print('*'*20)
        print('1. Jogar novamente')
        print('2. Sair')
        print('*'*20)
        print()
        loop = True
        try:
            while loop:
                escolha = int(input('Deseja jogar novamente ou sair: '))
                if escolha in [1,2]:
                    if escolha == 1:
                        os.system('cls')
                        JogoDaAdivinhacao.rodar_o_jogo()
                        loop = False
                    else:
                        print('Volte mais vezes! Até a próxima...')
                        loop = False
                else:
                    escolha = int(input('Você digitou uma opção inválida, tente novamente:  '))
        except:
            print('Você digitou algo inválido... tente novamente mais tarde.')
    
    def jogar(opcao):
        if opcao == 1:
            vidas = 7
        elif opcao == 2:
            vidas = 5
        else:
            vidas = 3
        
        numero_aleatorio = randint(0,100)

        chute = int(input('Porfavor, tente adivinhar o numero: '))
        loop = True

        while loop:
            if chute > numero_aleatorio:
                print('Você digitou um número maior... ')
                vidas -= 1
                if vidas != 0:
                    chute = int(input('\nPorfavor, tente adivinhar o numero: '))
                    print('')
                else:
                    os.system('cls')
                    print(f'Que pena, você não teve sorte dessa vez... O número correto era: {numero_aleatorio}.')
                    loop = False
                    JogoDaAdivinhacao._exibir_mensagem_final_de_jogo()
            elif chute == numero_aleatorio:
                os.system('cls')
                print(f'Parabéns, você é um gênio! Ganhou! O número correto era {numero_aleatorio}.')
                loop = False
                JogoDaAdivinhacao._exibir_mensagem_final_de_jogo()
            else:
                print('Você digitou um número menor... ')
                vidas -= 1
                if vidas != 0:
                    chute = int(input('\nPorfavor, tente adivinhar o numero: '))
                else:
                    os.system('cls')
                    print(f'Que pena, você não teve sorte dessa vez... O número correto era: {numero_aleatorio}.')
                    loop = False
                    JogoDaAdivinhacao._exibir_mensagem_final_de_jogo()

            

    def _escolha_da_dificuldade():
        print('1. Fácil')
        print('2. Médio')
        print('3. Dificil')
        try:
            opcao = int(input('Por favor, escolha a opção desejada: '))
            opcao_validada = JogoDaAdivinhacao._valida_a_opcao(opcao)
        except:
            print(f'Você digitou algo inválido. Porfavor, tente novamente mais tarde.')
        else:
            JogoDaAdivinhacao.jogar(opcao_validada)
            

    @staticmethod
    def rodar_o_jogo():
        numero_aleatorio = randint(0,100)
        JogoDaAdivinhacao._exibir_a_mensagem_inicial()
        JogoDaAdivinhacao._escolha_da_dificuldade()
