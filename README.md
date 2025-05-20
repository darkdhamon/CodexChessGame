# CodexChessGame

A simple chess game for two players in hotseat mode. The project is written in Python using an MVC structure.
By default the board is displayed in your web browser.

## Running the game

Use the launcher script for your operating system:

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
python -m chess_game.game
```

During the game, players take turns entering moves in algebraic form, e.g. `e2 e4`. Type `quit` or `exit` to end the session.
