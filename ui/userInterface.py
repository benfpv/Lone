from ui.gameButton import Button

class UserInterface:
    def __init__(self, game, screen, users, player_index):
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
        
        # Global texts
        self.globalTexts = [] # Need this
        self.globalTextsPositions = [] # Need this
        playername = users[player_index].name
        playermoney = users[player_index].money
        self.globalTexts.append(smallfont.render("Player: {}".format(playername), True, color))
        self.globalTextsPositions.append((0,40))
        self.globalTexts.append(smallfont.render("Money: {}".format(playermoney), True, color))
        self.globalTextsPositions.append((0,80))
    
    def update_buttons_hover(self, mouse):
        self.draw(mouse)
        return 
    
    def update_mouseclick(self, mouse):
        buttonIsClicked, buttonIndex = self.check_mouseclick(mouse)
        if buttonIsClicked: # mouse button click event
            buttonClicked = self.current_page.buttons[buttonIndex]
            print("- buttonIndex: {}, buttonClicked: {}".format(buttonIndex, buttonClicked))
            pass
        return
        
    def update_global_texts(self, users, player_index):
        playername = users[player_index].name
        playermoney = users[player_index].money
        self.globalTexts.append(smallfont.render("Player: {}".format(playername), True, color))
        self.globalTexts.append(smallfont.render("Money: {}".format(playermoney), True, color))
        return
    
    def draw(self, mouse):
        # Draw Current Page
        if (self.current_page.buttons):
            for button in self.current_page.buttons:
                button.draw(self.game, self.screen, mouse)
        if (self.current_page.texts):
            for i in range(len(self.current_page.texts)):
                thisText = self.current_page.texts[i]
                thisTextPosition = self.current_page.textsPositions[i]
                self.screen.blit(thisText, thisTextPosition)
        # Draw Global Items
        if (self.globalTexts):
            for i in range(len(self.globalTexts)):
                thisText = self.globalTexts[i]
                thisTextPosition = self.globalTextsPositions[i]
                self.screen.blit(thisText, thisTextPosition)
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
        # Texts
        self.texts = [] # Need this
        self.textsPositions = [] # Need this
        
        self.texts.append(smallfont.render("Homepage", True, color))
        self.textsPositions.append((0, 0))
        
        # Buttons
        self.buttons = [] # Need this
        
        self.buttons.append(Button(140, 40, width/2-200, height/2, color_light, color_hover, "Buy"))
        self.buttons.append(Button(140, 40, width/2+200, height/2, color_light, color_hover, "Sell"))
        self.buttons.append(Button(140, 40, width/2-200, height/2+200, color_light, color_hover, "Inventory"))
        self.buttons.append(Button(140, 40, width/2+200, height/2+200, color_light, color_hover, "Quit"))
        
        return
        
class Buypage:
    def __init__(self, game, width, height, smallfont, color, color_light, color_hover):
        pass