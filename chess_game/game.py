from __future__ import annotations

from .controllers.game_controller import GameController
from .views.browser_view import BrowserView


def main() -> None:
    view = BrowserView()
    controller = GameController(view)
    controller.run()


if __name__ == "__main__":
    main()
