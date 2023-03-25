#!/usr/bin/env python3
import tcod

from color_palette import SolarizedDark
from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    # Constants:
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50

    MAP_WIDTH = 80
    MAP_HEIGHT = 45

    # Solarized-dark color theme
    BACKGROUND_COLOR = SolarizedDark.BASE02
    FOREGROUND_COLOR = SolarizedDark.BASE0
    PLAYER_COLOR = SolarizedDark.BASE03
    NPC_COLOR = SolarizedDark.BLUE

    # Room constraints
    ROOM_MAX_SIZE = 15
    ROOM_MIN_SIZE = 6
    MAX_ROOMS = 10

    ########

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

    game_map = generate_dungeon(
        max_rooms=MAX_ROOMS,
        room_min_size=ROOM_MIN_SIZE,
        room_max_size=ROOM_MAX_SIZE,
        map_width=MAP_WIDTH,
        map_height=MAP_HEIGHT,
        player=player
    )

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
