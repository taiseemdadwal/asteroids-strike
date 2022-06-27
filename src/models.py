from pygame.math import Vector2

class AsteroidGameObject(object):
    """Parent Game Object to be derived from."""
    
    def __init__(self, sprite, position, velocity):
        self.sprite = sprite
        self.position = Vector2(position)
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        """Draw a given surface on screen.

        Args:
            surface(pygame.display object): surface object
        """
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self):
        """Moves the position of game object."""
        self.position = self.position + self.velocity
    
    def detect_collision_with(self, other_object):
        """Returns if game objects have collided or not.
        
        Args:
            other_object(GameObject object): Other GameObject class object
        
        Returns:
            bool: True if collision detected else False
        """
        distance = self.position.distance_to(other_object.position)
        
        return distance < self.radius + other_object.radius
