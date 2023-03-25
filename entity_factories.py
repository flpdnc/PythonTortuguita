from color_palette import SolarizedDark as sd
from entity import Entity

player = Entity(char="@", color=sd.BASE3, name="Player", blocks_movement=True)

orc = Entity(char="o", color=sd.GREEN, name="Orc", blocks_movement=True)
troll = Entity(char="T", color=sd.ORANGE, name="Troll", blocks_movement=True)
