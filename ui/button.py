class Button:

    def __init__(self, width, height, x, y, color, colorHover):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.colorHover = colorHover

    def isOn(self, otherX, otherY):
        if self.x < otherX < self.x + self.width and self.y < otherY < self.y + self.height:
            return True
        return False

    def draw(self, game, screen):
        game.draw.rect(screen,self.color,[self.x , self.y, self.width, self.height])

    def hover(self, game, screen, mouse):
        if self.isOn(mouse[0],mouse[1]):
            game.draw.rect(screen, self.colorHover, [self.x,self.y,self.width,self.height])   
        else:
            game.draw.rect(screen, self.color, [self.x,self.y,self.width,self.height])

    def click(self, game, mouse):
        if self.isOn(mouse[0],mouse[1]):
            game.quit()