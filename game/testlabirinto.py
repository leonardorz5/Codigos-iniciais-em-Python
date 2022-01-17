import pygame
from pygame.image import load

   
def menu():
    pygame.init()
    sair = False
    tela = pygame.display.set_mode([1280,720])
    imagem_menu = pygame.image.load ('menu.jpeg')
    tela.blit(imagem_menu, (50,10))
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    main()
                    
            pygame.display.update()
    
def foto_final():
    tela = pygame.display.set_mode([1280,720])
    fim_game = pygame.image.load ('ines-brasil.jpg')
    tela.blit(fim_game, (600,230))
    
    
    
def main():
    pygame.init() #faz o game iniciar 
    
    fundogame = pygame.image.load ('Anime-meme.jpg')
    tela = pygame.display.set_mode([1400,800])
    pygame.display.set_caption('Labirinto')
    sair = False
    relogio = pygame.time.Clock()
    cor_parede = (119,136,153)
    fim_mapa = (128,0,0)
    cor_retangulo = (240,238,255)
    
    
    parede1 = pygame.Rect(0, 0,650,1400) #parametros da superficie
    
    retangulo=pygame.Rect(655, 761,30,30)
    
    parede2 = pygame.Rect(688, 0,900,1400) #parametros da superficie
    
    
    final = pygame.Rect(650, 0,40,9)
    
    
                       
    
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
                
        
        pygame.display.update()                                                   
        relogio.tick(60)                   
        tela.blit(fundogame, (00,00))
        pygame.draw.rect(tela,cor_parede,parede1)
        pygame.draw.rect(tela,cor_parede,parede2)
        pygame.draw.rect(tela,fim_mapa,final)
        #tela.blit(parede2, [690,0]) #primeiro parametro mexe pro lado, e o segundo pra cima e pra baixo
        #tela.blit(final, [650,0])#primeiro parametro mexe pro lado, e o segundo pra cima e pra baixo
        
        
        
        
        (xant, yant) = (retangulo.left, retangulo.top)
        
        pygame.draw.rect(tela,cor_retangulo,retangulo)
        (retangulo.left, retangulo.top)=pygame.mouse.get_pos()
        retangulo.left -= retangulo.width/2 #centralizar o mouse
        retangulo.top -= retangulo.width/2
        if retangulo.colliderect(parede1 ):
            (retangulo.left, retangulo.top) = (xant, yant)
            
        elif retangulo.colliderect(parede2 ):
            (retangulo.left, retangulo.top) = (xant, yant)
            
        if retangulo.colliderect(final ):       
            foto_final()  
                                                                                         
        

pygame.quit()
menu()
               