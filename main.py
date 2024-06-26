import pygame
import random
import os
import time


tamanho = (800,600)
tela = pygame.display.set_mode( tamanho ) 

pygame.init()
relogio = pygame.time.Clock()


branco = (255,255,255)
preto = (0, 0 ,0 )


""""
os.system("cls")
mensagem = "Bem vindo ao Projeto Asteróide!"
print(mensagem)
"""

import pygame
import random
import os
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("Recursos/icon.png")
pepsico = pygame.image.load("Recursos/pepsico.png")
fundo = pygame.image.load("Recursos/fundo.jpg")
fundoStart = pygame.image.load("Recursos/fundoStart.png")
fundoDead = pygame.image.load("Recursos/fundoDead.png")

cocamerda = pygame.image.load("Recursos/cocamerda.png")
cocabosta = pygame.image.load("Recursos/cocabosta.png")
aviao = pygame.image.load("Recursos/aviao.png")
solgrande = pygame.image.load("Recursos/solgrande.png")
solpequeno = pygame.image.load("Recursos/solpequeno.png")
tamanho = (800,600)
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("PepsiMan")
pygame.display.set_icon(icone)
cocamerdaSound = pygame.mixer.Sound("Recursos/cocamerda.wav")
cocabostaSound = pygame.mixer.Sound("Recursos/cocamerda.wav")

explosaoSound = pygame.mixer.Sound("Recursos/crazydead.mp3")
fonte = pygame.font.SysFont("comicsans",28)
fonteStart = pygame.font.SysFont("comicsans",55)
fonteMorte = pygame.font.SysFont("arial",120)
pygame.mixer.music.load("Recursos/ironsound.mp3")

branco = (255,255,255)
azul = (0,0,160)
vermelho = (160,0,0)
preto = (0, 0 ,0 )

def jogar(nome):
    pygame.mixer.Sound.play(cocamerdaSound)
    pygame.mixer.music.play(-1)
    posicaoXPersona = 400
    posicaoYPersona = 370
    movimentoXPersona  = 0
    movimentoYPersona  = 0
    posicaoXcocamerda = 400
    posicaoYcocamerda = -240
    velocidadecocamerda = 1
    posicaoXcocabosta = 500
    posicaoYcocabosta = -240
    velocidadecocabosta = 3
    posicaoXaviao = -4000
    posicaoYaviao = 80
    velocidadeaviao = 5
    posicaoXsolpequeno = 660
    posicaoYsolpequeno = 20
    posicaoXsolgrande = 660
    posicaoYsolgrande = 20
    
    pontos = 0
    larguraPersona = 113
    alturaPersona = 161
    larguacocamerda  = 90
    alturacocamerda  = 117
    larguacocabosta  = 92
    alturacocabosta  = 169
    larguasolpequeno  = 140
    alturasolpequeno  = 104
    larguasolgrande  = 160
    alturasolgrande  = 119
    dificuldade  = 10



    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0
                
        posicaoXPersona = posicaoXPersona + movimentoXPersona            
        posicaoYPersona = posicaoYPersona + movimentoYPersona            
        
        if posicaoXPersona < 0 :
            posicaoXPersona = 10
        elif posicaoXPersona >550:
            posicaoXPersona = 540
            
        if posicaoYPersona < 0 :
            posicaoYPersona = 10
        elif posicaoYPersona > 473:
            posicaoYPersona = 463
        
            
        tela.fill(branco)
        tela.blit(fundo, (0,0) )
        #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0 )
        tela.blit( pepsico, (posicaoXPersona, posicaoYPersona) )
        
        posicaoYcocamerda = posicaoYcocamerda + velocidadecocamerda
        if posicaoYcocamerda > 600:
            posicaoYcocamerda = -240
            pontos = pontos + 1
            velocidadecocamerda = velocidadecocamerda + 1
            posicaoXcocamerda = random.randint(0,800)
            pygame.mixer.Sound.play(cocamerdaSound)

        posicaoXaviao = posicaoXaviao + velocidadeaviao
        if posicaoXaviao > 800:
            posicaoXaviao = -4000


        posicaoYcocabosta = posicaoYcocabosta + velocidadecocabosta
        if posicaoYcocabosta > 600:
            posicaoYcocabosta = -240
            pontos = pontos + 1
            velocidadecocabosta = velocidadecocabosta + 1
            posicaoXcocabosta = random.randint(0,800)
            pygame.mixer.Sound.play(cocamerdaSound)                    
            
        tela.blit( solpequeno, (posicaoXsolpequeno, posicaoYsolpequeno))                       
        tela.blit( aviao, (posicaoXaviao, posicaoYaviao))                   
        tela.blit( cocamerda, (posicaoXcocamerda, posicaoYcocamerda))
        tela.blit( cocabosta, (posicaoXcocabosta, posicaoYcocabosta)) 
                
        texto = fonte.render(nome+"- Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (10,10))
        
        pixelspepsicoX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
        pixelspepsicoY = list(range(posicaoYPersona, posicaoYPersona+alturaPersona))
        pixelscocamerdaX = list(range(posicaoXcocamerda, posicaoXcocamerda + larguacocamerda))
        pixelscocamerdalY = list(range(posicaoYcocamerda, posicaoYcocamerda + alturacocamerda))
        pixelscocabostaX = list(range(posicaoXcocabosta, posicaoXcocabosta + larguacocabosta))
        pixelscocabostalY = list(range(posicaoYcocabosta, posicaoYcocabosta + alturacocabosta))
        pixelssolpequenolY = list(range(posicaoYsolpequeno, posicaoYsolpequeno + alturasolpequeno))
        

        #print( len( list( set(pixelscocamerdaX).intersection(set(pixelspepsicoX))   ) )   )
        if  len( list( set(pixelscocamerdalY).intersection(set(pixelspepsicoY))) ) > dificuldade:
            if len( list( set(pixelscocamerdaX).intersection(set(pixelspepsicoX))   ) )  > dificuldade:
                dead(nome, pontos)

        if  len( list( set(pixelscocabostalY).intersection(set(pixelspepsicoY))) ) > dificuldade:
            if len( list( set(pixelscocabostaX).intersection(set(pixelspepsicoX))   ) )  > dificuldade:
                dead(nome, pontos)
        
        pygame.display.update()
        relogio.tick(60)


def dead(nome, pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    
    jogadas  = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("", True, branco)
        tela.blit(textoStart, (400,482))
        textoEnter = fonte.render("FALTA PEPSI NO SEU SISTEMA!!! 'PRESS ENTER'", True, branco)
        tela.blit(textoEnter, (60,482))
        pygame.display.update()
        relogio.tick(60)


def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        relogio.tick(60)


def start():
    nome = simpledialog.askstring("PepsiMan","Nome Completo:")
    
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()

        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        buttonRanking = pygame.draw.rect(tela, preto, (35,50,200,50),0,30)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (90,50))
        textoStart = fonteStart.render("START", True, branco)
        tela.blit(textoStart, (330,482))

        
        
        pygame.display.update()
        relogio.tick(60)

start()