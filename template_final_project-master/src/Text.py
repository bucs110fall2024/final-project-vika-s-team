import pygame

BLUE = 0, 0, 255
class Text:
    def __init__(self, screen):
        """
        initializes the screen

        Args:
            screen (screen object): screen 
        """
        self.screen = screen  
            
    def print_message(self,message, x, y):  
        """
        displays the message on the screen when called
        Args:
            message (str): message to be displayed
            x (int): x position of the message
            y (int): y position of the message
        """
        self.message = message
        font = pygame.font.Font(None, 20)
        text_display = font.render(self.message, True, (BLUE))
        text_rect = text_display.get_rect(center =(x,y))
        self.screen.blit(text_display, text_rect)