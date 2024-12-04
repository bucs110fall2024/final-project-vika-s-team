import pygame
import random
from src.Obstacle import Obstacle

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

class Game:
    def __init__(self, animal):
        """
        initializes the game state for walk

        Args:
            animal (Animal): the animal object
        """
        self.animal = animal
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption(f"{self.animal.name}'s Walk Time")
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.ground_y = 250
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.rewards = []
        
        self.all_sprites.add(self.animal)

    def spawn_reward(self):
        """
        creates the coin reward and adds it to a list of rewards
        """       
        x = 800
        y = self.ground_y - 100    
        reward = pygame.Rect(x,y,100,100)
        self.rewards.append(reward)
       
    def spawn_obstacle(self):
        """
        creates the obstacles and adds it to a list of obstacles
        """
        obstacle_type = random.choice(["cloud", "trash_can"])
        x = 800
        y = self.ground_y
        if obstacle_type == "cloud":
            y = self.ground_y - 150
        obstacle = Obstacle(obstacle_type, x, y)
        self.obstacles.add(obstacle)
        self.all_sprites.add(obstacle)

    def update_obstacles(self):
        """
        update obstacles and check for collisions
        """
        self.all_sprites.update()
        if pygame.sprite.spritecollide(self.animal, self.obstacles, False):
            self.running = False
 
    def draw(self):
        """
        draws the score and instructions on the screen 
        """
        x = 10
        y = 10
        self.screen.fill((WHITE))
        pygame.draw.rect(self.screen, (GREEN), (0, self.ground_y, 800, 150))
        self.all_sprites.draw(self.screen)
        score_text = pygame.font.Font(None, 36).render(f"Score: {self.score}", True, (BLACK))
        self.screen.blit(score_text, (x, y))
        score_text = pygame.font.Font(None, 26).render(f"Press space to jump over trash cans and avoid clouds", True, (BLACK))
        self.screen.blit(score_text, (x, y+20))
        score_text = pygame.font.Font(None, 26).render(f"Collect yellow coins for money", True, (BLACK))
        self.screen.blit(score_text, (x, y+40))

    def game_loop(self):
        """
        game loop
        """
        spawn_timer = 0
        while self.running:
            spawn_timer += 1
            if spawn_timer % 120 == 0:
                self.spawn_obstacle()

            self.update_obstacles()
            self.draw()
                   
            if random.randint(0, 100) == 0:
               self.spawn_reward()
        
            for reward in self.rewards:
                reward.x -= 3
                pygame.draw.circle(self.screen, (YELLOW), (reward.x,reward.y),10)
                if reward.colliderect(self.animal):
                    self.rewards.remove(reward)
                    self.animal.money +=1
                    self.score += 1
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.animal.jump()

            pygame.display.flip()
            self.clock.tick(60)

    def end_game(self):
        """
        handles all activities that happen after the mini game ends 
        """
        self.animal.energy -= 10 
        self.animal.happiness += 5 
        self.animal.rect.topleft = (100, 300) 
        self.animal.jump_count = 0
        money_earned = self.score
        self.animal.money += money_earned
        
        self.running = False
