"""an interface for tic tac toe using a dictionary to store the coordinates"""


class DictTTTBoard:
    """a class for playing tic tac toe with coordinates"""
    def __init__(self):
        """initializes the class"""
        self._coord_dict = {
            (0, 0): ' ', (1, 0): ' ', (2, 0): ' ',
            (0, 1): ' ', (1, 1): ' ', (2, 1): ' ',
            (0, 2): ' ', (1, 2): ' ', (2, 2): ' ',
        }

    def __eq__(self, other):
        """Implements equality

        >>> DictTTTBoard == DictTTTBoard
        True
        """
        return self._coord_dict == other._coord_dict

    def __repr__(self):
        """implements the repr function

        """
        return 'DictTTTBoard({})'.format(self._coord_dict)

    def place_token(self, x, y, token):
        """sets up the place token function

        >>> a = DictTTTBoard()
        >>> a.place_token(0, 0, 'o')
        >>> a._coord_dict[(0,0)]
        'o'
        """
        self._coord_dict[(x, y)] = token

    def _calc_winner_horizontal(self):
        """checks for a winner horizontally

        >>> a = DictTTTBoard()
        >>> a.place_token(0, 0, 'o')
        >>> a.place_token(0, 1, 'o')
        >>> a.place_token(0, 2, 'o')
        >>> a._calc_winner_horizontal()
        'o'
        """
        winner = None
        tokens = ['x', 'o']
        for token in tokens:
            for row in range(0, 3):
                if(
                    self._coord_dict[(row, 0)] == token and
                    self._coord_dict[(row, 1)] == token and
                    self._coord_dict[(row, 2)] == token
                ):
                    winner = token
        return winner

    def _calc_winner_vertical(self):
        """checks the board for a winner vertically

        >>> a = DictTTTBoard()
        >>> a.place_token(0, 0, 'o')
        >>> a.place_token(1, 0, 'o')
        >>> a.place_token(2, 0, 'o')
        >>> a._calc_winner_vertical()
        'o'
        """
        winner = None
        tokens = ['x', 'o']
        for token in tokens:
            for column in range(0, 3):
                if (
                    self._coord_dict[(0, column)] == token and
                    self._coord_dict[(1, column)] == token and
                    self._coord_dict[(2, column)] == token
                ):
                    winner = token
        if winner == ' ':
            winner = None
        return winner

    def _calc_winner_diagonal(self):
        """checks the board for a diagonal winner

        >>> a = DictTTTBoard()
        >>> a.place_token(0, 0, 'o')
        >>> a.place_token(1, 1, 'o')
        >>> a.place_token(2, 2, 'o')
        >>> a._calc_winner_diagonal()
        'o'
        >>> a = DictTTTBoard()
        >>> a.place_token(2, 0, 'x')
        >>> a.place_token(1, 1, 'x')
        >>> a.place_token(0, 2, 'x')
        >>> a._calc_winner_diagonal()
        'x'
        """
        winner = None
        tokens = ['x', 'o']
        for token in tokens:
            if(
                self._coord_dict[(0, 0)] == token and
                self._coord_dict[(1, 1)] == token and
                self._coord_dict[(2, 2)] == token
            ):
                winner = token

            if(
                self._coord_dict[(2, 0)] == token and
                self._coord_dict[(1, 1)] == token and
                self._coord_dict[(0, 2)] == token
            ):
               winner = token
        return winner

    def calc_winner(self):
        """checks for a winner on the board, if nobody has won returns None

        >>> a = DictTTTBoard()
        >>> a.place_token(0, 0, 'o')
        >>> a.place_token(1, 1, 'o')
        >>> a.place_token(2, 2, 'o')
        >>> a.calc_winner()
        'o'
        >>> a = DictTTTBoard()
        >>> a.place_token(2, 0, 'x')
        >>> a.place_token(1, 1, 'x')
        >>> a.place_token(0, 2, 'x')
        >>> a.calc_winner()
        'x'
        """
        winner = None
        tokens = ['x', 'o']
        for token in tokens:
            if token == self._calc_winner_horizontal and token is not None:
                winner = token
            elif token == self._calc_winner_diagonal() and token is not None:
                winner = token
            elif token == self._calc_winner_vertical() and token is not None:
                winner = token
        return winner


    def __str__(self):
        r"""converts the dict to a string

        >>> a = DictTTTBoard()
        >>> a.place_token(0, 0, 'o')
        >>> a.place_token(1, 1, 'o')
        >>> a.place_token(2, 2, 'o')
        >>> a.__str__()
        'o| | \n |o| \n | |o'
        """
        out_string = ('\n'.join(
                     ['|'.join(
                         [self._coord_dict[(row, column)]
                          for row in range(3)])
                         for column in range(3)]
                     ))
        return out_string

