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
text = smallfont.render('text' , True , color) # rendering a text written in this font

button1 = Button(140, 40, width/2-200, height/2, color_light, color_hover, "Buy")
button2 = Button(140, 40, width/2+200, height/2, color_light, color_hover, "Sell")
button3 = Button(140, 40, width/2-200, height/2+200, color_light, color_hover, "Inventory")
button4 = Button(140, 40, width/2+200, height/2+200, color_light, color_hover, "Quit")

smallfont = game.font.SysFont('Corbel',35)    # defining a font
nameText = smallfont.render('Username: Jeff' , True , color) # rendering a text written in this font
smallfont = game.font.SysFont('Corbel',35)    # defining a font
networthText = smallfont.render('Net Worth: 1,000,000,000' , True , color) # rendering a text written in this font
  
while True:
    # stores the (x,y) coordinates into the variable as a tuple
    mouse = game.mouse.get_pos()

    # fills the screen with a color
    screen.fill((60,25,60))

    # if mouse is hovered on a button it
    # changes to lighter shade 
    button1.draw(game, screen, mouse)
    button2.draw(game, screen, mouse)
    button3.draw(game, screen, mouse)
    button4.draw(game, screen, mouse)
    screen.blit(nameText, (width/2-200, height/2-200))
    screen.blit(networthText, (width/2-200, height/2-100))
      
    for ev in game.event.get():
          
        if ev.type == game.QUIT:
            game.quit()
              
        #checks if a mouse is clicked
        if ev.type == game.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            button1.click(game, mouse)
            button2.click(game, mouse)
            button3.click(game, mouse)
            button4.click(game, mouse)
                  
    # updates the frames of the game
    game.display.update()