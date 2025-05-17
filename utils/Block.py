class Block:
    def __init__(self, x, y, width, height, propertry):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.propertry = propertry
    
    def get_rect(self):
        return (self.x, self.y, self.width, self.height)
    
    def get_propertry(self):
        return self.propertry
    
    def get_position(self):
        return (int(self.x // self.width), int(self.y // self.height))