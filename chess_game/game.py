from __future__ import annotations

from .controllers.game_controller import GameController
from .views.console_view import ConsoleView


def main() -> None:
    view = ConsoleView()
    controller = GameController(view)
    controller.run()


if __name__ == "__main__":
    main()
