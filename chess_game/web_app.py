from __future__ import annotations

from .controllers.web_controller import WebController
import webbrowser
import threading


def main() -> None:
    controller = WebController()
    threading.Timer(1.0, lambda: webbrowser.open("http://localhost:5000")).start()
    controller.run()


if __name__ == "__main__":
    main()
