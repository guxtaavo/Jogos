import os
from random import randrange
import sys

class JogoDaForca:
    def _exibir_a_mensagem_inicial():
        os.system('cls')
        print('𝕁𝕆𝔾𝕆 𝔻𝔸 𝔽𝕆ℝℂ𝔸')
        print('Olá, você escolheu a opção de jogar o jogo da forca!')

    def _valida_a_opcao(opcao):
        while True:
            if opcao in [1, 2]:
                match opcao:
                    case 1:
                        print('Você escolheu o tema futebol...\n')
                        return 1
                    case 2: 
                        print('Você escolheu o tema frutas...\n')
                        return 2
            else:
                opcao = int(input('Você digitou uma opção inválida, porfavor, digite novamente: '))

    def _abrir_o_arquivo(tema):
        arquivo = open(f'modelos/listas_jogo_da_forca/{tema}.txt', 'r')
        palavras = []
        for linha in arquivo:
            # O STRIP REMOVE OS CARACTERES ESPECIAIS, TAL COMO O \n
            linha = linha.strip()
            palavras.append(linha)
        arquivo.close()
        print(palavras)
        return palavras

    def _exibir_mensagem_final_de_jogo():
        print()
        print('*'*20)
        print('1. Jogar novamente')
        print('2. Sair')
        print('*'*20)
        print()
        try:
            loop = True
            while loop:
                escolha = int(input('Deseja jogar novamente ou sair: '))
                if escolha in [1,2]:
                    if escolha == 1:
                        os.system('cls')
                        JogoDaForca.rodar_o_jogo()
                    else:
                        print('Volte mais vezes! Até a próxima...')
                        loop = False
                else:
                    escolha = int(input('Você digitou uma opção inválida, tente novamente: '))
        except:
            print('Você digitou algo inválido. Tente novamente mais tarde.')
    
    def _jogar(opcao):
        if opcao == 1:
            tema = 'futebol'
        else:
            tema = 'frutas'
        try:
            palavras = JogoDaForca._abrir_o_arquivo(tema)
            numero = randrange(0, len(palavras))
            palavra_secreta = palavras[numero].upper()
            exibir_a_palavra = palavra_secreta
            palavra_secreta = palavra_secreta.replace(' ', '')
            letras_corretas = ['_' for letra in palavra_secreta]
            vidas = 6
            while (vidas != 0):
                os.system('cls')
                print(letras_corretas)
                print(f'Vidas restantes: [{vidas}]')
                chute = input('Qual a letra ? ').upper().strip()
                posicao = 0                    
                if chute in palavra_secreta:
                    for letra in palavra_secreta:
                        if chute == letra:
                            letras_corretas[posicao] = chute
                        posicao += 1
                    if not '_' in letras_corretas:
                        os.system('cls')
                        print(f'PARABÉNSSS!!!! VOCÊ GANHOU!!!\nA palavra correta era: {exibir_a_palavra}')
                        vidas = 0
                        JogoDaForca._exibir_mensagem_final_de_jogo()
                else:
                    print('Letra não encontrada.')
                    vidas -= 1
                    if (vidas == 0):
                        os.system('cls')
                        palavra_secreta = palavra_secreta.title()
                        print(f'Game over! Você é grená e foi enforcado.\nA palavra correta era: {exibir_a_palavra}')
                        JogoDaForca._exibir_mensagem_final_de_jogo()
                
        except:
            print('Erro ao abrir o arquivo.')

            
    def _escolha_do_tema():
        print('1. Futebol')
        print('2. Frutas')
        try:
            opcao = int(input('Por favor, escolha a opção desejada: '))
            opcao_validada = JogoDaForca._valida_a_opcao(opcao)
        except:
            print(f'Você digitou algo inválido. Porfavor, tente novamente mais tarde.')
        else:
            JogoDaForca._jogar(opcao_validada)
            

    @staticmethod
    def rodar_o_jogo():
        JogoDaForca._exibir_a_mensagem_inicial()
        JogoDaForca._escolha_do_tema()
