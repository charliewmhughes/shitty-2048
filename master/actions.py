  #Written by Charlie Hughes. Since I can't stop you using this, do with it what you will. Also, I know it won't stop you, but don't delete this comment, because I did all the hard work and deserve at least this tiny bit of recognition. Thanks.

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

#draw ze icon
icon = pygame.image.load('twenty_fourty_eight_tile.png')
pygame.display.set_icon(icon)

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
blank_row_1 = pygame.image.load('first_row_blank.png')
blank_row_2 = pygame.image.load('second_row_blank.png')
blank_row_3 = pygame.image.load('third_row_blank.png')
blank_row_4 = pygame.image.load('fourth_row_blank.png')

#not needed at the moment:
coordinates_quoted = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2',  'B3',  'B4', 'C1',  'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']


#######################################################################################################


#this function just pulls up the background image/the playboard
def draw_background():
    screen.fill([255,255,255])
    screen.blit(background,  (0, 0))
    pygame.display.update()



#######################################################################################################

#tile class so we don't have to reassign every fucking variable
class tile:
    numerical_value = 0
    tile_x_var = 0
    tile_y_var = 0
    dubloop = 0

#but we do have to assign each tile a name
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

#and an individual location on the window
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

#then we have these 'lovely' (read horrible) lists, so that the game will be able to call upon the tiles at different times and in different ways.
coordinates_unquoted = [A1, A2, A3, A4, B1, B2,  B3,  B4, C1, C2, C3, C4, D1, D2, D3, D4]

coordinates_unquoted_down = [D4, D3, D2, D1, C4, C3, C2, C1, B4, B3, B2, B1, A4, A3, A2, A1]
coordinates_unquoted_up = [A1, A2, A3, A4, B1, B2,  B3,  B4, C1, C2, C3, C4, D1, D2, D3, D4]
coordinates_unquoted_right = [A4, B4, C4, D4, A3, B3, C3, D3, A2, B2, C2, D2, A1, B1, C1, D1]
coordinates_unquoted_left = [A1, B1, C1, D1, A2, B2, C2, D2, A3, B3, C3, D3, A4, B4, C4, D4]

row1 = [A1, A2, A3, A4]
row2 = [B1, B2, B3, B4]
row3 = [C1, C2, C3, C4]
row4 = [D1, D2, D3, D4]

#######################################################################################################
#these lists and strings mainly deal with spawning the tiles, and then regulating what image is blitted for each tile by update_screen()
available_tile_values_spawn = ('2', '4')
available_tile_values = ('2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096')
available_tile_names = [two_tile, four_tile, eight_tile,  sixteen_tile,  thirty_two_tile, sixty_four_tile, one_twenty_eight_tile, two_fifty_six_tile, five_twelve_tile, ten_twenty_four_tile, twenty_fourty_eight_tile, fourty_ninety_six_tile]

#spawn a new tile    
def spawn_tile():
    #choose from avaiable spawn values
    spawned_tile = random.choice(coordinates_unquoted)
    #i know this next bit is ugly, but it makes it very hard for a tile to not spawn, because it can't spawn on an occupied space, and sometimes it does that, so we run the random thing more if it does, so hopefully you will never see a tile not spawn.
    if spawned_tile.numerical_value != 0:
        spawned_tile = ('none')
        spawned_tile = random.choice(coordinates_unquoted)
        if spawned_tile.numerical_value != 0:
            spawned_tile = ('none')
            spawned_tile = random.choice(coordinates_unquoted)
            if spawned_tile.numerical_value != 0:
                spawned_tile = ('none')
                spawned_tile = random.choice(coordinates_unquoted)
                if spawned_tile.numerical_value != 0:
                    spawned_tile = ('none')
       
       
    ##tile2 = random.choice(coordinates)
    #if the spawned tile has a value, give it a value
    if spawned_tile != 'none':
        spawned_tile.numerical_value = random.choice(available_tile_values_spawn)

