from __future__ import annotations

from .controllers.web_controller import WebController


def main() -> None:
    controller = WebController()
    controller.run()


if __name__ == "__main__":
    main()
