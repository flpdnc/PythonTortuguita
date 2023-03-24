from tcod import Color 

from color_palette import SolarizedDark


class Entity:
    """
    Generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color


    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
