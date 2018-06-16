import actions
import time

running = 1

actions.draw_background()    
time.sleep(0.001)
actions.spawn_tile()
actions.spawn_tile()
while running:
    actions.sense_key()
    actions.draw_background()
    counter = 0
    while counter < 17:
        actions.update_screen()
        counter +=1
    
    time.sleep(0.001)
