import pygame

class Animal(pygame.sprite.Sprite):
    
    def __init__(self, x, y, name, anim_img, ground):
        """
        Initializes animal object

        Args:
            x (int): x position of the animal
            y (int): y position of the animal
            name (str): name of animal
            anim_img (str): path to animal image
            ground (int): ground level coordinate
        """
        super().__init__()
        self.initial_jump_velocity = -15
        self.x = x
        self.y = y
        self.name = name
        self.anim_img = anim_img
        self.ground = ground

        self.image = pygame.image.load(anim_img)  
        self.image = pygame.transform.scale(self.image, (70, 70))  
        self.rect = self.image.get_rect(topleft=(x, y)) 
        
        self.energy = 100
        self.happiness = 100
        self.hunger = 10
        self.is_jumping = False
        self.jump_speed = -15
        self.gravity = 1
        self.jump_height = 100
        self.move_up = 0
        self.money = 0
        self.jump_count = 0
        self.max_jump_count = 10

        self.hunger_interval = 7000
        self.hunger_lapse = pygame.time.get_ticks()
        
        
    def jump(self):
        """
        starts a jump
        """
        if not self.is_jumping: 
            self.is_jumping = True
            self.move_up = self.initial_jump_velocity * 1.5

    def is_animal_alive(self):
        """
        checks the animals statistics to make sure it is still alive

        Returns:
            boolean: if the animal is alive
        """
        if self.hunger > 100 or self.happiness < 0 or self.energy < 0:
                return False
        else:
            return True

    def feed(self, food, food_cost):
        """
        checks to see if play has enough to feed and changes stats if they do
        """
        if self.money >= food_cost:
                self.hunger -= 10
                self.energy += 10
                self.money -= 5

    def play(self):
        """
        checks to see if the animal has enough energy to play and changes stats if it does
        """
        if self.energy > 10:
            self.energy -= 10
            self.happiness += 20
            self.hunger += 10
            
    def update(self):
        """
        updates the jump and stat functions of the animal
        """
        if self.is_jumping:      
                self.move_up += self.gravity
                self.rect.y += self.move_up
                self.jump_count += 1
      
        if self.rect.y >= self.ground:
            self.rect.y = self.ground
            self.is_jumping = False
            self.jump_count = 0
                
        current_time = pygame.time.get_ticks()
        
        if not self.is_animal_alive():
            return False
        
        if (current_time - self.hunger_lapse) >= self.hunger_interval:
            self.hunger += 2
            self.hunger_lapse = current_time
            self.happiness -= 2
        return True