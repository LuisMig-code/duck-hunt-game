import random

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# peguei do stackoverflow mesmo :|
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

largura_tela = 600
altura_tela = 400

tela = pygame.display.set_mode( (largura_tela,altura_tela) )
pygame.display.set_caption("Duck Hunt")

path_bg = pygame.image.load("imgs/cenario.png")
pato_vivo = pygame.image.load("imgs/pato_vivo.png")
pato_vivo_acima = pygame.image.load("imgs/pato_vivo.png")
pato_morto_acima = pygame.image.load("imgs/pato_morto.png")
pato_morto = pygame.image.load("imgs/pato_morto.png")
mira = pygame.image.load("imgs/mira.png")
arma = pygame.image.load("imgs/arma.png")
path_municao = pygame.image.load("imgs/bullet.png")
path_pato_pontuacao = pygame.image.load("imgs/pato_pontuacao.png")

patos_acertados = 0

# fazendo a velocidade dos patos ser aleatoria:
velocidade_pato1 = random.randint(1,3)
velocidade_pato2 = random.randint(1,3)

# função que mostra as imagens na tela
def arma_tela(x,y):
    tela.blit( pygame.transform.scale(arma, (64*2, 64*2)) , (x,y) )

def pato(img,x,y):
    tela.blit(img, (x, y))

def mouse(x,y):
    tela.blit(mira,(x-32,y-32))

def municao_tela(x,y):
    tela.blit(path_municao,(x,y))

def pato_pontuacao(x,y):
    tela.blit(path_pato_pontuacao,(x,y))

# posição onde o pato inicia
x_pato1 = 600 - 64
y_pato1 = 310 - 64

# posição onde o segundo pato inicia
x_pato2 = 600-64
y_pato2 = 310-64-140

# posições onde o player acertou os patos
lista_posicoes_acertadas = []

municao = 12

# textos na tela:
fonte = pygame.font.SysFont("Arial",36,True,False)

# musicas do jogo:
pygame.mixer.music.set_volume(0.1)

musica_de_fundo = pygame.mixer.music.load("sons/ost.mp3")
pygame.mixer.music.play(-1)

som_pato_death = pygame.mixer.Sound("sons/quack.wav")
som_tiro = pygame.mixer.Sound("sons/shot.wav")

# Funções de game over:
def exibe_mensagem(mensagem,tamanho,cor):
    fonte = pygame.font.SysFont('lucidasans', tamanho, True, False)
    msg = f'{mensagem}'
    texto_format = fonte.render(msg, True, cor)
    return texto_format

