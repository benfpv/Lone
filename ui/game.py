import pygame as game
import sys

from button import Button

# pylint: disable=no-member

game.init()                         # initializing the constructor
res = (720,720)                     # screen resolution
screen = game.display.set_mode(res) # opens up a window
color = (255,255,255)        # white color 
color_light = (170,170,170)  # light shade of the button
color_hover = (100,100,100)   # dark shade of the button
width = screen.get_width()   # stores the width of the screen
height = screen.get_height() # stores the height of the screen
smallfont = game.font.SysFont('Corbel',35)    # defining a font
text = smallfont.render('quit' , True , color) # rendering a text written in this font

button1 = Button(width/2,height/2,140,40,color_light,color_hover)
  
while True:
    # stores the (x,y) coordinates into the variable as a tuple
    mouse = game.mouse.get_pos()

    # fills the screen with a color
    screen.fill((60,25,60))
      
    for ev in game.event.get():
          
        if ev.type == game.QUIT:
            game.quit()
              
        #checks if a mouse is clicked
        if ev.type == game.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            button1.click(game, mouse)
                  
    # if mouse is hovered on a button it
    # changes to lighter shade 
    button1.hover(game, screen, mouse)
      
    # superimposing the text onto our button
    screen.blit(text , (width/2+50,height/2))
      
    # updates the frames of the game
    game.display.update()