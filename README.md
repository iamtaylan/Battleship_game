# Battleship Game

This is a simple command-line Battleship game in Python, where two players take turns shooting at each other’s hidden maps. The game continues until one player has no more ships left.

## Table of Contents

- [How It Works](#how-it-works)
- [File Structure](#file-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [Notes](#notes)
- [Contact](#contact)

## How It Works

1. **Maps**: Each player has a map represented by a 2D list of characters:
   - `#` represents a ship cell.
   - `*` represents a hit cell.
   - `o` represents a miss.

2. **Gameplay**:
   - Players take turns shooting at each other's maps.
   - If the shot hits a `#`, it's marked with a `*` on both players' maps.
   - If it misses, it’s marked as `o`.

3. **Game End**: The game ends when all `#` cells on a player’s map have been hit.

## File Structure

- **Map files**: Text files for each player containing a 2D grid where `#` indicates ships.
- **Moves file**: A text file (`battleship/moves.txt`) containing a list of moves in `A,1` format, with each move on a new line.

## Setup

1. Create two map files (e.g., `player1_map.txt` and `player2_map.txt`), each with a 2D grid of characters. Here, `#` denotes the presence of a ship.
2. Create a `moves.txt` file with each move in `Letter,Number` format (e.g., `A,1` represents the first row and first column).

### Sample Map File (`player1_map.txt` or `player2_map.txt`)
```plaintext
.#..#
.....
##..#
.....
.#..#
```

### Sample Moves File (moves.txt)
```plaintext
A,1
B,3
C,2
D,4
E,5
```

## Usage

1. Run the script:
```bash
python battleship.py
```
2. When prompted, enter the file names for each player’s map (e.g., player1_map.txt and player2_map.txt).
3. The game will go through all moves listed in moves.txt and display the results of each shot.

## Example Output

```plaintext
Enter the name of the map file for Player 1: player1_map.txt
Enter the name of the map file for Player 2: player2_map.txt
Player 1 shot: A, 1 - miss
Player 1's map:
.#..#
.....
##..#
.....
.#..#
Player 2's map:
.#..#
.....
##..#
.....
.#..#
...
Game over!
Final maps:
Player 1's map:
.#..#
.....
**..#
.....
*#..#
Player 2's map:
.#..#
.....
**..#
.....
*#..#
```

