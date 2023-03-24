#!/usr/bin/env python3
import tcod

from color_palette import SolarizedDark
from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


def main() -> None:
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50

    MAP_WIDTH = 80
    MAP_HEIGHT = 45

    # Solarized-dark color theme
    BACKGROUND_COLOR = SolarizedDark.BASE02
    FOREGROUND_COLOR = SolarizedDark.BASE0
    PLAYER_COLOR = FOREGROUND_COLOR
    NPC_COLOR = SolarizedDark.GREEN

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(
        x = int(SCREEN_WIDTH / 2),
        y = int(SCREEN_HEIGHT / 2),
        char = "@",
        color = (PLAYER_COLOR)
    )
    npc = Entity(
        x = int(SCREEN_WIDTH / 2 - 5),
        y = int(SCREEN_HEIGHT / 2 - 3),
        char = "@",
        color = (NPC_COLOR)
    )
    entities = {npc, player}

    game_map = GameMap(MAP_WIDTH, MAP_HEIGHT)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        root_console.clear(bg=BACKGROUND_COLOR)
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()
