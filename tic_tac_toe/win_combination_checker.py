class WinCombinationChecker:
    # TODO: Reduce duplication in this class. Can probably reduce to one reusable func taking in a board and 3 indices

    def game_is_won(self, board: list[str]):
        return (
            self.top_row_is_win(board)
            or self.middle_row_is_win(board)
            or self.bottom_row_is_win(board)
            or self.left_col_is_win(board)
            or self.middle_col_is_win(board)
            or self.right_col_is_win(board)
            or self.left_up_diagonal_is_win(board)
            or self.right_down_diagonal_is_win(board)
        )

    def top_row_is_win(self, board: list[str]):
        if (
            board is not None
            and len(board) > 0
            and board[0] is not None
            and board[0] in ["O", "X"]
        ):
            return board[0] == board[1] == board[2]
        return False

    def middle_row_is_win(self, board: list[str]):
        if (
            board is not None
            and len(board) > 0
            and board[3] is not None
            and board[3] in ["O", "X"]
        ):
            return board[3] == board[4] == board[5]
        return False

    def bottom_row_is_win(self, board: list[str]):
        if (
            board is not None
            and len(board) > 0
            and board[6] is not None
            and board[6] in ["O", "X"]
        ):
            return board[6] == board[7] == board[8]
        return False

    def left_col_is_win(self, board: list[str]):
        if (
            board is not None
            and len(board) > 0
            and board[0] is not None
            and board[0] in ["O", "X"]
        ):
            return board[0] == board[3] == board[6]
        return False

    def middle_col_is_win(self, board: list[str]):
        if (
            board is not None
            and len(board) > 0
            and board[1] is not None
            and board[1] in ["O", "X"]
        ):
            return board[1] == board[3] == board[6]
        return False

    def right_col_is_win(self, board: list[str]):
        if (
            board is not None
            and len(board) > 0
            and board[2] is not None
            and board[2] in ["O", "X"]
        ):
            return board[2] == board[5] == board[8]
        return False

    def left_up_diagonal_is_win(self, board: list[str]):
        if (
            board is not None
            and len(board) > 0
            and board[2] is not None
            and board[2] in ["O", "X"]
        ):
            return board[2] == board[4] == board[6]
        return False

    def right_down_diagonal_is_win(self, board: list[str]):
        if (
            board is not None
            and len(board) > 0
            and board[2] is not None
            and board[2] in ["O", "X"]
        ):
            return board[0] == board[4] == board[8]
        return False


##012
##345
##678
