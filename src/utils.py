"""This module contains utilities functions."""

from pygame.image import load


def load_sprite(sprite_name, with_alpha=True):
    """
    Loads a sprite in the game.

    Args:
        sprite_name(str): name of the image.
        with_alpha(bool): Default set to True

    Returns:
        sprite: game sprite 
    """
    sprite_path = f"src/assets/sprites/{sprite_name}.png"
    loaded_sprite = load(sprite_path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    
    return loaded_sprite.convert() 