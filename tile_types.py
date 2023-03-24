from typing import Tuple
from tcod import Color
from color_palette import SolarizedDark as sd

import numpy as np # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # unicode codepoint.
        ("fg", "3B"), # 3 unsigned bytes, for RGB colors
        ("bg", "3B"),
    ]
)

# Tile struct used for statistically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool_), # True if this tile can be walked over
        ("transparent", np.bool_), # True if this tile doesn't block FOV
        ("dark", graphic_dt), # Graphics for when this tile is not in FOV
    ]
)

def new_tile(
    *, # Enforce the use of keywords, so that param order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Color, Color],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), sd.BASE02, sd.BASE03),
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord("H"), sd.BASE00, sd.BASE01),
)