#ensure all tiles are up to date        
def update_screen():
    #for every tile:
    for x in coordinates_unquoted:
        #now we can do maths on the variable:
        x.numerical_value = int(x.numerical_value)
        #if not 0, then do stuff i can;t be fucked to explain, just look at it, lazy.
        #guess what: I decided to be nice to you idiots who can't understand my marvelous, neat, and sensible programming, so I decided to help you out by explaining:
        #if the tile doesn't equal 0
        if x.numerical_value != 0:
            #for every option in available values
            for y in available_tile_values:
                #make integer so maths work
                yint = int(y)
                #if the available value isnt the numerical value of the tile in question (x), do nothing.
                if yint != x.numerical_value:
                    pass
                #but if it is:
                elif yint == x.numerical_value:
                    #z is the position of the tile in the string, so we get that, make it an integer, then the z=(z) bit does nothing at all. seriously.
                    z = available_tile_values.index(y)
                    z = int(z)
                    z = (z)
                    #then the blittingval equals the position in the tile name string that is the same as the position the numerical value was in.
                    blittingval = available_tile_names[z]
            #blit the image that represents the tile's numerical value:
            screen.blit(blittingval, (x.tile_x_var, x.tile_y_var))
        #but if the tile is 0, then print a blank spot on it, so the screen stays nice and pretty. Also it does this individually, so the whole window doesn't flash like it does when you just reblit the background. It also blits on the right kind of tile, cause having them all the same colour of grey was fucking ugly.
        elif x.numerical_value == 0:
            if x in row1:
                screen.blit(blank_row_1, (x.tile_x_var, x.tile_y_var))
            elif x in row2:
                screen.blit(blank_row_2, (x.tile_x_var, x.tile_y_var))
            elif x in row3:
                screen.blit(blank_row_3, (x.tile_x_var, x.tile_y_var))
            elif x in row4:
                screen.blit(blank_row_4, (x.tile_x_var, x.tile_y_var))
        #update the screen to show all changes:
        pygame.display.update()
    

