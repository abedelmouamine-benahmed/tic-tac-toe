
import pygame 
import sys
import jeu

def page_accueil():
    pygame.init()

    width,height = 900,600

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("tic-tac-toe")

    #couleur defond
    screen.fill((255,255,255))
    pygame.font.init()
    
    while True:

        for event in pygame.event.get() :
            my_font=pygame.font.Font(None, 100)        
            text = my_font.render("Le Morpion",1,(0,0,0))
            screen.blit(text,(250,0))
            
            My_font=pygame.font.Font(None, 50)        
            text = My_font.render("1vs1",1,(0,0,0))
            screen.blit(text,(300,300))
            text = My_font.render("1vsAI",1,(0,0,0))
            screen.blit(text,(500,300))
            # pygame.display.flip() 
            pygame.display.update() 
            
            if event.type==pygame.QUIT:
                sys.exit()
            
            elif event.type== pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if 300<x<370 and 300<y<330:
                    jeu.partie_simple()
                

page_accueil()     
           

