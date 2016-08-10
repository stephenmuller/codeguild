"""Stores a tic tac toe board as a list of lists"""


class ListTTTBoard:
    """List class """
    def __init__(self):
        self._rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def __eq__(self, other):
        return (self._rows == other._rows)

    def __repr__(self):
        return 'ListTTTBoard({!r})'.format(self._rows)

    def place_token(self, x, y, token):
        """places a token on the list structure

        >>> a = ListTTTBoard()
        >>> a.place_token(0, 0, 'x')
        >>> a
        ListTTTBoard([['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

        >>> a = ListTTTBoard()
        >>> a.place_token(0, 1, 'x')
        >>> a
        ListTTTBoard([[' ', ' ', ' '], ['x', ' ', ' '], [' ', ' ', ' ']])
        """
        self._rows[y] [x] = token

    def _calc_winner_horizontally(self):
        """Checks the board for a horizontal winner, returns None if there is no winner

        >>> a = ListTTTBoard()
        >>> a._rows = [['x', 'x', 'x'], [' ', ' ', ' '], [' ', ' ', ' ']]
        >>> a._calc_winner_horizontally()
        'x'
        """
        winner = None
        for row in self._rows:
            token_to_check = row[0]
            if (token_to_check == row[1] and
                token_to_check == row[2] and
                token_to_check != ' '
            ):
                winner = token_to_check
        # if winner == ' ':
        #     winner = None
        return winner

    def _calc_winner_vertically(self):
        """Checks the board for a vertical winner, returns None if there is no winner

        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', ' ', 'x'], [' ', ' ', 'x'], [' ', ' ', 'x']]
        >>> a._calc_winner_vertically()
        'x'
        """
        winner = None
        tokens = ['x', 'o']
        for i in range(0, 3):
            for token in tokens:
                if(token == self._rows[0][i] and
                    token == self._rows[1][i] and
                    token == self._rows[2][i]
                ):
                    winner = token
        return winner

    def _calc_winner_diagonally(self):
        """Checks the board for a winner diagonally

        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', ' ', 'x'], [' ', 'x', ' '], ['x', ' ', ' ']]
        >>> a._calc_winner_diagonally()
        'x'

        >>> a = ListTTTBoard()
        >>> a._rows = [['x', ' ', 'x'], [' ', 'x', ' '], [' ', ' ', 'x']]
        >>> a._calc_winner_diagonally()
        'x'

        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', ' ', 'o'], [' ', 'o', ' '], ['o', ' ', ' ']]
        >>> a._calc_winner_diagonally()
        'o'
        """
        winner = None
        tokens = ['x', 'o']
        for token in tokens:
            if(
                token == self._rows[0][0] and
                token == self._rows[1][1] and
                token == self._rows[2][2]
            ):
                winner = token
            elif(
                token == self._rows[0][2] and
                token == self._rows[1][1] and
                token == self._rows[2][0]
            ):
                winner = token
        return winner

    def calc_winner(self):
        """runs a board against the three functions and outputs a winner or None

        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', ' ', 'o'], [' ', 'o', ' '], ['o', ' ', ' ']]
        >>> a.calc_winner()
        'o'
        """
        winner = None
        tokens = ['x', 'o']
        for token in tokens:
            if token == self._calc_winner_horizontally and token is not None:
                winner = token
            elif token == self._calc_winner_diagonally() and token is not None:
                winner = token
            elif token == self._calc_winner_vertically() and token is not None:
                winner = token
        return winner

    def __str__(self):
        r"""outputs a str version of the class

        >>> a = ListTTTBoard()
        >>> a._rows = [[' ', ' ', 'o'], [' ', 'o', ' '], ['o', ' ', ' ']]
        >>> a.__str__()
        ' | |o\n |o| \no| | '
        """
        temp = ['|'.join(row) for row in self._rows]
        output = '\n'.join(temp)
        return output
