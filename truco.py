import random


class Maquina:
    def __init__(self, pontos_total):
        self.pontos_total = pontos_total
        self.__cartasmao = []


class Jogador:
    def __init__(self, nome, idade, pontos_total, saldo):
        self.nome = nome
        self.idade = idade
        self.pontos_total = pontos_total
        self.cartasmao = []
        self.saldo = saldo

class Pares(object):
    par_um_id = 'par_um'
    par_dois_id = 'par_dois'

    def __init__(self, id_pair, players):
        self.id_pair = id_pair
        self.players = players

    players = {}.fromkeys(['jogador1','jogador1'],'player')


def aposta():
    print("Lancem suas apostas")
    aposta_jogador_1 = float("Jogador 1, quanto deseja apostar?\n")
    if aposta_jogador_1 > jogador1.saldo:
        print("Valor de aposta inválido!")

    aposta_jogador_2 = float("Jogador 2, quanto deseja apostar?\n")
    if aposta_jogador_2 > jogador2.saldo:
        print("Valor de aposta inválido!")

    aposta_jogador_3 = float("Jogador 3, quanto deseja apostar?\n")
    if aposta_jogador_3 > jogador3.saldo:
        print("Valor de aposta inválido!")

    aposta_jogador_4 = float("Jogador 4, quanto deseja apostar?\n")
    if aposta_jogador_4 > jogador1.saldo:
        print("Valor de aposta inválido!")
    


jogadores = []
quantidade_jogadores = int(input("Insira a quantidade de jogadores (1 - 4): "))

if quantidade_jogadores == 1:
    nome = input("Insira seu nome\n")
    idade = int(input("Insira sua idade\n"))
    saldo = float(input("Insira seu saldo\n"))
    jogador1 = Jogador(nome, idade, 0, saldo)


if quantidade_jogadores == 4:
    nome = input("Insira o nome do Jogador 1 da Dupla 1\n")
    idade = int(input("Insira sua idade\n"))
    saldo = float(input("Insira seu saldo\n"))
    jogador1 = Jogador(nome, idade, 0, saldo)
    jogadores.append(jogador1)
    
    nome = input("Insira o nome do Jogador 2 da Dupla 1\n")
    idade = int(input("Insira sua idade\n"))
    saldo = float(input("Insira seu saldo\n"))
    jogador2 = Jogador(nome, idade, 0, saldo)
    jogadores.append(jogador2)

    nome = input("Insira o nome do Jogador 1 da Dupla 2\n")
    idade = int(input("Insira sua idade\n"))
    saldo = float(input("Insira seu saldo\n"))
    jogador3 = Jogador(nome, idade, 0, saldo)
    jogadores.append(jogador3)

    nome = input("Insira o nome do Jogador 2 da Dupla 2\n")
    idade = int(input("Insira sua idade\n"))
    saldo = float(input("Insira seu saldo\n"))
    jogador4 = Jogador(nome, idade, 0, saldo)
    jogadores.append(jogador4)

    par1 = {'jogador1': jogador1, 'jogador2': jogador2}
    par_um = Pares(Pares.par_um_id, par1)

    par2 = {'jogador1': jogador3, 'jogador2': jogador4}
    par_dois = Pares(Pares.par_dois_id, par2)

    if jogador1.idade >= 18 and jogador2.idade >= 18 and jogador3.idade >=18 and jogador4.idade >= 18:
        aposta()
    
    else:
        print("Hmmm parece que vocês não poderão apostar hoje! :(")

else:
    print("Número Inválido")

 



