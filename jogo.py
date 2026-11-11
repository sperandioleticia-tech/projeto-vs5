
from pyscript import document, when
from random import randint
import asyncio


# ELEMENTOS DA TELA
jogador = document.querySelector("#jogador")
moeda = document.querySelector("#moeda")
inimigo = document.querySelector("#inimigo")
placar = document.querySelector("#placar")
vidas_tela = document.querySelector("#vidas")
mensagem = document.querySelector("#mensagem")


# JOGADOR
x = 100
y = 100
velocidade = 10


def atualizar_jogador():
    jogador.style.left = f"{x}px"
    jogador.style.top = f"{y}px"


# MOEDAS E PONTUAÇÃO
moeda_x = 300
moeda_y = 200
pontos = 0


def mover_moeda():
    global moeda_x, moeda_y

    moeda_x = randint(20, 650)
    moeda_y = randint(20, 410)

    moeda.style.left = f"{moeda_x}px"
    moeda.style.top = f"{moeda_y}px"


def verificar_moeda():
    global pontos

    if game_over:
        return

    distancia_x = abs(x - moeda_x)
    distancia_y = abs(y - moeda_y)

    if distancia_x < 40 and distancia_y < 40:
        pontos += 1
        placar.innerText = str(pontos)

        mensagem.innerText = "🪙 Moeda coletada! +1 ponto!"

        mover_moeda()


# SISTEMA DE VIDAS
vidas = 3
pode_perder_vida = True
game_over = False


def atualizar_vidas():
    vidas_tela.innerText = str(vidas)


async def liberar_vida():
    global pode_perder_vida

    await asyncio.sleep(1)

    pode_perder_vida = True


def perder_vida():
    global vidas, pode_perder_vida
    global game_over, x, y

    if not pode_perder_vida or game_over:
        return

    vidas -= 1
    pode_perder_vida = False

    atualizar_vidas()

    if vidas <= 0:
        game_over = True
        mensagem.innerText = "💀 GAME OVER! Você ficou sem vidas!"
    else:
        mensagem.innerText = "💥 Você perdeu uma vida! Cuidado!"

        # O jogador retorna ao ponto inicial.
        x = 100
        y = 100
        atualizar_jogador()

        # Aguarda antes de permitir perder outra vida.
        asyncio.create_task(liberar_vida())
