from tic_tac_toe import win_combination_checker


## TODO: Move this class to the tests dir
class Test_Game_Win_Logic:
    def test_top_row_can_be_won(self):
        board = [
            "X",
            "X",
            "X",
            "O",
            "X",
            "O",
            "X",
            "O",
            "X",
        ]
        gme = win_combination_checker.WinCombinationChecker()
        assert gme.top_row_is_win(board)

    ##@pytest.mark.parametrize([])
    def test_top_row_can_be_not_won_yet(self):
        board: list[str] = []
        gme = win_combination_checker.WinCombinationChecker()
        actual = gme.top_row_is_win(board)
        expected = False
        assert expected == actual

    def test_not_implemented(self):
        assert 1 == 2
