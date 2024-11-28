# -*- codding: utf-8 -*-
"""
Corrida de Cavalos

@description: jogo de apostas em corridas de cavalos
@version: 0.1.1v
@author: Rúben Gaspar
"""

import random
import time

from colorama import Fore, Style, Back, init

init(autoreset=True)

# Pedir o número de jogadores
#Número por jogador
# o computador tem de gerar um número alea
# o jogador tem de inserir uma aposta           

def numero_de_jogadores() -> int: 
    """
    Pede o número de jogadores via entrada do usuário

    Returns:
        qtdDeJogadores: A quantidade de jogadores

    """
    
    #O loop corre até obter uma resposta válida
    while True:
        try:
            qtdDeJogadores = int(input(f"{Fore.BLUE}👥 ~ Digite o número de jogadores (1 ou 2): "))
            print("       ")
            if qtdDeJogadores == 1:
                print(f"{Fore.GREEN} ✅ Bem vindo ao jogo! ✅")
                print(" ")
                return qtdDeJogadores
            elif qtdDeJogadores == 2:
                print(f"{Fore.GREEN} ✅ Bem vindos ao jogo! ✅")
                print(" ")
                return qtdDeJogadores
            else:
                print(f"{Fore.RED} ⚠ Escolha inválida! O jogo suporta apenas 1 ou 2 jogadores. ⚠")
                print(" ")
        except ValueError:
            print(f"{Fore.RED}⛔Por favor, insira 1 ou 2.⛔")
            print(" ")

def nome_e_saldo_do_jogador(ndoJogador) -> dict :
    """
    Pede o nome e o saldo inicial do jogador.

    Args:
        ndoJogador (int): número do jogador.

    Returns
        dict: Informações do jogador contendo nome, saldo, pontos, aposta e cavalo.
    
    """

    # Permite o usuário digitar o nome e introduzir o seu saldo.
    # Mostra também uma mensagem de erro quando o saldo é inválido
    nome = input(f"{Fore.CYAN}🖊️ Olá Jogador {ndoJogador}, digite o seu nome : ").strip()
    while True:
        try:
            saldo = float(input(f"{Fore.CYAN}💸 Digite o saldo inicial do jogador {ndoJogador} (mínimo 100€): "))
            if saldo >= 100:
                return {"nome": nome, "saldo": saldo, "pontos": 0, "aposta": 0, "cavalo": ""}
            else:
                print(f"{Fore.RED}❌ Saldo insuficiente! O saldo inicial deve ser no mínimo €100.❌")
        except ValueError:
            print(f"{Fore.LIGHTYELLOW_EX}⚠ Por favor, insira um valor numérico válido. ⚠")
    
def apostar(jogador):
    """
    Pede o valor da aposta via entrada do jogador

    Args:
        jogador: O jogador individual
    
    Returns:
        aposta: O valor da aposta.

    """
    #Permite o usuário apostar com um minimo de 100 €while True:
    while True:
        try:
            aposta = int(input(f"{Fore.LIGHTGREEN_EX}💶 {jogador['nome']}, digite o valor da sua aposta (mínimo 100€): "))
            if 100 <= aposta <= jogador["saldo"]:
                return aposta
            print(f"{Fore.RED}❌ Aposta inválida! Deve ser no mínimo €100 e no máximo o saldo disponível. ❌")
        except ValueError:
            print(f"{Fore.YELLOW}⚠ Por favor, insira um número válido. ⚠")

def escolher_cavalo():
    """
    Permite aos usuários escolherem o cavalo para apostar

    Returns:
        escolha: O cavalo escolhido pelo jogador
    
    """
    cavalos = ["Radiant Zephyr", "Silver Shadow", "Thunder Blaze", "Lunar Blossom", "Mystic Horizon"]
    
    #Lista de cavalos disponiveis para a aposta
    print("   Cavalos disponíveis:  ")
    print(f"{Fore.YELLOW}#1 - 🐎 Radiant Zephyr 🐎")
    print(f"{Fore.LIGHTCYAN_EX}#2 - 🐎 Silver Shadow 🐎")
    print(f"{Fore.LIGHTRED_EX}#3 - 🐎 Thunder Blaze 🐎")
    print(f"{Fore.MAGENTA}#4 - 🐎 Lunar Blossom 🐎")
    print(f"{Fore.LIGHTGREEN_EX}#5 - 🐎 Mystic Horizon 🐎")
    # o usuário escolhe o cavalo
    # Apresenta uma mensagem de erro quando o cavalo é inválido
    while True:
        escolha = input(f"{Fore.YELLOW}Digite o nome do cavalo escolhido: ").strip()
        if escolha in cavalos:
            return escolha
        print(f"{Fore.RED}⛔ Cavalo inválido! Escolha um cavalo válido. ⛔")

