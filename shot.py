from circleshape import *
from constants import PLAYER_SHOT_SPEED

class Shot(CircleShape):
    
    def __init__(self, x, y, radius):
        
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        
    def draw(self, screen):
        center = self.position
        pygame.draw.circle(screen, "white", center, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity)*dt