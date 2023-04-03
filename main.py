#!/usr/bin/env python3
import copy
import traceback

import tcod

import color
from color_palette import SolarizedDark
from engine import Engine
import entity_factories
from procgen import generate_dungeon


def main() -> None:
    # Constants:
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50

    MAP_WIDTH = 80
    MAP_HEIGHT = 43

    # Solarized-dark color theme
    BACKGROUND_COLOR = SolarizedDark.BASE02
    FOREGROUND_COLOR = SolarizedDark.BASE0
    PLAYER_COLOR = SolarizedDark.BASE03
    NPC_COLOR = SolarizedDark.BLUE

    # Room constraints
    ROOM_MAX_SIZE = 15
    ROOM_MIN_SIZE = 6
    MAX_ROOMS = 10

    MAX_MONSTERS_PER_ROOM = 2
    MAX_ITEMS_PER_ROOM = 2

    ########

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=MAX_ROOMS,
        room_min_size=ROOM_MIN_SIZE,
        room_max_size=ROOM_MAX_SIZE,
        map_width=MAP_WIDTH,
        map_height=MAP_HEIGHT,
        max_monsters_per_room=MAX_MONSTERS_PER_ROOM,
        max_items_per_room=MAX_ITEMS_PER_ROOM,
        engine=engine,
    )

    engine.update_fov()

    engine.message_log.add_message(
            "Hello and welcome, adventurer, to yet another dungeon!", color.welcome_text
        )

    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        while True:
            root_console.clear(bg=BACKGROUND_COLOR)
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            try:
                for event in tcod.event.wait():
                    context.convert_event(event)
                    engine.event_handler.handle_events(event)
            except Exception:  # Handle exceptions in game.
                traceback.print_exc()  # Print error to stderr.
                # Then print the error to the message log.
                engine.message_log.add_message(traceback.format_exc(), color.error)


if __name__ == "__main__":
    main()
