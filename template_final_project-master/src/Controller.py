import pygame
from src.Animal import Animal
from src.Habitat import Habitat

class Controller:
  
  def __init__(self):
    #setup pygame data
    pass
  
  def mainloop(self):
    #select state loop
    while(True):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
          
    pygame.display.flip()
    pass
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
    pass
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    pass
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
    pass
