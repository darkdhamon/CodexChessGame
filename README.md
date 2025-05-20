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
  The Windows launcher will automatically install required Python packages if
  they are missing.

You can also run the game directly using Python:

```sh
python -m chess_game.web_app
```

Before running the game ensure the required Python packages are installed:

```sh
pip install -r requirements.txt
```

Once started, open `http://localhost:5000` in your browser.
Click on a piece and then a target square to make a move. The move history appears next to the board.