while True:
    # colocando o background
    tela.blit(path_bg , (0,0))

    # mira no cursor do usuario
    try:
        x_mouse = pygame.mouse.get_pos()[0]
        y_mouse = pygame.mouse.get_pos()[1]
    except:
        x_mouse = 0
        y_mouse = 0

    mouse(x_mouse, y_mouse)

    for event in pygame.event.get():
        # saindo do jogo
        if event.type == QUIT :
            pygame.quit()
            exit()

        # reinicia o jogo
        if event.type == KEYDOWN :
            if event.key == K_r and municao < 1:
                municao = 12
                velocidade_pato2 = random.randint(1,3)
                velocidade_pato1 = random.randint(1,3)

                valor_posi = random.randint(0, 600)
                if valor_posi > 300:
                    pato_vivo = pygame.image.load("imgs/pato_vivo.png")
                    x_pato1 = 600
                    velocidade_pato1 = -velocidade_pato1
                else:
                    pato_vivo = pygame.image.load("imgs/pato_vivo_esq.png")
                    x_pato1 = -64
                    velocidade_pato1 = -velocidade_pato1

                valor_posi = random.randint(0, 600)
                if valor_posi > 300:
                    pato_vivo_acima = pygame.image.load("imgs/pato_vivo.png")
                    x_pato2 = 600
                    velocidade_pato2 = -velocidade_pato2
                else:
                    pato_vivo_acima = pygame.image.load("imgs/pato_vivo_esq.png")
                    x_pato2 = -64
                    velocidade_pato2 = -velocidade_pato2

                patos_acertados = 0
                lista_posicoes_acertadas = []


        # capturando o evento de tiro
        if event.type == pygame.MOUSEBUTTONUP:
            # pega coordenada do clique
            pos = pygame.mouse.get_pos()

            # para cada clique , o usuário perde um tiro da munição
            municao -= 1


            # munição acabou:
            if municao < 1:
                municao = 0
                patos_acertados += 0

                break

            som_tiro.play()

            # posicao do click
            x_click = pos[0]
            y_click = pos[1]

            # Caso o usuário tenha acertado o pato da tábua de baixo:
            if (x_click >= x_pato1 and x_click <= x_pato1 + 64) and (y_click >= y_pato1 and y_click <= y_pato1 + 64):
                som_pato_death.play()
                patos_acertados += 1

                lista_posicoes_acertadas.append((x_pato1, y_pato1))

                # sorteia um numero e se for maior que 300 , o pato comeca no lado direito da tela , caso o contrario comeca
                # no lado esquerdo da tela
                valor_posi = random.randint(0, 600)
                if valor_posi > 300:
                    x_pato1 = 600
                    pato_vivo = pygame.image.load("imgs/pato_vivo.png")
                    pato_morto = pygame.image.load("imgs/pato_morto.png")
                    velocidade_pato1 = random.randint(1, 3)
                    velocidade_pato1 = -velocidade_pato1

                else:
                    x_pato1 = -64
                    pato_vivo = pygame.image.load("imgs/pato_vivo_esq.png")
                    pato_morto = pygame.image.load("imgs/pato_morto_esq.png")
                    velocidade_pato1 = random.randint(1, 3)
                    velocidade_pato1 = -velocidade_pato1

            # Caso o usuário tenha acertado o pato da tábua de baixo:
            if (x_click >= x_pato2 and x_click <= x_pato2 + 64) and (y_click >= y_pato2 and y_click <= y_pato2 + 64):
                som_pato_death.play()
                patos_acertados += 1

                lista_posicoes_acertadas.append((x_pato2, y_pato2))

                valor_posi = random.randint(0, 600)
                if valor_posi > 300:
                    x_pato2 = 600
                    pato_vivo_acima = pygame.image.load("imgs/pato_vivo.png")
                    pato_morto_acima = pygame.image.load("imgs/pato_morto.png")
                    velocidade_pato2 = random.randint(1, 3)
                    velocidade_pato2 = -velocidade_pato2
                else:
                    x_pato2 = -64
                    pato_vivo_acima = pygame.image.load("imgs/pato_vivo_esq.png")
                    pato_morto_acima = pygame.image.load("imgs/pato_morto_esq.png")
                    velocidade_pato2 = random.randint(1, 3)
                    velocidade_pato2 = -velocidade_pato2


    # no momento que o usuário acerta um pato , ele deixa um pato morto na posição acertada
    if len(lista_posicoes_acertadas)>=1:
        pato(pato_morto,lista_posicoes_acertadas[-1][0] , lista_posicoes_acertadas[-1][1])

    # munição acabou:
    if municao < 1:
        municao = 0
        game_over = exibe_mensagem("GAME OVER", 40, (0, 0, 0))
        sua_pontuacao = exibe_mensagem(f"Você acertou {patos_acertados} patos",(26),(0,0,0))
        restart = exibe_mensagem("pressione R para reiniciar",(20),(0,0,0))

        tela.blit(game_over, (290, 200))
        tela.blit(sua_pontuacao, (290, 250))
        tela.blit(restart, (290, 290))

        velocidade_pato1 = 0
        velocidade_pato2 = 0

    # faz o pato andar na tela:

    x_pato1 -= velocidade_pato1
    ## Caso o pato chegue no final , coloca novamente na tela
    if x_pato1<-64 or x_pato1>664:
        # sorteia um numero e se for maior que 300 , o pato comeca no lado direito da tela , caso o contrario comeca
        # no lado esquerdo da tela
        valor_posi = random.randint(0,600)
        if valor_posi > 300:
            pato_vivo = pygame.image.load("imgs/pato_vivo.png")
            x_pato1 = 600
            velocidade_pato1 = -velocidade_pato1
        else:
            pato_vivo = pygame.image.load("imgs/pato_vivo_esq.png")
            x_pato1 = -64
            velocidade_pato1 = -velocidade_pato1

    pato(pato_vivo, x_pato1, y_pato1)

    x_pato2 -= velocidade_pato2
    if x_pato2 < -64 or x_pato2 > 664:
        # sorteia um numero e se for maior que 300 , o pato comeca no lado direito da tela , caso o contrario comeca
        # no lado esquerdo da tela
        valor_posi = random.randint(0, 600)
        if valor_posi > 300:
            pato_vivo_acima = pygame.image.load("imgs/pato_vivo.png")
            x_pato2 = 600
            velocidade_pato2 = -velocidade_pato2
        else:
            pato_vivo_acima = pygame.image.load("imgs/pato_vivo_esq.png")
            x_pato2 = -64
            velocidade_pato2 = -velocidade_pato2
    pato(pato_vivo_acima, x_pato2, y_pato2)

    # mostra a arminha a tela:
    arma_tela(0,310)


    # mostra a quantidade de balas:
    for i in range(municao):
        municao_tela(128+(i*32), 345)

    # mostrar Pontuação:
    pato_pontuacao(450,0)

    mensagem = f"{patos_acertados}"
    texto_formatado = fonte.render(mensagem,True,(0,0,0))

    tela.blit(texto_formatado,(530,13))

    pygame.display.update()