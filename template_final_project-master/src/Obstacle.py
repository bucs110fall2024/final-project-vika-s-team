import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type, x, y):
        """
        initializes the obstacle object

        Args:
            obstacle_type (str): which of the 2 obstacles is chosen
            x (int): x position of obstacle
            y (int): y position of obstacle
        """
        super().__init__()
        self.x = x
        self.y= y
        self.type = obstacle_type
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
        if self.type == "cloud":
            self.image = pygame.image.load("assets/cloud.png")
            self.image = pygame.transform.scale(self.image, (60, 60))
        elif self.type == "trash_can":
            self.image = pygame.image.load("assets/trash_can_3.png")
            self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        """
        moves the obstacle over the x axis
        """
        self.rect.x -= 5 
        if self.rect.x < -50:
            self.kill()