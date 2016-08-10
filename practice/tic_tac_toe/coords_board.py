"""Board Class for Tic Tac Toe"""

class CoordsTTTBoard:
    def __init__(self):
        self.coords_dict = []

    def __eq__(self, other):
        """sets EQ

        >>> CoordsTTTBoard() == CoordsTTTBoard()
        True
        """
        return self.coords_dict == other.coords_dict

    def __repr__(self):
        """implements repr

        >>> CoordsTTTBoard()
        CoordsTTTBoard([])
        """
        return 'CoordsTTTBoard({!r})'.format(self.coords_dict)


    def place_token(self, x, y, token):
        """Saves a token to coordinates for later placement the board

        >>> a = CoordsTTTBoard()
        >>> a.place_token(0, 0, 'X')
        >>> a.coords_dict
        [(0, 0, 'X')]

        >>> a = CoordsTTTBoard()
        >>> a.place_token(0, 0, 'X')
        >>> a.place_token(0, 1, 'X')
        >>> a.coords_dict
        [(0, 0, 'X'), (0, 1, 'X')]
        """
        self.coords_dict.append((x, y, token))

    def _calc_winner_horizontally(self):
        """checks for 3 in a row

        >>> a = CoordsTTTBoard()
        >>> a.place_token(0, 0, 'X')
        >>> a.place_token(1, 0, 'X')
        >>> a.place_token(2, 0, 'X')
        >>> a._calc_winner_horizontally()
        'X'
        """
        tokens = ['X', 'O']
        winner = None
        for token in tokens:
            if(
                (0, 0, token) in self.coords_dict and
                (1, 0, token) in self.coords_dict and
                (2, 0, token) in self.coords_dict
            ):
                winner = token
            elif(
                (0, 1, token) in self.coords_dict and
                (1, 1, token) in self.coords_dict and
                (2, 1, token) in self.coords_dict
            ):
                winner = token
            elif (
                (0, 1, token) in self.coords_dict and
                (1, 1, token) in self.coords_dict and
                (2, 1, token) in self.coords_dict
            ):
                winner = token
        return winner

    def _calc_winner_vertically(self):
        """checks for 3 in a row

        >>> a = CoordsTTTBoard()
        >>> a.place_token(0, 0, 'X')
        >>> a.place_token(0, 1, 'X')
        >>> a.place_token(0, 2, 'X')
        >>> a._calc_winner_vertically()
        'X'
        """
        tokens = ['X', 'O']
        winner = None
        for token in tokens:
            if (
                (0, 0, token) in self.coords_dict and
                (0, 1, token) in self.coords_dict and
                (0, 2, token) in self.coords_dict
            ):
                winner = token
            elif (
                (1, 0, token) in self.coords_dict and
                (1, 1, token) in self.coords_dict and
                (1, 2, token) in self.coords_dict
            ):
                winner = token
            elif (
                (2, 0, token) in self.coords_dict and
                (2, 1, token) in self.coords_dict and
                (2, 2, token) in self.coords_dict
            ):
                winner = token
        return winner

    def _calc_winnner_diagonally(self):
        """checks for a diagonal winner

        >>> a = CoordsTTTBoard()
        >>> a.place_token(0, 0, 'X')
        >>> a.place_token(1, 1, 'X')
        >>> a.place_token(2, 2, 'X')
        >>> a._calc_winnner_diagonally()
        'X'
        """
        tokens = ['X', 'O']
        winner = None
        for token in tokens:
            if (
                (0, 0, token) in self.coords_dict and
                (1, 1, token) in self.coords_dict and
                (2, 2, token) in self.coords_dict
            ):
                winner = token
            elif (
                 (0, 2, token) in self.coords_dict and
                 (1, 1, token) in self.coords_dict and
                 (2, 0, token) in self.coords_dict
            ):
                winner = token
        return winner

    def calc_winner(self):
        """checks who won"""
        winner = None
        tokens = ['x', 'o']
        for token in tokens:
            if token == self._calc_winner_horizontally() and token is not None:
                winner = token
            elif token == self._calc_winner_diagonally() and token is not None:
                winner = token
            elif token == self._calc_winner_vertically() and token is not None:
                winner = token
        return winner
