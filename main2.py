def initialize_map(file_name):
    with open(file_name, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def process_shot(player_map, opponent_map, row, col):
    if opponent_map[row][col] == '#':
        player_map[row][col] = '*'
        opponent_map[row][col] = '*'
        return "hit"
    else:
        player_map[row][col] = 'o'
        return "miss"

def print_map(map):
    for row in map:
        print(''.join(row))

def main():
    player1_map_file = input("Enter the name of the map file for Player 1: ")
    player2_map_file = input("Enter the name of the map file for Player 2: ")

    player1_map = initialize_map(player1_map_file)
    player2_map = initialize_map(player2_map_file)

    moves = []
    with open('battleship/moves.txt', 'r') as moves_file:
        moves = [move.strip().split(',') for move in moves_file.readlines()]

    current_player = 1
    for move in moves:
        row_idx = ord(move[0]) - ord('A')
        col_idx = int(move[1]) - 1

        if current_player == 1:
            player_map = player2_map
            opponent_map = player1_map
            player = "Player 1"
        else:
            player_map = player1_map
            opponent_map = player2_map
            player = "Player 2"

        result = process_shot(player_map, opponent_map, row_idx, col_idx)
        print(f"{player} shot: {move[0]}, {move[1]} - {result}")

        print(f"Player 1's map:")
        print_map(player1_map)

        print(f"Player 2's map:")
        print_map(player2_map)

        if all(row.count('#') == 0 for row in player1_map) or all(row.count('#') == 0 for row in player2_map):
            print("Game over!")
            break

        current_player = 3 - current_player  # Switch players (1 -> 2, 2 -> 1)

    print("Final maps:")
    print("Player 1's map:")
    print_map(player1_map)
    print("Player 2's map:")
    print_map(player2_map)

if __name__ == "__main__":
    main()
