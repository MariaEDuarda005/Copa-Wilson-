import random

cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
naipe = ["paus", "ouro", "espadas", "copas"]

def sortear_carta():
    return random.choice(cartas)

def sortear_naipe():
    return random.choice(naipe)

def sortear_baralho(numero_jogadores):
    baralho = {}

    for jogador in range(1, numero_jogadores + 1):
        cartas_jogador = []
        for _ in range(3):
            carta = sortear_carta()
            naipe_escolhido = sortear_naipe()
            cartas_jogador.append({'Carta': carta, 'Naipe': naipe_escolhido})
        baralho[f'Jogador {jogador}'] = cartas_jogador

    return baralho

def mostrar_cartas(baralho):
    for jogador, cartas in baralho.items():
        print(f'{jogador}:')
        for carta_naipe in cartas:
            carta = carta_naipe['Carta']
            naipe = carta_naipe['Naipe']
            carta_simbolo = tratamento_cartas([carta])[0]
            # naipe_simbolo = tratamento_naipe([naipe])[0]
            print(f'  {carta_simbolo} de {naipe}')

# Funções de tratamento
def tratamento_cartas(lista):
    simbolos = {
        1: "4", 2: "5", 3: "6", 4: "7", 5: "Q", 6: "J", 7: "K", 8: "A", 9: "2", 10: "3", 11: "10"
    }
    return [simbolos[carta] for carta in lista]

def tratamento_naipe(lista):
    naipe_numerico = {"paus": 4, "copas": 3, "espadas": 2, "ouro": 1}
    return [naipe_numerico[n] for n in lista]

# Exemplo de uso
numero_jogadores = 3
baralho = sortear_baralho(numero_jogadores)
mostrar_cartas(baralho)

