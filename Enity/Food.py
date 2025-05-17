
import pygame
import random
from utils.World import World
from colors import *

class Food(pygame.sprite.Sprite):
    _instance = None

    def __init__(self, screen: pygame.Surface, world: World):
        super().__init__()
        self.world_size = (world.get_width(), world.get_height())
        self.world = world
        self.screen = screen
        self.x, self.y = self._inital_position()

    @classmethod
    def get_instance(cls, screen: pygame.Surface, world: World):
        """
        get the instance of the food
        """
        if cls._instance is None:
            cls._instance = cls(screen, world)
        return cls._instance


    def _inital_position(self):
        """
        inital the position of the food
        """
        x = random.randint(0, self.world_size[0]-1)
        y = random.randint(0, self.world_size[1]-1)
        return (x, y)
    
    def re_generate(self):
        """
        regenerate the position of the food
        """
        self.x, self.y = self._inital_position()

    def update(self):
        """
        update the position of the food
        """
        block = self.world.get_block(self.x, self.y)
        pygame.draw.rect(self.screen, GREEN, block.get_rect())
    
    def get_position(self):
        """
        get the position of the food
        """
        return (self.x, self.y)
