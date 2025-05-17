import pygame
import random
from utils.Block import Block
from utils.World import World
from colors import *
clock = pygame.time.Clock()

DICTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

class Snake(pygame.sprite.Sprite):
    def __init__(self, screen:pygame.Surface ,world: World):
        super().__init__()
        self.world_size = (world.get_width(), world.get_height())
        self.world = world
        self.x, self.y = self.get_intial_position()
        self.snake_length = 1
        self.direction = "UP"
        self.screen = screen
        self.snake_body = [self.world.get_block(self.x, self.y)]

    def is_self_body(self):
        """
        check if the snake collide with itself
        """
        return len(set(self.snake_body)) != len(self.snake_body)


    def get_head(self):
        """
        get the head of the snake
        """
        return self.x, self.y

    def set_direction(self, direction: str):
        """
        set the direction of the snake
        """
        if direction in DICTIONS:
            self.direction = direction
        else:
            raise ValueError("Invalid direction")

    def append_snake_body(self):
        """
        append a new block to the snake body
        """
          
        block_x, block_y = self.snake_body[0].get_position()
        direction = self.direction
        for i in range(1, self.snake_length):
            b = self.snake_body[i]
            b_x, b_y = b.get_position()
            if b_x == block_x and b_y == block_y-1:
                direction = "UP"
            elif b_x == block_x and b_y == block_y+1:
                direction = "DOWN"
            elif b_x == block_x-1 and b_y == block_y:
                direction = "LEFT"
            elif b_x == block_x+1 and b_y == block_y:
                direction = "RIGHT"
            block_x, block_y = b_x, b_y
        if direction == "UP":
            self.snake_body.append(self.world.get_block(block_x, (block_y + 1) % self.world_size[1]))
        elif direction == "DOWN":
            self.snake_body.append(self.world.get_block(block_x, (block_y - 1) % self.world_size[1]))
        elif direction == "LEFT":
            self.snake_body.append(self.world.get_block((block_x + 1) % self.world_size[0], block_y))
        elif direction == "RIGHT":
            self.snake_body.append(self.world.get_block((block_x - 1) % self.world_size[0], block_y))
                
        self.snake_length += 1
        

    def _update_snake_body(self):
        """
        update the snake body position
        """
        for i in range(self.snake_length-1, 0, -1):
            self.snake_body[i] = self.snake_body[i-1]
        self.snake_body[0] = self.world.get_block(self.x, self.y)


    def _draw_snake_body(self):
        """
        draw the snake body in the world
        """
        for block in self.snake_body:
            self.draw_black(*block.get_position())

    def draw_black(self, x, y):
        """
        draw a black block in the world
        """
        block = self.world.get_block(x, y)
        pygame.draw.rect(self.screen, BLACK, block.get_rect())


    def get_intial_position(self):
        """
        get a random position in the world in intialization
        """
        x = random.randint(0, self.world_size[0] - 1)
        y = random.randint(0, self.world_size[1] - 1)
        return (x, y)
    
    def print_body_position(self):
        """
        print the position of the snake body
        """
        body = []
        for block in self.snake_body:
            body.append(block.get_position())
        print(body)

    def update(self):
        """
        update the snake position and draw it in the world
        """
        clock.tick(6)
        self.x = (self.x + DICTIONS[self.direction][0]) % self.world_size[0]
        self.y = (self.y + DICTIONS[self.direction][1]) % self.world_size[1]
        self._update_snake_body()
        if self.is_self_body():
            raise ValueError("Game Over")
        self._draw_snake_body()
        
        