#import necessary libraries
import pygame
import time
import random


#initiate pygame
pygame.init()

#setup display window
(width,  height) = (445,  500)
screen = pygame.display.set_mode((width, height))
running = True

#set colour variables
white = (255,  255,  255)
black = (0,  0,  0)
grey = (128,  128,  128)

#give the display window a title
pygame.display.set_caption('shitty 2048')

#import necessary images
background = pygame.image.load('background.png')
two_tile = pygame.image.load('two_tile.png') 
four_tile =  pygame.image.load('four_tile.png')
eight_tile =  pygame.image.load('eight_tile.png')
sixteen_tile = pygame.image.load('sixteen_tile.png')
thirty_two_tile = pygame.image.load('thirty_two_tile.png')
sixty_four_tile = pygame.image.load('sixty_four_tile.png')
one_twenty_eight_tile = pygame.image.load('one_hundred_twenty_eight_tile.png')
two_fifty_six_tile = pygame.image.load('two_hundred_fifty_six_tile.png')
five_twelve_tile = pygame.image.load('five_hundred_twelve_tile.png')
ten_twenty_four_tile = pygame.image.load('ten_twenty_four_tile.png')
twenty_fourty_eight_tile = pygame.image.load('twenty_fourty_eight_tile.png')
fourty_ninety_six_tile = pygame.image.load('fourty_ninety_six_tile.png')



#now we will set up the arrays and strings needed for the game
A1 = 0
B1 = 0
C1 = 0
D1 = 0
A2 = 0
B2 = 0
C2 = 0
D2 = 0
A3 = 0
B3 = 0
C3 = 0
D3 = 0
A4 = 0
B4 = 0
C4 = 0
D4 = 0
coordinates = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2',  'B3',  'B4', 'C1',  'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']
morecoordinates = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2',  'B3',  'B4', 'C1',  'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']

#######################################################################################################


#this function just pulls up the background image/the playboard
def draw_background():
    screen.blit(background,  (0, 0))
    pygame.display.flip()



#######################################################################################################



def grid_update():
    global A1  
    global B1  
    global C1  
    global D1  
    global A2  
    global B2  
    global C2  
    global D2  
    global A3  
    global B3  
    global C3  
    global D3  
    global A4  
    global B4  
    global C4  
    global D4
    print(A1,  ' ' , B1 , ' ' , C1 ,  ' ' , D1 )
    print(A2 , ' ' , B2 , ' ' , C2 ,  ' ' , D2 )
    print(A3 , ' ' , B3 , ' ' , C3 ,  ' ' , D3 )
    print(A4 , ' ' , B4 , ' ' , C4 ,  ' ' , D4 )
    print(' ')
    


#######################################################################################################


    
def spawn_tile():
    
    global A1  
    global B1  
    global C1  
    global D1  
    global A2  
    global B2  
    global C2  
    global D2  
    global A3  
    global B3  
    global C3  
    global D3  
    global A4  
    global B4  
    global C4  
    global D4  
    
    spawn_loops = 0
    while spawn_loops < 1:
        
        time.sleep(0.001)
        tile1 = random.choice(coordinates)
       
        ##tile2 = random.choice(coordinates)
        
        
        if tile1  == 'A1':
            tile_y_var = 70
            tile_x_var = 15
            A1 = 2
        elif tile1 == 'B1':
            tile_y_var = 70
            tile_x_var = 120
            B1 = 2
        elif tile1 == 'C1':
            tile_y_var = 70
            tile_x_var = 225
            C1 = 2
        elif tile1 == 'D1':
            tile_y_var = 70
            tile_x_var = 330
            D1 = 2
        
        
        if tile1 == 'A2':
            tile_x_var = 15
            tile_y_var = 175
            A2 = 2
        elif tile1 == 'B2':
            tile_x_var = 120
            tile_y_var = 175
            B2 = 2
        elif tile1 == 'C2':
            tile_x_var = 225
            tile_y_var = 175
            C2 = 2
        elif tile1 == 'D2':
            tile_x_var = 330
            tile_y_var = 175
            D2 = 2
        
        if tile1  == 'A3':
            tile_y_var = 280
            tile_x_var = 15
            A3 = 2
        elif tile1 == 'B3':
            tile_y_var = 280
            tile_x_var = 120
            B3 = 2
        elif tile1 == 'C3':
            tile_y_var = 280
            tile_x_var = 225
            C3 = 2
        elif tile1 == 'D3':
            tile_y_var = 280
            tile_x_var = 330
            D3 = 2
        
        
        if tile1  == 'A4':
            tile_x_var = 15
            tile_y_var = 385
            A4 = 2
        elif tile1 == 'B4':
            tile_x_var = 120
            tile_y_var = 385
            B4 = 2
        elif tile1 == 'C4':
            tile_x_var = 225
            tile_y_var = 385
            C4 = 2
        elif tile1 == 'D4':
            tile_x_var = 330
            tile_y_var = 385
            D4 = 2
    
        spawn_loops = spawn_loops +1
        



