import pygame
from src.Dog import Dog
from src.Panda import Panda
from src.Snake import Snake
from src.Game import Game
from src.Play import Play
from src.Text import Text

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTBLUE = (200,200,255)
BLUE = (0,0,255)
class Controller:
    def __init__(self):
        """
        initializes the screen and variables
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Animal Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.animal = None
        self.state = 'start' 
        self.message = ""
        self.message_time = 0

    def mainloop(self):
        """
        switches the screens based on the state of the game
        """
        while self.running:
            if self.state == 'start':
                self.welcome_message()
            if self.state == 'menu':              
                self.menuloop()
            elif self.state == 'action':
                self.actionloop()
            elif self.state == 'game':
                self.gameloop()

   

        

    def menuloop(self):
        """
        creates the buttons and checks for user interaction with them. then it changes the screen based on selection
        """
        font = pygame.font.Font(None, 36)
        while self.state == 'menu' and self.running:
            self.screen.fill(WHITE)
            title_text = font.render("Select an Animal", True, (BLACK))
            self.screen.blit(title_text, (300, 100))

            dog_button = pygame.Rect(300, 150, 200, 50)
            panda_button = pygame.Rect(300, 220, 200, 50)
            snake_button = pygame.Rect(300, 290, 200, 50)

            pygame.draw.rect(self.screen, (LIGHTBLUE), dog_button)
            pygame.draw.rect(self.screen, (LIGHTBLUE), panda_button)
            pygame.draw.rect(self.screen, (LIGHTBLUE), snake_button)

            dog_text = font.render("Dog", True, BLACK)
            panda_text = font.render("Panda", True, BLACK)
            snake_text = font.render("Snake", True, BLACK)

            self.screen.blit(dog_text, (375, 165))
            self.screen.blit(panda_text, (365, 235))
            self.screen.blit(snake_text, (365, 305))

            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if dog_button.collidepoint(event.pos):
                        self.animal = Dog(100, 250)
                        self.state = 'action'
                    elif panda_button.collidepoint(event.pos):
                        self.animal = Panda(100, 250)
                        self.state = 'action'
                    elif snake_button.collidepoint(event.pos):
                        self.animal = Snake(100, 250)
                        self.state = 'action'
        
    def actionloop(self):
        """
        creates the menu after the user picks the animal they want
        """

        font = pygame.font.Font(None, 36)
        while self.state == 'action' and self.running:
            self.screen.fill(WHITE)
            title_text = font.render(f"{self.animal.name}'s Actions", True, (BLACK))
            self.screen.blit(title_text, (300, 100))

            feed_button = pygame.Rect(300, 150, 350, 50)
            play_button = pygame.Rect(300, 220, 200, 50)
            walk_button = pygame.Rect(300, 290, 200, 50)

            pygame.draw.rect(self.screen, (LIGHTBLUE), feed_button)
            pygame.draw.rect(self.screen, (LIGHTBLUE), play_button)
            pygame.draw.rect(self.screen, (LIGHTBLUE), walk_button)

            feed_text = font.render("Feed. 1 meal = 5 coins", True, (BLACK))
            play_text = font.render("Play", True, (BLACK))
            walk_text = font.render("Walk", True, (BLACK))

            self.screen.blit(feed_text, (375, 165))
            self.screen.blit(play_text, (375, 235))
            self.screen.blit(walk_text, (375, 305))

            self.display_stats()
            
            is_successful = self.animal.update()
            if not is_successful:
                self.text = Text(self.screen)
                self.screen.fill(WHITE)
                self.text.print_message(message = "Your pet died of hunger:(. press q to exit",x = 220,y = 150)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    self.state = 'menu'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if feed_button.collidepoint(event.pos):
                        if self.animal.money >= 5:
                            self.animal.feed('food', 5)
                        else:
                            font = pygame.font.Font(None, 36)
                            message = "Not enough money! walk your pet"
                            text_display = font.render(message, True, (BLUE))
                            text_rect = text_display.get_rect(center =(280,200))
                            self.screen.blit(text_display, text_rect)
                
                    elif play_button.collidepoint(event.pos):
                        self.state = 'play'
                        play = Play(self.animal)
                        play.display_trivia()
                        self.state = 'action'
                    elif walk_button.collidepoint(event.pos):
                        self.state = 'game'
                        game = Game(self.animal)
                        game.game_loop()
                        self.state = 'action'

    def gameloop(self):
        """
        starts the game if the user chooses to walk the animal 
        """
        while self.state == 'game' and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.running = False

    def display_stats(self):
        """
        displays the animals current stateon the menu screen
        """
        if not self.animal:
            return 
        
        font = pygame.font.Font(None, 36)
        stats = [
            f"Name: {self.animal.name}",
            f"Energy: {self.animal.energy}",
            f"Happiness: {self.animal.happiness}",
            f"Hunger: {self.animal.hunger}",
            f"You have {self.animal.money} dollars",
            f"'b' for different animal",
            f"'q' to quit",
        ]

        x_offset = 10
        y_offset = 10 
        for stat in stats:
            text_surface = font.render(stat, True, (BLACK))
            self.screen.blit(text_surface, (x_offset, y_offset))
            y_offset += 40 

        screen_width, screen_height = self.screen.get_size()
        image_x = screen_width - self.animal.image.get_width() - 10
        image_y = (screen_height // 2) - (self.animal.image.get_height() // 2)
        self.screen.blit(self.animal.image, (image_x, image_y)) 
        
    def welcome_message(self):
        """
        writes the welcome message before the game begins
        """
        start_time = pygame.time.get_ticks() 
        while self.state == 'start' and self.running:
            self.screen.fill(WHITE)
            self.text = Text(self.screen)
            x = 400
            y = 80
            self.text.print_message(message = "Welcome to you pet simulator!", x = x, y = y )
            self.text.print_message(message = "After you choose a pet, you are responsible for keeping it alive", x = x, y  = y + 20)
            self.text.print_message(message = "The pet will die if its hunger reaches above 100, or if its happiness and energy dip below 0", x = x, y  = y + 40)
            self.text.print_message(message = "The hunger goes up by 2 every 2 seconds", x = x, y = y + 60)
            self.text.print_message(message = "You will have to feed the pet to keep it from starving with money you earn by walking the pet or playing with it", x = x, y = y + 80)
            self.text.print_message(message = "Good luck!", x = x, y = y+100)
            self.text.print_message(message = "(This message will automatically disappear)", x = x, y = y + 120)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return

            if pygame.time.get_ticks() - start_time > 10000:
                self.state = 'menu'       