def simular_a_corrida():
    """
    Permite simular a corrida.

    Returns:
        vencedor: O cavalo vencedor da corrida.
    
    """
    
    #O programa utiliza time para criar a imersão de uma corrida
    print(f"{Fore.GREEN}🏁 A corrida vai começar! Preparar... 🏁")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print(f"{Fore.YELLOW}🏇 Os cavalos estão correndo! 🏇")
    time.sleep(2)
    
    #O programa seleciona o cavalo vencedor
    vencedor = random.choice(["Radiant Zephyr", "Silver Shadow", "Thunder Blaze", "Lunar Blossom", "Mystic Horizon"])
    print(f"{Fore.YELLOW}✨ Corrida terminada! O vencedor foi: {vencedor} ✨")
    return vencedor
    

def atualizar_jogador(jogador, vencedor):
    """
    Atualiza as estatisticas dos jogadores.

    Args:
        jogador: O jogador.
        aposta: O valor apostado.
        cavaloEscolhido: O cavlo escolhido pelo jogador.
        vencedor: O cavalo vencedor.
    """
    
    #Adiciona os respetivos pontos ao jogador
    if jogador["cavalo"] == vencedor:
        print(f"{Fore.GREEN}🏆 Parabéns, {jogador['nome']}! Você acertou o cavalo vencedor! 🏆")
        jogador["pontos"] += 5
    else:
        print(f"{Fore.RED} 🤷🏻‍♂️ Que pena, {jogador['nome']}! Você não acertou desta vez. 🤷🏻‍♂️")
        jogador["pontos"] += 1
    
    #Retira o valor da aposta ao saldo
    jogador["saldo"] -= jogador["aposta"]

    # Mostra os pontos do jogador e o seu respetivo saldo
    print(f"{Fore.LIGHTMAGENTA_EX}Pontos acumulados por {jogador['nome']}: {jogador['pontos']}")
    print(f"{Fore.LIGHTMAGENTA_EX}Saldo restante de {jogador['nome']}: {jogador['saldo']}€")

def jogar_ronda(jogadores):
    """
    Permite jogar uma ronda por todos os jogadores.

    Args:
        jogadores (list): Lista de jogadores.
    """
    # Cada jogador realiza a sua aposta e escolhe o seu cavalo
    for jogador in jogadores:
        if jogador["saldo"] < 100:
            print(f"{Fore.RED}❌ {jogador['nome']} não tem saldo suficiente para continuar.")
            continue
        print(f"Turno do jogador {jogador['nome']}")
        jogador["aposta"] = apostar(jogador)  # Define a aposta do jogador
        jogador["cavalo"] = escolher_cavalo()  # Define o cavalo do jogador
    
    # Simula a corrida uma vez, aplicável a todos os jogadores
    vencedor = simular_a_corrida()

    # Atualiza as informações de cada jogador com base no resultado da corrida
    for jogador in jogadores:
        if jogador["saldo"] >= 100:
            atualizar_jogador(jogador, vencedor)

def mostrar_resultados_finais(jogadores)-> None:
    """
    Mostra os resultados finais do jogo para todos os jogadores
    Args:
        jogadores: os jogadores
    
    """
    
    # Quando o jogo acaba, mostra os resultados finais
    print(f"{Fore.GREEN}------------------ RESULTADOS FINAIS ------------------")
    for jogador in jogadores:
        print(f"{Fore.YELLOW}Jogador: {jogador['nome']}")
        print("=====================")
        print(f"    Pontos finais: {jogador['pontos']}")
        print(f"    Saldo final: {jogador['saldo']}€")
        if jogador["pontos"] >= 10:
            ganho = 100 * 100
            jogador["saldo"] += ganho
            print(f"{Fore.YELLOW} 🏆 Parabéns, {jogador['nome']}! Você atingiu 10 ou mais pontos e ganhou {ganho}€! 🏆")
        elif jogador["pontos"] <= 5:
            jogador["saldo"] = 0
            print(f"{Fore.LIGHTRED_EX}Infelizmente, {jogador['nome']}, você terminou com 5 ou menos pontos e perdeu todo o saldo.")
        else:
            print(f"{jogador['nome']}, você não atingiu 10 pontos, mas ainda mantém o saldo restante.")
        print(f"Saldo final após o jogo para {jogador['nome']}: €{jogador['saldo']}")

def main():
    """
    Função principal para rodar o jogo.
    
    """
    
    # Começa na rodada um acabando na cinco
    qtdDeJogadores = numero_de_jogadores()
    jogadores = [nome_e_saldo_do_jogador(i + 1) for i in range(qtdDeJogadores)]
    
    rodada = 1
    while rodada <= 5:
        print(f"------------- RODADA {rodada} -------------")
        if all(jogador["saldo"] < 100 for jogador in jogadores):
            print(f"{Fore.GREEN} Todos os jogadores estão sem saldo suficiente para continuar. Fim de jogo!")
            break
        jogar_ronda(jogadores)
        if rodada < 5:
            continuar = input("Os jogadores desejam continuar para a próxima rodada? (sim/não): ").strip().lower()
            if continuar != "sim":
                print(f"{Fore.BLUE} Os jogadores decidiram encerrar o jogo.")
                break
        rodada += 1
    
    # No final apresenta todos os resultados
    mostrar_resultados_finais(jogadores)

# Executa o jogo
if __name__ == "__main__":
    main()
