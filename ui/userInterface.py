from ui.gameButton import Button

class UserInterface:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        color = (255,255,255)        # white color 
        color_light = (170,170,170)  # light shade of the button
        color_hover = (100,100,100)   # dark shade of the button
        self.width = screen.get_width()   # stores the width of the screen
        self.height = screen.get_height() # stores the height of the screen
        # Pages
        self.homepage = Homepage(self, self.game, self.screen, self.width, self.height, color, color_light, color_hover)
        self.current_page = self.homepage
    
    def draw(self, mouse):
        for button in self.current_page.buttons:
            button.draw(self.game, self.screen, mouse)
        self.screen.blit(self.current_page.nameText, (self.width/2-200, self.height/2-200))
        self.screen.blit(self.current_page.networthText, (self.width/2-200, self.height/2-100))
        return
        
    def click(self, mouse):
        for button in self.current_page.buttons:
            if (button.click(self.game, mouse)):
                return True
        return False
    
class Homepage:
    def __init__(self, userInterface, game, screen, width, height, color, color_light, color_hover):
        # Title Text
        smallfont = game.font.SysFont('Corbel',36)    # defining a font
        self.nameText = smallfont.render('Username: Jeff' , True , color) # rendering a text written in this font
        self.networthText = smallfont.render('Net Worth: 1,000,000,000' , True , color) # rendering a text written in this font

        # Buttons
        self.buttons = []
        self.buttons.append(Button(140, 40, width/2-200, height/2, color_light, color_hover, "Buy"))
        self.buttons.append(Button(140, 40, width/2+200, height/2, color_light, color_hover, "Sell"))
        self.buttons.append(Button(140, 40, width/2-200, height/2+200, color_light, color_hover, "Inventory"))
        self.buttons.append(Button(140, 40, width/2+200, height/2+200, color_light, color_hover, "Quit"))