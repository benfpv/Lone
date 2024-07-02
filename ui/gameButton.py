import pygame as game

class Button:
    def __init__(self, width, height, x, y, color, colorHover, text):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.colorHover = colorHover
        smallfont = game.font.SysFont('Corbel',35)    # defining a font
        textcolor = (255,255,255)
        self.text = text
        self.surface = smallfont.render(text , True , textcolor) # rendering a text written in this font

    def isOn(self, otherX, otherY):
        if self.x < otherX < self.x + self.width and self.y < otherY < self.y + self.height:
            return True
        return False

    def draw(self, game, screen, mouse):
        if self.isOn(mouse[0],mouse[1]):
            game.draw.rect(screen,self.colorHover,[self.x , self.y, self.width, self.height])
            screen.blit(self.surface, (self.x,self.y)) # superimposing the text onto our button
        else:
            game.draw.rect(screen,self.color,[self.x , self.y, self.width, self.height])
            screen.blit(self.surface, (self.x,self.y))
        

    def click(self, game, mouse):
        if self.isOn(mouse[0],mouse[1]):
            return True
        return False