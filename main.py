import sys
import pygame
from pygame.event import Event

from config import *
from colors import *
from utils.World import World
from Enity.Snake import Snake
from Enity.Food import Food

DIRECTIONS = [
    "UP",
    "DOWN",
    "LEFT", 
    "RIGHT"
]

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Greedy Snake")
clock = pygame.time.Clock()

running = True
world = World("world/world1.json", WIDTH, HEIGHT)
snake = Snake(screen, world)
food = Food.get_instance(screen, world)

def update_world(screen:pygame.Surface, world:World):
    world_height = world.get_height()
    world_width = world.get_width()
    block_height = world.get_block_height()
    block_width = world.get_block_width()
    for h in range(1, world_height):
        pygame.draw.line(screen, BLACK, (0, h*block_height), (WIDTH, h*block_height), 1)
    for w in range(1, world_width):
        pygame.draw.line(screen, BLACK, (w*block_width, 0), (w*block_width, HEIGHT), 1)

def key_event(event:Event):
    if event.key == pygame.K_UP:
        snake.set_direction("UP")
    elif event.key == pygame.K_DOWN:
        snake.set_direction("DOWN")
    elif event.key == pygame.K_LEFT:
        snake.set_direction("LEFT")
    elif event.key == pygame.K_RIGHT:
        snake.set_direction("RIGHT")

def collide(snake:Snake, food:Food):
    """
    check if the snake collide with the food
    """
    if snake.get_head() == food.get_position():
        snake.append_snake_body()
        food.re_generate()
    
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key_event(event)

    clock.tick(FPS)
    screen.fill(WHITE)
    update_world(screen, world)
    snake.update()
    food.update()
    collide(snake, food)
    pygame.display.update()
