from color_palette import SolarizedDark as sd
from components.consumable import (
        HealingConsumable,
        LightningDamageConsumable,
    )
from components.ai import HostileEnemy
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item

player = Actor(
        char="@", 
        color=sd.BASE3, 
        name="Player", 
        ai_cls=HostileEnemy,
        fighter = Fighter(hp=10, defense=2, power=5),
        inventory=Inventory(capacity=26),
    )

orc = Actor(
        char="o", 
        color=sd.GREEN, 
        name="Orc", 
        ai_cls=HostileEnemy,
        fighter=Fighter(hp=10, defense=0, power=3),
        inventory=Inventory(capacity=0),
    )

troll = Actor(
        char="T", 
        color=sd.ORANGE, 
        name="Troll", 
        ai_cls=HostileEnemy,
        fighter=Fighter(hp=16, defense=1, power=4),
        inventory=Inventory(capacity=0),
    )

health_potion = Item(
        char="!",
        color=sd.MAGENTA,
        name="Health Potion",
        consumable=HealingConsumable(amount=4),
    )

lightning_scroll = Item(
        char="~",
        color=sd.YELLOW,
        name="Lightning Scroll",
        consumable=LightningDamageConsumable(
            damage=20, maximum_range=5),
    )
