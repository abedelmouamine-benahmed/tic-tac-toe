import pygame  
import sys 
import menu 

def partie_simple():
   
    #variable collision pour eviter que les croix et les ronds ne ce superpose
    collision1= False
    collision2= False
    collision3= False
    collision4= False
    collision5= False
    collision6= False
    collision7= False
    collision8= False
    collision9= False 
    
    #la valeur prend 1 pour les croix et 2 pour les ronds cela permet determiner l'alignement
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    j=0

    #indice fin de partie pour gerer le match Nul
    indice_fin_partie=0
          
    #initialisation du i permettant de faire alterner les tours
    i=0

    #initilisation du jeu parametre de debut 
    pygame.init()

    width,height = 900,600

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("tic-tac-toe")

    #couleur defond
    screen.fill((255,255,255))

    #grille du jeu
    pygame.draw.line(screen,(0,0,0),(300, 50),(300,550),5) 
    pygame.draw.line(screen,(0,0,0),(600, 50),(600,550),5) 
    pygame.draw.line(screen,(0,0,0),(50,200),(850, 200),5)
    pygame.draw.line(screen,(0,0,0),(50,400),(850, 400),5)
    
    
    while True:
    
        for event in pygame.event.get() :
            
            x,y=pygame.mouse.get_pos()
            pygame.font.init()
            
            # pygame.display.flip() 
            pygame.display.update() 
            
            if event.type==pygame.QUIT:
                sys.exit()           
           
            elif event.type == pygame.MOUSEBUTTONDOWN :
                i=i+1                     
                                        
                if i%2==0 :
                        
                    if 0<x<=300 and 0<y<=200 and collision1==False:
                        pygame.draw.circle(screen,(0,0,0),(150,100),90,5)    
                        collision1=True
                        a=2
                    
                    elif 0<x<=300 and 200<y<=400 and collision2==False:
                        pygame.draw.circle(screen,(0,0,0),(150,300),90,5)    
                        collision2=True
                        d=2
                        

                    elif 0<x<=300 and 400<y<=600 and collision3==False:
                        pygame.draw.circle(screen,(0,0,0),(150,500),90,5)
                        collision3=True
                        g=2
                        

                    elif 300<x<=600 and 0<y<=200 and collision4==False:
                        pygame.draw.circle(screen,(0,0,0),(450,100),90,5)
                        collision4=True
                        b=2
                        
                    
                    elif 300<x<=600 and 200<y<=400 and collision5==False:
                        pygame.draw.circle(screen,(0,0,0),(450,300),90,5)
                        collision5=True
                        e=2

                    
                    elif 300<x<=600 and 400<y<=600 and collision6==False:
                        pygame.draw.circle(screen,(0,0,0),(450,500),90,5)
                        collision6=True
                        h=2
                    
                    elif 600<x<=900 and 0<y<=200 and collision7==False:
                        pygame.draw.circle(screen,(0,0,0),(750,100),90,5)
                        collision7=True
                        c=2
                    
                    elif 600<x<=900 and 200<y<=400 and collision8==False:
                        pygame.draw.circle(screen,(0,0,0),(750,300),90,5)
                        collision8=True
                        f=2
                    
                    elif 600<x<=900 and 400<y<=600 and collision9==False:
                        pygame.draw.circle(screen,(0,0,0),(750,500),90,5)  
                        collision9=True
                        j=2
                    indice_fin_partie+=1
               
                else :
                    
                    if 0<x<=300 and 0<y<=200 and collision1==False:
                        pygame.draw.line(screen,(0,0,0),(80,20),(270,180),5)
                        pygame.draw.line(screen,(0,0,0),(270,20),(80,180),5)
                        collision1=True            
                        a=1                    
                    
                    elif 0<x<=300 and 200<y<=400 and collision2==False:
                        pygame.draw.line(screen,(0,0,0),(80,220),(270,380),5)
                        pygame.draw.line(screen,(0,0,0),(270,220),(80,380),5)    
                        collision2=True
                        d=1                   
                    
                    elif 0<x<=300 and 400<y<=600 and collision3==False:
                        pygame.draw.line(screen,(0,0,0),(80,420),(270,580),5)
                        pygame.draw.line(screen,(0,0,0),(270,420),(80,580),5)
                        collision3=True
                        g=1
                    
                    elif 300<x<=600 and 0<y<=200 and collision4==False:
                        pygame.draw.line(screen,(0,0,0),(380,20),(560,180),5)
                        pygame.draw.line(screen,(0,0,0),(560,20),(380,180),5)    
                        collision4=True
                        b=1                   
                        
                    elif 300<x<=600 and 200<y<=400 and collision5==False:
                        pygame.draw.line(screen,(0,0,0),(380,220),(560,380),5)
                        pygame.draw.line(screen,(0,0,0),(560,220),(380,380),5)
                        collision5=True
                        e=1   
                    
                    elif 300<x<=600 and 400<y<=600 and collision6==False:
                        pygame.draw.line(screen,(0,0,0),(380,420),(560,580),5)
                        pygame.draw.line(screen,(0,0,0),(560,420),(380,580),5)
                        collision6=True
                        h=1
                    
                    elif 600<x<=900 and 0<y<=200 and collision7==False:
                        pygame.draw.line(screen,(0,0,0),(680,20),(870,180),5)
                        pygame.draw.line(screen,(0,0,0),(870,20),(680,180),5)
                        collision7=True
                        c=1
                                        
                    elif 600<x<=900 and 200<y<=400 and collision8==False:
                        pygame.draw.line(screen,(0,0,0),(680,220),(870,380),5)
                        pygame.draw.line(screen,(0,0,0),(870,220),(680,380),5)
                        collision8=True
                        f=1

                    elif 600<x<=900 and 400<y<=600 and collision9==False:
                        pygame.draw.line(screen,(0,0,0),(680,420),(870,580),5)
                        pygame.draw.line(screen,(0,0,0),(870,420),(680,580),5)
                        collision9=True
                        j=1
                    indice_fin_partie+=1
            
            #Victoire croix
            elif a==b==c==1 or d==e==f==1 or g==h==j==1 or a==e==j==1 or c==e==g==1 or a==d==g==1 or b==e==h==1 or c==f==j==1:
            
            #indice p est l'argument de la fonction menu qui est dans le fichier menu qui permet de gerer l'affichage du menu en fin de partie 
            # p=1,2ou3 ce qui permet de definir p=1 affichage victoire croix ... 
                p=1
                menu(p)

            #Victoire ronds
            elif a==b==c==2 or d==e==f==2 or g==h==j==2 or a==e==j==2 or c==e==g==2 or a==d==g==2 or b==e==h==2 or c==f==j==2:
                 
                p=0
                menu(p)          
            
            #Match Nul
            elif indice_fin_partie==9:
                
                p=3
                menu(p)

                                         
# partie_simple()                            
                
                        
                    
                