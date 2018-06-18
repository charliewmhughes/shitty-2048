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
blank_tile = pygame.image.load('blank_tile.png')
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


coordinates_quoted = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2',  'B3',  'B4', 'C1',  'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']


#######################################################################################################


#this function just pulls up the background image/the playboard
def draw_background():
    screen.fill([255,255,255])
    screen.blit(background,  (0, 0))
    pygame.display.update()



#######################################################################################################

#variables associated with each tile
class tile:
    numerical_value = 0
    tile_x_var = 0
    tile_y_var = 0

A1 = tile()
A2 = tile()
A3 = tile()
A4 = tile()

B1 = tile()
B2 = tile()
B3 = tile()
B4 = tile()

C1 = tile()
C2 = tile()
C3 = tile()
C4 = tile()

D1 = tile()
D2 = tile()
D3 = tile()
D4 = tile()

A1.tile_x_var = 15
A1.tile_y_var = 70
A2.tile_x_var = 120
A2.tile_y_var = 70
A3.tile_x_var = 225
A3.tile_y_var = 70
A4.tile_x_var = 330
A4.tile_y_var = 70
B1.tile_x_var = 15
B1.tile_y_var = 175
B2.tile_x_var = 120
B2.tile_y_var = 175
B3.tile_x_var = 225
B3.tile_y_var = 175
B4.tile_x_var = 330
B4.tile_y_var = 175
C1.tile_x_var = 15
C1.tile_y_var = 280
C2.tile_x_var = 120
C2.tile_y_var = 279
C3.tile_x_var = 225
C3.tile_y_var = 280
C4.tile_x_var = 330
C4.tile_y_var = 280
D1.tile_x_var = 15
D1.tile_y_var = 385
D2.tile_x_var = 120
D2.tile_y_var = 385
D3.tile_x_var = 225
D3.tile_y_var = 385
D4.tile_x_var = 330
D4.tile_y_var = 385

coordinates_unquoted = [A1, A2, A3, A4, B1, B2,  B3,  B4, C1, C2, C3, C4, D1, D2, D3, D4]

coordinates_unquoted_down = [D4, D3, D2, D1, C4, C3, C2, C1, B4, B3, B2, B1, A4, A3, A2, A1]
coordinates_unquoted_up = [A1, A2, A3, A4, B1, B2,  B3,  B4, C1, C2, C3, C4, D1, D2, D3, D4]
coordinates_unquoted_right = [A4, B4, C4, D4, A3, B3, C3, D3, A2, B2, C2, D2, A1, B1, C1, D1]
coordinates_unquoted_left = [A1, B1, C1, D1, A2, B2, C2, D2, A3, B3, C3, D3, A4, B4, C4, D4]

#######################################################################################################
available_tile_values_spawn = ('2', '4')
available_tile_values = ('2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096')
available_tile_names = [two_tile, four_tile, eight_tile,  sixteen_tile,  thirty_two_tile, sixty_four_tile, one_twenty_eight_tile, two_fifty_six_tile, five_twelve_tile, ten_twenty_four_tile, twenty_fourty_eight_tile, fourty_ninety_six_tile]

#spawn a new tile    
def spawn_tile():
    spawned_tile = random.choice(coordinates_unquoted)
    if spawned_tile.numerical_value != 0:
        spawned_tile = ('none')
       
    ##tile2 = random.choice(coordinates)
    if spawned_tile != 'none':
        spawned_tile.numerical_value = random.choice(available_tile_values_spawn)

#ensure all tiles are up to date        
def update_screen():
    for x in coordinates_unquoted:
        x.numerical_value = int(x.numerical_value)
        if x.numerical_value != 0:
            for y in available_tile_values:
                yint = int(y)
                if yint != x.numerical_value:
                    pass
                elif yint == x.numerical_value:
                    z = available_tile_values.index(y)
                    z = int(z)
                    z = (z)
                    blittingval = available_tile_names[z]
            screen.blit(blittingval, (x.tile_x_var, x.tile_y_var))
        elif x.numerical_value == 0:
            screen.blit(blank_tile, (x.tile_x_var, x.tile_y_var))
        pygame.display.update()
    

