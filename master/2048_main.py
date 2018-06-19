import actions
import time

running = 1

actions.draw_background()    
time.sleep(0.001)
actions.spawn_tile()
actions.spawn_tile()
while True:
    actions.update_screen() 
    actions.key_control()
    time.sleep(0.005)
