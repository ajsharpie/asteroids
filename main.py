import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():    
    #game stuff
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #player instance
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    
    #asteroid things
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()
    
    #shots
    Shot.containers = (updatable, drawable, shots)
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        for thing in updatable:
            thing.update(dt)
            
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()
                
            for shot in shots:
                if asteroid.is_colliding(shot):
                   asteroid.split()
                   shot.kill()
                   
        #visuals 
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        #framerate @60
        dt = clock.tick(60)/1000
        
        
    
    
    
if __name__ == "__main__":
    main()