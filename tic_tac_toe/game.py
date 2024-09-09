import random as rand
import win_combination_checker


class Game:
    """The entire game of noughts and crosses/tic tac toe as a class"""

    def __init__(self):
        print("Hello noughts and crosses!")
        self.nought = "O"
        self.cross = "X"
        self.available_pieces: list[str] = [self.nought, self.cross]
        self.count_available_pieces = len(self.available_pieces)
        self.count_players: int = 2
        self.count_cells: int = 9
        default_cell_value = " "
        self.win_combination_checker = win_combination_checker.WinCombinationChecker()
        self.board_pieces: list[str] = [
            default_cell_value,
            default_cell_value,
            default_cell_value,
            default_cell_value,
            default_cell_value,
            default_cell_value,
            default_cell_value,
            default_cell_value,
            default_cell_value,
        ]

    def get_pieces_as_triplet(self) -> list[list[str]]:
        return [
            [
                self.board_pieces[0],
                self.board_pieces[1],
                self.board_pieces[2],
            ],
            [
                self.board_pieces[3],
                self.board_pieces[4],
                self.board_pieces[5],
            ],
            [
                self.board_pieces[6],
                self.board_pieces[7],
                self.board_pieces[8],
            ],
        ]

    def get_random_int(self, upper_bound_exclusive: int) -> int:
        return int(rand.random() * 100) % upper_bound_exclusive

    def get_index_of_next_empty_cell(self):
        for i in range(self.count_cells):
            if self.board_pieces[i].isspace() or self.board_pieces[i] is None:
                return i
        return -1

    def get_all_empty_cell_indices(self) -> list[int]:
        empty_cell_indices = []
        for i in range(self.count_cells):
            if self.board_pieces[i].isspace() or self.board_pieces[i] is None:
                empty_cell_indices.append(i)
        return empty_cell_indices

    def get_index_of_rand_empty_cell(self):
        empty_indices = self.get_all_empty_cell_indices()
        random = self.get_random_int(len(empty_indices))
        return empty_indices[random]

    def announce_round(self, round_index: int) -> None:
        print("~~ Round ", round_index, ": begin! ~~")

    def announce_player_turn(self, player: int) -> None:
        print("__Player ", player, "'s turn!")

    def print_board(self):
        for i in range(3):
            self.print_row_outline()
            self.print_row(self.get_pieces_as_triplet()[i])
        self.print_row_outline()

    def print_row(self, pieces_in_row: list[str]):
        print(
            "|",
            pieces_in_row[0],
            "|",
            pieces_in_row[1],
            "|",
            pieces_in_row[2],
            "|",
        )

    def print_row_outline(self):
        print("+", "-", "+", "-", "+", "-", "+", end="\n")

    def game_is_won(self):
        return self.win_combination_checker.game_is_won(board=self.board_pieces)

    def announce_winner(self):
        print("announcing winner")
        raise NotImplementedError()

    def restart_game(self):
        print("restarting game")
        raise NotImplementedError()

    def play_game_auto(self, should_print_board_after_round: bool = False):
        for i in range(9):
            self.announce_round(i)
            player_index = self.get_player_index_by_round_index(i)
            friendly_player_index = player_index + 1
            self.announce_player_turn(friendly_player_index)
            random_board_piece_val = self.available_pieces[player_index]
            print("__Use piece: ", random_board_piece_val, " !")
            rand_index: int = self.get_index_of_rand_empty_cell()
            self.board_pieces[rand_index] = random_board_piece_val
            print("rand_index is: ", rand_index)
            print("__Chose a cell!")
            if should_print_board_after_round:
                self.print_board()
            if self.game_is_won():
                self.announce_winner()
                self.restart_game()

    def get_player_index_by_round_index(self, i):
        return i % 2