#make a move:
def key_control():

    #shorten the shit u habve to type
    events = pygame.event.get()
    #not gonna explain this variable, but it comes in quite handy later on.
    loops = 0
    #oh yeah, that loops has to be equal to 0 at the start of the cycle, else it will fuck shit up
    

    for event in events:
        #for event in the variable called events that equals pygame.event.get()
        #while the loop below hasn't run four times yet:
        while loops < 4:
            #if the event was a keypress:
            if event.type == pygame.KEYDOWN:
                #if it was the up key or 'w'
                if event.key == 273 or event.key == 119:
                    #for (arbitrary variable name) in the 'up' coordinates string (has to be unquoted so that it actually is the variable, not just represents it:
                    for tilew in coordinates_unquoted_up:
                        #dunno about this bit myself, think it just makes sure the other variable (tilex) doesn't give a syntax error:
                        tilex = tilew
                        #as long as it isnt in the A row (cause we can't move it up, there are no more tiles above)
                        if tilew != A1 and tilew != A2 and tilew != A3 and tilew != A4:
                            #this bit is true genius, I had the greatest sense of acheivement when I came up with it:
                            #it removes four index places, so that the tilex is four variables up from tilew, (the one tile above it physically)
                            tilex = coordinates_unquoted_up[int(coordinates_unquoted_up.index(tilew)) - 4]
                        #integerize them so they can be mathsed
                        tilew.numerical_value  = int(tilew.numerical_value)
                        tilex.numerical_value = int(tilex.numerical_value)
                        # again, as long as it isnt in the A row - see above comment
                        if tilew.numerical_value != 0 and tilew != A1 and tilew != A2 and tilew != A3 and tilew != A4:
                            #if they are the same, and haven't been addded together before (so it doesn't add tiles in a column indefinitely, just once)
                            if tilex.numerical_value == tilew.numerical_value and tilew.dubloop < 1 and tilex.dubloop < 1:
                                #the higher one equals double the lower one numerically
                                tilex.numerical_value = tilew.numerical_value * 2
                                #lower one becomes equal to nothing
                                tilew.numerical_value = 0
                                #then record how many times the tile has been added together per cycle:
                                tilew.dubloop +=1
                                tilex.dubloop +=1
                                #uncommented the draw_background()s in this section, because they do jack shit, and make the screen flash annoyingly:
                                #draw_background()
                            # if the tile above is zilch:
                            if tilex.numerical_value == 0:
                                #tile above equals tile below:
                                tilex.numerical_value = tilew.numerical_value
                                #tile below equals nothin:
                                tilew.numerical_value = 0
                                #draw_background()
                                
        
                #this is the same, except it goes down not up, so sum variables are different, and it operates out of the 'down' coordinates tring
                elif event.key == 274 or event.key == 115:
                    for tilew in coordinates_unquoted_down:
                        tilex = tilew
                        if tilew != D1 and tilew != D2 and tilew != D3 and tilew != D4:
                            tilex = coordinates_unquoted_down[int(coordinates_unquoted_down.index(tilew)) - 4]
                        tilew.numerical_value  = int(tilew.numerical_value)
                        tilex.numerical_value = int(tilex.numerical_value)
                        if tilew.numerical_value != 0 and tilew != D1 and tilew != D2 and tilew != D3 and tilew != D4:
                            if tilex.numerical_value == tilew.numerical_value and tilew.dubloop < 1 and tilex.dubloop < 1:
                                tilex.numerical_value = tilew.numerical_value * 2
                                tilew.numerical_value = 0
                                tilew.dubloop +=1
                                tilex.dubloop +=1
                                #draw_background()
                            if tilex.numerical_value == 0:
                                tilex.numerical_value = tilew.numerical_value
                                tilew.numerical_value = 0
                                #draw_background()
                                
                
                #same as before, using 'right' variables string
                elif event.key == 275 or event.key == 100:
                    for tilew in coordinates_unquoted_right:
                        tilex = tilew
                        if tilew != A4 and tilew != B4 and tilew != C4 and tilew != D4:
                            tilex = coordinates_unquoted_right[int(coordinates_unquoted_right.index(tilew)) - 4]
                        tilew.numerical_value  = int(tilew.numerical_value)
                        tilex.numerical_value = int(tilex.numerical_value)
                        if tilew.numerical_value != 0 and tilew != A4 and tilew != B4 and tilew != C4 and tilew != D4:
                            if tilex.numerical_value == tilew.numerical_value and tilew.dubloop < 1 and tilex.dubloop < 1:
                                tilex.numerical_value = tilew.numerical_value * 2
                                tilew.numerical_value = 0
                                tilew.dubloop +=1
                                tilex.dubloop +=1
                                #draw_background()
                            if tilex.numerical_value == 0:
                                tilex.numerical_value = tilew.numerical_value
                                tilew.numerical_value = 0
                                #draw_background()
                                
                    
                #aswell as this one, which uses 'right' variables string
                elif event.key == 276 or event.key == 97:
                    for tilew in coordinates_unquoted_left:
                        tilex = tilew
                        if tilew != A1 and tilew != B1 and tilew != C1 and tilew != D1:
                            tilex = coordinates_unquoted_left[int(coordinates_unquoted_left.index(tilew)) - 4]
                        tilew.numerical_value  = int(tilew.numerical_value)
                        tilex.numerical_value = int(tilex.numerical_value)
                        if tilew.numerical_value != 0 and tilew != A1 and tilew != B1 and tilew != C1 and tilew != D1:
                            if tilex.numerical_value == tilew.numerical_value and tilew.dubloop < 1 and tilex.dubloop < 1:
                                tilex.numerical_value = tilew.numerical_value * 2
                                tilew.numerical_value = 0
                                tilew.dubloop +=1
                                tilex.dubloop +=1
                                #draw_background()
                            if tilex.numerical_value == 0:
                                tilex.numerical_value = tilew.numerical_value
                                tilew.numerical_value = 0
                                #draw_background()
                
            #record how many times this shit has looped
            loops = loops+1
            #for (arbitrary value) in coordinates string:
            for anytile in coordinates_unquoted:
                #if the thing has looped four times (one cycle), then reset the adding loop of each variable:
                if loops == 4:
                    anytile.dubloop = 0
            #just gonna stick this here I know it shouldn't go here:
            gamekeys = (276, 97, 275, 100, 274, 115, 273, 119)
            #if you release a key, and the cycle has ended, spawn a new tile
            if event.type == pygame.KEYUP and event.key in gamekeys:
                if loops == 4:
                    spawn_tile()
            #if you click the exit button, then it will quit the program, instead of doing nothing like it used to.
            if event.type == pygame.QUIT:
                pygame.quit()
                
#pretty basic huh?
#well i bet you couldn't do it, and some of the solutions i made to problems were true genius.