#######################################################################################################


def update_screen():
    morecoordinates = [A1, A2, A3, A4, B1, B2,  B3,  B4, C1, C2, C3, C4, D1, D2, D3, D4]

    
    for tile in morecoordinates:
        if tile == A1:
            tilex = 15
            tiley = 70
        if tile == B1:
            tilex = 120
            tiley = 70
        if tile == C1:
            tilex = 225
            tiley = 70
        if tile == D1:
            tilex = 330
            tiley = 70
        if tile == A2:
            tilex = 15
            tiley = 175
        if tile == B2:
            tilex = 120
            tiley = 175
        if tile == C2:
            tilex = 225
            tiley = 175
        if tile == D2:
            tilex = 330
            tiley = 175
        if tile == A3:
            tilex = 15
            tiley = 280
        if tile == B3:
            tilex = 120
            tiley = 280
        if tile == C3:
            tilex = 225
            tiley = 280
        if tile == D3:
            tilex = 330
            tiley = 280
        if tile == A4:
            tilex = 15
            tiley = 385
        if tile == B4:
            tilex = 120
            tiley = 385
        if tile == C4:
            tilex = 225
            tiley = 385
        if tile == D4:
            tilex = 330
            tiley = 385
        
        
        if tile == 2:
            screen.blit(two_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 4:
            screen.blit(four_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 8:
            screen.blit(eight_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 16:
            screen.blit(sixteen_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 32:
            screen.blit(thirty_two_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 64:
            screen.blit(sixty_four_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 128:
            screen.blit(one_twenty_eight_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 256:
            screen.blit(two_fifty_six_tile,  (tilex, tiley))
            pygame.display.flip()
        if tile == 512:
            screen.blit(five_twelve_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 1024:
            screen.blit(ten_twenty_four_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 2048:
            screen.blit(twenty_fourty_eight_tile,  (tilex, tiley))
            pygame.display.flip()
             
        if tile == 4096:
            screen.blit(fourty_ninety_six_tile,  (tilex, tiley))
            pygame.display.flip()
             
    

def sense_key():
    global A1  
    global B1  
    global C1  
    global D1  
    global A2  
    global B2  
    global C2  
    global D2  
    global A3  
    global B3  
    global C3  
    global D3  
    global A4  
    global B4  
    global C4  
    global D4 
    
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if A4 == A3 and A4 != 0:
                    A4 = A3*2
                    A3 = 0
                if A3 == A2 and A3 != 0:
                    A3 = A2*2
                    A2 = 0
                if A2 == A1 and A2 != 0:
                    A2 = A1*2
                    A1 = 0
                while  A1 != 0 and A2 == 0:
                    A2 = A1
                    A1 = 0
                while  A2 != 0 and A3 == 0:
                    A3 = A2
                    A2 = 0
                while  A3 != 0 and A4 == 0:
                    A4 = A3
                    A3 = 0
                
                if B4 == B3 and B4 != 0:
                    B4 = B3*2
                    B3 = 0
                if B3 == B2 and B3 != 0:
                    B3 = B2*2
                    B2 = 0
                if B2 == B1 and B2 != 0:
                    B2 = B1*2
                    B1 = 0
                while  B1 != 0 and B2 == 0:
                    B2 = B1
                    B1 = 0
                while  B2 != 0 and B3 == 0:
                    B3 = B2
                    B2 = 0
                while  B3 != 0 and B4 == 0:
                    B4 = B3
                    B3 = 0
                    
                if C4 == C3 and C4 != 0:
                    C4 = C3*2
                    C3 = 0
                if C3 == C2 and C3 != 0:
                    C3 = C2*2
                    C2 = 0
                if C2 == C1 and C2 != 0:
                    C2 = C1*2
                    C1 = 0
                while  C1 != 0 and C2 == 0:
                    C2 = C1
                    C1 = 0
                while  C2 != 0 and C3 == 0:
                    C3 = C2
                    C2 = 0
                while  C3 != 0 and C4 == 0:
                    C4 = C3
                    C3 = 0
                    
                if D4 == D3 and D4 != 0:
                    D4 = D3*2
                    D3 = 0
                if D3 == D2 and D3 != 0:
                    D3 = D2*2
                    D2 = 0
                if D2 == D1 and D2 != 0:
                    D2 = D1*2
                    D1 = 0
                while  D1 != 0 and D2 == 0:
                    D2 = D1
                    D1 = 0
                while  D2 != 0 and D3 == 0:
                    D3 = D2
                    D2 = 0
                while  D3 != 0 and D4 == 0:
                    D4 = D3
                    D3 = 0
                grid_update()
                update_screen()
                spawn_tile()
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if D1 == C1 and D1 != 0:
                    D1 = C1*2
                    C1 = 0
                if C1 == B1 and C1 != 0:
                    C1 = B1*2
                    B1 = 0
                if B1 == A1 and B1 != 0:
                    B1 = A1*2
                    A1 = 0
                while  A1 != 0 and B1 == 0:
                    B1 = A1
                    A1 = 0
                while  B1 != 0 and C1 == 0:
                    C1 = B1
                    B1 = 0
                while  C1 != 0 and D1 == 0:
                    D1 = C1
                    C1 = 0
                    
                if D2 == C2 and D2 != 0:
                    D2 = C2*2
                    C2 = 0
                if C2 == B2 and C2 != 0:
                    C2 = B2*2
                    B2 = 0
                if B2 == A2 and B2 != 0:
                    B2 = A2*2
                    A2 = 0
                while  A2 != 0 and B2 == 0:
                    B2 = A2
                    A2 = 0
                while  B2 != 0 and C2 == 0:
                    C2 = B2
                    B2 = 0
                while  C2 != 0 and D2 == 0:
                    D2 = C2
                    C2 = 0
                    
                if D3 == C3 and D3 != 0:
                    D3 = C3*2
                    C3 = 0
                if C3 == B3 and C3 != 0:
                    C3 = B3*2
                    B3 = 0
                if B3 == A3 and B3 != 0:
                    B3 = A3*2
                    A3 = 0
                while  A3 != 0 and B3 == 0:
                    B3 = A3
                    A3 = 0
                while  B3 != 0 and C3 == 0:
                    C3 = B3
                    B3 = 0
                while  C3 != 0 and D3 == 0:
                    D3 = C3
                    C3 = 0
                    
                if D4 == C4 and D4 != 0:
                    D4 = C4*2
                    C4 = 0
                if C4 == B4 and C4 != 0:
                    C4 = B4*2
                    B4 = 0
                if B4 == A4 and B4 != 0:
                    B4 = A4*2
                    A4 = 0
                while  A4 != 0 and B4 == 0:
                    B4 = A4
                    A4 = 0
                while  B4 != 0 and C4 == 0:
                    C4 = B4
                    B4 = 0
                while  C4 != 0 and D4 == 0:
                    D4 = C4
                    C4 = 0
                grid_update()
                update_screen()
                spawn_tile()
                
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if A1 == B1 and A1 != 0:
                    A1 = B1*2
                    B1 = 0
                if B1 == C1 and B1 != 0:
                    B1 = C1*2
                    C1 = 0
                if C1 == D1 and C1 != 0:
                    C1 = D1*2
                    D1 = 0
                while  D1 != 0 and C1 == 0:
                    C1 = D1
                    D1 = 0
                while  C1 != 0 and B1 == 0:
                    B1 = C1
                    C1 = 0
                while  B1 != 0 and A1 == 0:
                    A1 = B1
                    B1 = 0
                
                if A2 == B2 and A2 != 0:
                    A2 = B2*2
                    B2 = 0
                if B2 == C2 and B2 != 0:
                    B2 = C2*2
                    C2 = 0
                if C2 == D2 and C2 != 0:
                    C2 = D2*2
                    D2 = 0
                while  D2 != 0 and C2 == 0:
                    C2 = D2
                    D2 = 0
                while  C2 != 0 and B2 == 0:
                    B2 = C2
                    C2 = 0
                while  B2 != 0 and A2 == 0:
                    A2 = B2
                    B2 = 0
                    
                if A3 == B3 and A3 != 0:
                    A3 = B3*2
                    B3 = 0
                if B3 == C3 and B3 != 0:
                    B3 = C3*2
                    C3 = 0
                if C3 == D3 and C3 != 0:
                    C3 = D3*2
                    D3 = 0
                while  D3 != 0 and C3 == 0:
                    C3 = D3
                    D3 = 0
                while  C3 != 0 and B3 == 0:
                    B3 = C3
                    C3 = 0
                while  B3 != 0 and A3 == 0:
                    A3 = B3
                    B3 = 0
                    
                if A4 == B4 and A4 != 0:
                    A4 = B4*2
                    B4 = 0
                if B4 == C4 and B4 != 0:
                    B4 = C4*2
                    C4 = 0
                if C4 == D4 and C4 != 0:
                    C4 = D4*2
                    D4 = 0
                while  D4 != 0 and C4 == 0:
                    C4 = D4
                    D4 = 0
                while  C4 != 0 and B4 == 0:
                    B4 = C4
                    C4 = 0
                while  B4 != 0 and A4 == 0:
                    A4 = B4
                    B4 = 0
                grid_update()
                update_screen()
                spawn_tile()
                
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if A1 == A2 and A1 != 0:
                    A1 = A2*2
                    A2 = 0
                if A2 == A3 and A2 != 0:
                    A2 = A3*2
                    A3 = 0
                if A3 == A4 and A3 != 0:
                    A3 = A4*2
                    A4 = 0
                while  A4 != 0 and A3 == 0:
                    A3 = A4
                    A4 = 0
                while  A3 != 0 and A2 == 0:
                    A2 = A3
                    A3 = 0
                while  A2 != 0 and A1 == 0:
                    A1 = A2
                    A2 = 0
                
                if B1 == B2 and B1 != 0:
                    B1 = B2*2
                    B2 = 0
                if B2 == B3 and B2 != 0:
                    B2 = B3*2
                    B3 = 0
                if B3 == B4 and B3 != 0:
                    B3 = B4*2
                    B4 = 0
                while  B4 != 0 and B3 == 0:
                    B3 = B4
                    B4 = 0
                while  B3 != 0 and B2 == 0:
                    B2 = B3
                    B3 = 0
                while  B2 != 0 and B1 == 0:
                    B1 = B2
                    B2 = 0
            
                if C1 == C2 and C1 != 0:
                    C1 = C2*2
                    C2 = 0
                if C2 == C3 and C2 != 0:
                    C2 = C3*2
                    C3 = 0
                if C3 == C4 and C3 != 0:
                    C3 = C4*2
                    C4 = 0
                while  C4 != 0 and C3 == 0:
                    C3 = C4
                    C4 = 0
                while  C3 != 0 and C2 == 0:
                    C2 = C3
                    C3 = 0
                while  C2 != 0 and C1 == 0:
                    C1 = C2
                    C2 = 0
                    
                if D1 == D2 and D1 != 0:
                    D1 = D2*2
                    D2 = 0
                if D2 == D3 and D2 != 0:
                    D2 = D3*2
                    D3 = 0
                if D3 == D4 and D3 != 0:
                    D3 = D4*2
                    D4 = 0
                while  D4 != 0 and D3 == 0:
                    D3 = D4
                    D4 = 0
                while  D3 != 0 and D2 == 0:
                    D2 = D3
                    D3 = 0
                while  D2 != 0 and D1 == 0:
                    D1 = D2
                    D2 = 0
                grid_update()
                update_screen()
                spawn_tile()
                
                


    
    
    


    
