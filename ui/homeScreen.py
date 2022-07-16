from ui.gameButton import Button
class HomeScreen:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        color = (255,255,255)        # white color 
        color_light = (170,170,170)  # light shade of the button
        color_hover = (100,100,100)   # dark shade of the button
        self.width = screen.get_width()   # stores the width of the screen
        self.height = screen.get_height() # stores the height of the screen

        self.button1 = Button(140, 40, self.width/2-200, self.height/2, color_light, color_hover, "Buy")
        self.button2 = Button(140, 40, self.width/2+200, self.height/2, color_light, color_hover, "Sell")
        self.button3 = Button(140, 40, self.width/2-200, self.height/2+200, color_light, color_hover, "Inventory")
        self.button4 = Button(140, 40, self.width/2+200, self.height/2+200, color_light, color_hover, "Quit")

        smallfont = game.font.SysFont('Corbel',35)    # defining a font
        self.nameText = smallfont.render('Username: Jeff' , True , color) # rendering a text written in this font
        self.networthText = smallfont.render('Net Worth: 1,000,000,000' , True , color) # rendering a text written in this font

    def draw(self, mouse):
        self.button1.draw(self.game, self.screen, mouse)
        self.button2.draw(self.game, self.screen, mouse)
        self.button3.draw(self.game, self.screen, mouse)
        self.button4.draw(self.game, self.screen, mouse)
        self.screen.blit(self.nameText, (self.width/2-200, self.height/2-200))
        self.screen.blit(self.networthText, (self.width/2-200, self.height/2-100))

    def click(self, mouse):
        if self.button1.click(self.game, mouse) or \
            self.button2.click(self.game, mouse) or \
            self.button3.click(self.game, mouse) or \
            self.button4.click(self.game, mouse):
            return True
        return False