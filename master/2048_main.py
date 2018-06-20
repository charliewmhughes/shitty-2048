#Written by Charlie Hughes. Since I can't stop you using this, do with it what you will. Also, I know it won't stop you, but don't delete this comment, because I did all the hard work and deserve at least this tiny bit of recognition. Thanks.

#okay so basically this program just describes what happens in a game of 2048, all the real magic is in the 'actions' module.

#import sum modules
import actions
import time

#running variable
running = 1

#draw the background on the window
actions.draw_background()    
#wait a sec. Well not a sec, but you get what I mean.
time.sleep(0.001)
#spawn two tiles at the start
actions.spawn_tile()
actions.spawn_tile()
#loop forever:
while True:
    #check for changes to the tile layout, and if so, then update the screen to show it:
    actions.update_screen() 
    #check for input and move tiles around accordingly.
    actions.key_control()
    #timeout so that you don't chew up CPU power. Also, you might not want to change this lest you make the game slow and laggy. I found that this timeout was the best compromise between low CPU time, and low lag time.
    time.sleep(0.005)
    
#mkay that's it, just as the vinyl I was listening to finished. Nice timing huh?
