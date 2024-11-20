class Animal:
    def __init__ (self, x, y, anim_img):
        """
        Initializes animal object

        Args:
            x (int): starting x coordinate
            y (int): starting y coordinate
            anim_img (str): path to img file
        """
        self.x = abs(x)
        self.y = abs(y)
        self.img = anim_img
        self.health = 100
        self.hunger = 0
        self.energy = 100
        self.happiness = 0
        
        
    def move_right(self):
        """
        moves position right by 1
        """
        pass
    
    def move_left(self):
        """
        moves position left by 1
        """
        pass
    
    def jump(self):
        """
        moves position up and down by 1
        """
        pass
    
    def feed(self,food):
        """
        Lower hunger and increase health based on food

        Args:
            food (str): type of food given to the pet
        """
        pass
    
    def play (self):
        """
        Increases happiness, decreases energy
        """
        pass
    
    def stats(self):
        """
        Updates the pets stats as actions happen
        """
        pass
    
        
