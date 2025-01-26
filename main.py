import pygame
from constants import *
from player import Player

def main():    
    #game stuff
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    #player instance
    Player.containers = (updatable, drawable)
    
    Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
        
    
    
    
if __name__ == "__main__":
    main()