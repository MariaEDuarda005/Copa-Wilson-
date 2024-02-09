import random

cartas =  [1,2,3,4,5,6,7,8,9,10,11]
naipe =["paus","ouro","espadas","copas"]
cartas_originais=[]
naipes_original = []

# carta_escolhida = random.choice(cartas)
# naipe_escolhido = random.choice(naipe)



def sortear_carta():
    carta_escolhida = random.choice(cartas)
    return carta_escolhida

def sortear_naipe():
    naipe_escolhido = random.choice(naipe)
    return naipe_escolhido

def sortear_baralho():
    mao_jogador={}
    
    while len(mao_jogador)<3:
        mao_jogador[sortear_carta()] = sortear_naipe()

    # for chave, valor in mao_jogador.items():
    #     cartas_originais.append(chave)
    #     naipes_original.append(valor)
    return mao_jogador


def separar_naipes(lista):
    separados = []
    for chave, valor in lista.items():
        cartas_originais.append(chave)
        naipes_original.append(valor)
        
        separados.append(naipes_original)
    return separados

def separar_cartas(lista):
    separados = []
    for chave, valor in lista.items():
        cartas_originais.append(chave)
        naipes_original.append(valor)
        
        separados.append(cartas_originais)
    return separados


def tratamento_cartas(lista):
    lista_tratada = [ ]
    for i in range(3):
        if lista[i] == 1:
            lista_tratada.append("4")
        if lista[i] == 2:
            lista_tratada.append("5")
        if lista[i] == 3:
            lista_tratada.append("6")
        if lista[i] == 4:
            lista_tratada.append("7")
        if lista[i] == 5:
            lista_tratada.append("Q")
        if lista[i] == 6:
            lista_tratada.append("J")
        if lista[i] == 7:
            lista_tratada.append("K")
        if lista[i] == 8:
            lista_tratada.append("A")
        if lista[i] == 9:
            lista_tratada.append("2")
        if lista[i] == 10:
            lista_tratada.append("3")

    return lista_tratada

def tratamento_naipe(lista):
    #"paus","ouro","espadas","copas"
    lista_tratada = [ ]
    for i in range(3):
        if lista[i] == "paus":
            lista_tratada.append(4)
        if lista[i] == "copas":
            lista_tratada.append(3)
        if lista[i] == "espadas":
            lista_tratada.append(2)
        if lista[i] == "ouro":
            lista_tratada.append(1)

    return lista_tratada

test= print(type(sortear_baralho()))
jogador1 = sortear_baralho()
testando = print(separar_cartas(jogador1))


