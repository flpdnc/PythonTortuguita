from color_palette import SolarizedDark as sd
from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@", 
    color=sd.BASE3, 
    name="Player", 
    ai_cls=HostileEnemy,
    fighter = Fighter(hp=100, defense=2, power=5),
)

orc = Actor(
    char="o", 
    color=sd.GREEN, 
    name="Orc", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)

troll = Actor(
    char="T", 
    color=sd.ORANGE, 
    name="Troll", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)
