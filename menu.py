import pygame
import sys
import jeu
import page_accueil

def menu(p):
    
    def match_nul():
        pygame.font.init()
        screen.fill((255,255,255))
        my_font=pygame.font.Font(None, 100)        
        text1 = my_font.render("Match NUL",1,(0,0,0))
        
        screen.blit(text1,(250,100))
        font=pygame.font.Font(None, 50)        
        text = font.render(" page d'acceuil",1,(0,0,0))
        screen.blit(text,(500,300))
        text = font.render(" recommencer",1,(0,0,0))
        screen.blit(text,(100,300))
        if event.type== pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if 500<x<745 and 310<y<330:
                page_accueil.page_accueil()
            elif 110<x<430 and 310<y<330:
                jeu.partie_simple()    

    def victoire_croix():
        pygame.font.init()
        screen.fill((255,255,255))
        my_font=pygame.font.Font(None, 100)        
        text1 = my_font.render("You Win 'X'",1,(0,0,0))
        
        screen.blit(text1,(250,100))
        font=pygame.font.Font(None, 50)        
        text = font.render(" page d'acceuil",1,(0,0,0))
        screen.blit(text,(500,300))
        text = font.render(" recommencer",1,(0,0,0))
        screen.blit(text,(100,300))
        if event.type== pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if 500<x<745 and 310<y<330:
                page_accueil.page_accueil()
            elif 110<x<430 and 310<y<330:
                jeu.partie_simple()           

    def victoire_rond():
        pygame.font.init()
        screen.fill((255,255,255))
        my_font=pygame.font.Font(None, 100)        
        text2 = my_font.render("You Win 'O'",1,(0,0,0))
        screen.blit(text2,(250,100))
        font=pygame.font.Font(None, 50)        
        text = font.render(" page d'acceuil",1,(0,0,0))
        screen.blit(text,(500,300))
        text = font.render(" recommencer",1,(0,0,0))
        screen.blit(text,(100,300))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if 500<x<745 and 310<y<320:
                page_accueil.page_acceuil()
            elif 110<x<430 and 300<y<330:
                jeu.partie_simple()   


    pygame.init()
    
    width,height = 900,600

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("tic-tac-toe")
    
    
    #couleur defond
    screen.fill((255,255,255))
    
    
    while True:
        
        # pygame.display.flip() 
        pygame.display.update()
        
        
        for event in pygame.event.get() : 
                      
            if event.type==pygame.QUIT:
                sys.exit()
            if p==1: 
                victoire_croix()          
            elif p==0:
                victoire_rond()
            elif p==3:
                match_nul()
              
                
                
                