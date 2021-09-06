"""
PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
CURSO: BIG DATA E INTELIGÊNCIA ANALÍTICA
Disciplina: Raciocíneo Computacional
aluna: Cintia Eitelwein
"""
import random
import time

#Identificação dos Jogadores
print("ZOMBIE, seja bem-vindo!")
numJogadores = 0
while (numJogadores < 2):
    numJogadores = int(input("Informe o número de ZOMBIES jogadores: "))
    if (numJogadores <2):
        print("O número de ZOMBIE jogadores deve ser maior ou igual a 2!\n")

listajogadores = []
for i in range(numJogadores):
    nome = input("Informe o nome do Zombie jogador " + str(i+1)+": ")
    listajogadores.append(nome)
print(listajogadores)

#Os dados
Verde = 0
Amarelo = 0
Vermelho = 0

cerebros = 0
passos = 0
tiros = 0

dadoVerde = "CPCTCP";
dadoAmarelo = "TCPTCP";
dadoVermelho = "TPTCPT";

listadados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
              dadoAmarelo,dadoAmarelo,dadoAmarelo,dadoAmarelo,
              dadoVermelho, dadoVermelho, dadoVermelho];

#Iniciando o Jogo
print("Vamos começar! \n")
time.sleep(1)

jogador = 0
dadosSorteados = []
turnoFinalizado = False

#Tirando os dados
for jogador in listajogadores:
    turnoFinalizado = False
    while not turnoFinalizado:
        print("O jogador da vez é: ", jogador)
        time.sleep(2)
        for i in range(3):
            dadosSorteados = random.choice (listadados)
            listadados.remove(dadosSorteados)
            if dadosSorteados == "TCPTCP":
                 print("Dado Amarelo")
            elif dadosSorteados == "CPCTCP":
                 print("Dado Verde")
            else:
                 print("Dado Vermelho")

            faceSorteada = random.choice(dadosSorteados)
            if faceSorteada == "C":
                 print("CÉREBRO")
                 cerebros = cerebros + 1
            elif faceSorteada == "P":
                 print("Passos")
                 passos = passos + 1
            elif faceSorteada == "T":
                 print("Tiros")
                 tiros = tiros + 1
            print("A quantidade de cérebros é: ", cerebros)
            print("A quantidade de passos é: ", passos)
            print("A quantidade de tiros é:", tiros)
        opcao = input("deseja continuar jogando(s/n)?")
        if opcao == "n":
            turnoFinalizado = True


