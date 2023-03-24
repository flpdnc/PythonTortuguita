#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50

    # Solarized-dark color theme
    BACKGROUND_COLOR = tcod.Color(7, 54, 66)
    FOREGROUND_COLOR = tcod.Color(131, 148, 150)

    ##
    player_x = int(SCREEN_WIDTH / 2)
    player_y = int(SCREEN_HEIGHT / 2)
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

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
            root_console.print(x=player_x, y=player_y, string="@", fg=FOREGROUND_COLOR)
            
            context.present(root_console)
            
            root_console.clear(bg=BACKGROUND_COLOR)

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()
