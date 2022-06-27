import pygame

from models import AsteroidGameObject as GameObject
from utils import load_sprite


class AsteroidsStrike(object):
    """Base class for asteroid strike game."""

    def __init__(self):
        self._initialize_pygame()
        self.screen = pygame.display.set_mode((1366,798))
        self.background = load_sprite("background", False)
        self.clock = pygame.time.Clock()
        self.spaceship = GameObject(
            load_sprite("spaceship"),
            (680, 380),
            (0, 0)
        )
        self.asteroid = GameObject(
            load_sprite("asteroid"),
            (680, 380),
            (1, 0)
        )
    
    def enter_game_loop(self):
        """Main game loop."""
        while True:
            self._handle_user_input()
            self._process_game_logic()
            self._draw_on_screen()
    
    def _initialize_pygame(self):
        """Initialize pygame"""
        pygame.init()
        pygame.display.set_caption("Asteroids Strike")
    
    def _handle_user_input(self):
        """Handle user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

    def _process_game_logic(self):
        """Process game logic like rules of physics."""
        self.spaceship.move()
        self.asteroid.move()

    def _draw_on_screen(self):
        """Draw game graphics on screen."""
        self.screen.blit(self.background,(0,0))
        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)
        # print(f"Collision: {self.spaceship.detect_collision_with(self.asteroid)}")
        pygame.display.flip()
        self.clock.tick(60)