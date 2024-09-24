from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
temp = 0
while (True):
    while(temp % 2 == 0):
        while(x < 790):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 5
            delay(0.01)
        while(y < 600):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y + 5
            delay(0.01)
        while(x > 0):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x - 5
            delay(0.01)
        while(y > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y - 5
            delay(0.01)
        while(x < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 5
            delay(0.01)
        temp = temp + 1
    while(temp % 2 == 1):
        radius = 0
        while(radius < 360):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = 400 + 400 * math.sin((540 - radius) / 360 * 2 * math.pi)
            y = 390 + 300 * math.cos((540 - radius) / 360 * 2 * math.pi)
            radius = radius + 2
            delay(0.01)
        temp = temp + 1
    
    
    

# fill here

close_canvas()