#make a move:
def key_control():

    events = pygame.event.get()
    loops = 0
    
    #so that adding doesn't continue past one event.
    loopU = 0
    loopD = 0
    loopL = 0
    loopR = 0
    for event in events:
        while loops < 4:
        
            if event.type == pygame.KEYDOWN:
                if event.key == 273 or event.key == 119:
                    for tilew in coordinates_unquoted_up:
                        tilex = tilew
                        if tilew != A1 and tilew != A2 and tilew != A3 and tilew != A4:
                            tilex = coordinates_unquoted_up[int(coordinates_unquoted_up.index(tilew)) - 4]
                        tilew.numerical_value  = int(tilew.numerical_value)
                        tilex.numerical_value = int(tilex.numerical_value)
                        if tilew.numerical_value != 0 and tilew != A1 and tilew != A2 and tilew != A3 and tilew != A4:
                            if tilex.numerical_value == tilew.numerical_value and loopU < 1:
                                tilex.numerical_value = tilew.numerical_value * 2
                                tilew.numerical_value = 0
                                loopU += 1
                                #draw_background()
                            if tilex.numerical_value == 0:
                                tilex.numerical_value = tilew.numerical_value
                                tilew.numerical_value = 0
                                #draw_background()
                                
        
        
                elif event.key == 274 or event.key == 115:
                    for tilew in coordinates_unquoted_down:
                        tilex = tilew
                        if tilew != D1 and tilew != D2 and tilew != D3 and tilew != D4:
                            tilex = coordinates_unquoted_down[int(coordinates_unquoted_down.index(tilew)) - 4]
                        tilew.numerical_value  = int(tilew.numerical_value)
                        tilex.numerical_value = int(tilex.numerical_value)
                        if tilew.numerical_value != 0 and tilew != D1 and tilew != D2 and tilew != D3 and tilew != D4:
                            if tilex.numerical_value == tilew.numerical_value and loopD < 1:
                                tilex.numerical_value = tilew.numerical_value * 2
                                tilew.numerical_value = 0
                                loopD += 1
                                #draw_background()
                            if tilex.numerical_value == 0:
                                tilex.numerical_value = tilew.numerical_value
                                tilew.numerical_value = 0
                                #draw_background()
                                
                
                
                elif event.key == 275 or event.key == 100:
                    for tilew in coordinates_unquoted_right:
                        tilex = tilew
                        if tilew != A4 and tilew != B4 and tilew != C4 and tilew != D4:
                            tilex = coordinates_unquoted_right[int(coordinates_unquoted_right.index(tilew)) - 4]
                        tilew.numerical_value  = int(tilew.numerical_value)
                        tilex.numerical_value = int(tilex.numerical_value)
                        if tilew.numerical_value != 0 and tilew != A4 and tilew != B4 and tilew != C4 and tilew != D4:
                            if tilex.numerical_value == tilew.numerical_value and loopR < 1:
                                tilex.numerical_value = tilew.numerical_value * 2
                                tilew.numerical_value = 0
                                loopR += 1
                                #draw_background()
                            if tilex.numerical_value == 0:
                                tilex.numerical_value = tilew.numerical_value
                                tilew.numerical_value = 0
                                #draw_background()
                                
                    
                    
                elif event.key == 276 or event.key == 97:
                    for tilew in coordinates_unquoted_left:
                        tilex = tilew
                        if tilew != A1 and tilew != B1 and tilew != C1 and tilew != D1:
                            tilex = coordinates_unquoted_left[int(coordinates_unquoted_left.index(tilew)) - 4]
                        tilew.numerical_value  = int(tilew.numerical_value)
                        tilex.numerical_value = int(tilex.numerical_value)
                        if tilew.numerical_value != 0 and tilew != A1 and tilew != B1 and tilew != C1 and tilew != D1:
                            if tilex.numerical_value == tilew.numerical_value and loopL < 1:
                                tilex.numerical_value = tilew.numerical_value * 2
                                tilew.numerical_value = 0
                                loopL += 1
                                #draw_background()
                            if tilex.numerical_value == 0:
                                tilex.numerical_value = tilew.numerical_value
                                tilew.numerical_value = 0
                                #draw_background()
                
                
            loops = loops+1
            if event.type == pygame.KEYUP:
                if loops == 4:
                    spawn_tile()
            if event.type == pygame.QUIT:
                pygame.quit()
