# CodexChessGame

A simple chess game for two players in hotseat mode. The project is written in Python using an MVC structure.
The game now runs as a small web application so that you can play entirely from your browser.

## Running the game

Use the launcher script for your operating system to start the web server:

- On Linux or macOS:
  ```sh
  ./launch_unix.sh
  ```
- On Windows:
  ```cmd
  launch_windows.bat
  ```

You can also run the game directly using Python:

```sh
python -m chess_game.web_app
```

Once started, open `http://localhost:5000` in your browser. Enter moves like `e2 e4` in the provided form.
The web application requires the `flask` package to be installed.
