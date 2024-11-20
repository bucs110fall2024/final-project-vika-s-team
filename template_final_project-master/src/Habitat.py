class Habitat:
    def __init__(self,screen_img):
        """
        initializes the habitat

        Args:
            screen_img (str): path to img file
        """
        
        self.screen_img = screen_img
        
        #initialize backgorund aspects
        self.time = "day"
        self.weather = "clear"
    
        # #import different backgrounds
        self.time_of_day = pygame.image.load(screen_img)
    def update_props(self):
        """
        updates the properties of the background as the user makes choices
        """
        pass
    