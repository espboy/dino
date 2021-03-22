from machine import Pin,I2C
import ssd1306
import gfx
from time import sleep_ms,sleep
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)
graphics = gfx.GFX(128, 32, display.pixel)
from sprite import Sprite
from screen import Screen
    
        


#display.text("1",10, 10)
#graphics.line(0, 0, 127, 20, 1)
#graphics.circle(10, 10, 4, 1)
#display.show()
isgameover=False
screen = Screen(128,32,display)
player = Sprite(10,16,'''
0000000000111111100
0000000001101111111
0000000001111111111
0000000001111111111
0000000001111000000
1000000001111111100
1000000011110000000
1100001111110000000
1110011111111100000
0011111111110100000
0000111111110000000
0000011101100000000
0000011000100000000
0000010000100000000
0000011000110000000
''')

enemy=Sprite(80,12,'''
00000011100000
00000111110000
00000111110000
00000111110000
01100111110000
01100111110000
01100111110110
01100111110110
01100111110110
01100111110110
00110111111100
00011111111000
00001111110000
00000111110000
00000111110000
00000111110000
00000111110000
00000111110000
00000111110000
''')

bg=Sprite(0,28,'''
0000011100000000000000000000000000011110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
1111110011111111111111111111111111110001111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0001000100000011000001000000110000000001110000000000000000000000000100000000000000000000010000000000000000000000000100000000000
''')

bg2=Sprite(128,28,'''
0000011100000000000000000000000000011110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
1111110011111111111111111111111111110001111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0001000100000011000001000000110000000001110000000000000000000000000100000000000000000000010000000000000000000000000100000000000
''')



screen.add_player_sprite(player)
screen.add_enemy_sprite(enemy)
screen.add_bg_sprite(bg)
screen.add_bg_sprite(bg2)
screen.clear()
screen.show()

def gameover():
    display.text('game over',30, 10)

while True:
    screen.clear()
    if isgameover:
        gameover()
        display.show()
    else:
        bg.x-=2
        bg2.x-=2
        if bg.x<=-128:
            bg.x=128
        if bg2.x<=-128:
            bg2.x=128
        enemy.x-=2
        if enemy.x<=-10:
            enemy.x=128
        screen.show()
    #sleep_ms(1)
