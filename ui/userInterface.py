from ui.gameButton import Button

class UserInterface:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        smallfont = game.font.SysFont('Corbel',36)    # defining a font
        color = (255,255,255)        # white color 
        color_light = (170,170,170)  # light shade of the button
        color_hover = (100,100,100)   # dark shade of the button
        self.width = screen.get_width()   # stores the width of the screen
        self.height = screen.get_height() # stores the height of the screen
        # Pages - every page needs self.buttons even if it is empty [].
        self.homepage = Homepage(self.game, self.width, self.height, smallfont, color, color_light, color_hover)
        self.current_page = self.homepage
    
    def update_buttons_hover(self, mouse):
        self.draw(mouse)
        return 
    
    def update_mouseclick(self, mouse):
        buttonIsClicked, buttonIndex = self.check_mouseclick(mouse)
        buttonClicked = self.current_page.buttons[buttonIndex]
        if buttonIsClicked: # mouse button click event
            print("- buttonIndex: {}, buttonClicked: {}".format(buttonIndex, buttonClicked))
            pass
        return
    
    def draw(self, mouse):
        if (self.current_page.buttons):
            for button in self.current_page.buttons:
                button.draw(self.game, self.screen, mouse)
        self.screen.blit(self.current_page.nameText, (self.width/2-200, self.height/2-200))
        self.screen.blit(self.current_page.networthText, (self.width/2-200, self.height/2-100))
        return
        
    def check_mouseclick(self, mouse):
        buttonIndex = -1
        if (self.current_page.buttons):
            buttonIndex = 0
            for button in self.current_page.buttons:
                if (button.click(self.game, mouse)):
                    return True, buttonIndex
                buttonIndex += 1
        return False, buttonIndex
    
class Homepage:
    def __init__(self, game, width, height, smallfont, color, color_light, color_hover):
        # Title Text
        self.nameText = smallfont.render('Username: Jeff' , True , color) # rendering a text written in this font
        self.networthText = smallfont.render('Net Worth: 1,000,000,000' , True , color) # rendering a text written in this font

        # Buttons
        self.buttons = [] # Do not delete this
        
        self.buttons.append(Button(140, 40, width/2-200, height/2, color_light, color_hover, "Buy"))
        self.buttons.append(Button(140, 40, width/2+200, height/2, color_light, color_hover, "Sell"))
        self.buttons.append(Button(140, 40, width/2-200, height/2+200, color_light, color_hover, "Inventory"))
        self.buttons.append(Button(140, 40, width/2+200, height/2+200, color_light, color_hover, "Quit"))
        
        return
        
class Buypage:
    def __init__(self, game, width, height, smallfont, color, color_light, color_hover):
        pass