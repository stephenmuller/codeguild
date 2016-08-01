"""Account Module"""


class Account:
    """A class for storing account details for an ATM"""
    def __init__(self):
        self._balance = 0.0
        self._int_rate = .001
        self.user_id = ''
        self.od_fee = 50
        self.account_type = ''

    def __eq__(self, other):
        return (
            self.get_funds() == other.get_funds() and
            self._int_rate == other.int_rate and
            self.user_id == other.user_id and
            self.od_fee == other.od_fee and
            self.account_type == other.account_type
        )

    def __repr__(self):
        return 'Account({!r}, {!r}, {!r}, {!r}, {!r}'.format(
            self._balance,
            self._int_rate,
            self.user_id,
            self.od_fee,
            self.account_type
        )

    def get_funds(self):
        """get funds

        >>> a = Account()
        >>> a.get_funds()
        0.0
        """
        return self._balance

    def deposit(self, amount):
        """deposit

        >>> a = Account()
        >>> a.deposit(49)
        >>> a._balance
        49.0
        """
        self._balance += amount


    def check_withdrawal(self, amount):
        """check withdrawal

        >>> a = Account()
        >>> a.check_withdrawal(1)
        False
        """
        return self._balance >= amount

    def calc_interest(self):
        """calc interest

        >>> a = Account()
        >>> a.deposit(200)
        >>> a.calc_interest()
        0.2
        """
        return self._balance * self._int_rate

    def withdraw(self, amount):
        """withdraw

        >>> a = Account()
        >>> a.deposit(50)
        >>> a.withdraw(10)
        >>> a.get_funds()
        40.0

        >>> a = Account()
        >>> a.withdraw(10)
        Traceback (most recent call last):
        ...
        ValueError
        """
        self._balance -= amount
        if self._balance < 0.0:
            raise ValueError('not enough money')
