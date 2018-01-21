import time
import random

def spawn_tile():
    import random
    spawn_loops = 0
    while spawn_loops < 1:
        
        time.sleep(0.001)
        tile1 = random.choice(coordinates)
       
        ##tile2 = random.choice(coordinates)
        
        print(tile1)
        
        if tile1  == 'A1' or tile1 == 'A2' or tile1 == 'A3' or tile1 == 'A4':
            tile_y_var = 70
        elif tile1 == 'B1' or tile1 == 'B2' or tile1 == 'B3' or tile1 == 'B4':
            tile_y_var = 175
        elif tile1 == 'C1' or tile1 == 'C2' or tile1 == 'C3' or tile1 == 'C4':
            tile_y_var = 280
        elif tile1 == 'D1' or tile1 == 'D2' or tile1 == 'D3' or tile1 == 'D4':
            tile_y_var = 385
        
        
        if tile1  == 'A1' or tile1 == 'B1' or tile1 == 'C1' or tile1 == 'D1':
            tile_x_var = 15
        elif tile1 == 'A2' or tile1 == 'B2' or tile1 == 'C2' or tile1 == 'D2':
            tile_x_var = 120
        elif tile1 == 'A3' or tile1 == 'B3' or tile1 == 'C3' or tile1 == 'D3':
            tile_x_var = 225
        elif tile1 == 'A4' or tile1 == 'B4' or tile1 == 'C4' or tile1 == 'D4':
            tile_x_var = 330
        
        print(tile_x_var,  tile_y_var)
        
        def tile_two():
            screen.blit(two_tile,  (tile_x_var,  tile_y_var))
        def tile_four():
            screen.blit(four_tile,  (tile_x_var,  tile_y_var))
        two = tile_two()
        four = tile_four()
        
        random.sample([tile_two,  tile_four],1)[0]()
    
        pygame.display.flip()
        spawn_loops = spawn_loops +1

