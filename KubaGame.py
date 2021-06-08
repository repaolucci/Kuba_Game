# Author: Rebecca Paolucci
# Date: 5/30/2021
# Description: A program for the Kuba board game.

class KubaGame:
    """A class representing the Kuba Game."""

    def __init__(self, player_1_tuple, player_2_tuple):
        """
        Initializes the game board, with two players (as parameters), those player's names
        and default marble color, the current turn, the winning player (set to None), and
        each player's captured marbles.
        """
        self._player_1 = player_1_tuple
        self._player_2 = player_2_tuple
        self._player_1_name = player_1_tuple[0]
        self._player_1_color = player_1_tuple[1]
        self._player_2_name = player_2_tuple[0]
        self._player_2_color = player_2_tuple[1]
        self._current_turn = None
        self._winner = None
        self._player_1_captured = None
        self._player_2_captured = None
        self._w_count = 0
        self._b_count = 0
        self._r_count = 0
        self._board = [["W", "W", "X", "X", "X", "B", "B"],
                       ["W", "W", "X", "R", "X", "B", "B"],
                       ["X", "X", "R", "R", "R", "X", "X"],
                       ["X", "R", "R", "R", "R", "R", "X"],
                       ["X", "X", "R", "R", "R", "X", "X"],
                       ["B", "B", "X", "R", "X", "W", "W"],
                       ["B", "B", "X", "X", "X", "W", "W"]]

    def get_current_turn(self):
        """
        Returns the player name whose turn it is to play the game. Returns None
        if no player has made the first move yet.
        """
        return self._current_turn

    def make_move(self, playername, coordinates, direction):
        """
        Takes three parameters: playername, for the player who is currently making the move;
        coordinates, a tuple containing the location of the marble that is being moved; and
        direction, for the direction in which the player wants to push the marble. A
        successful move returns True. A move made under invalid conditions returns False.
        """
        pass

    def get_winner(self):
        """Returns the name of the winning player, or None if no player has won yet."""
        return self._winner

    def get_captured(self, player):
        """
        Takes a player's name as a parameter and returns the number of Red marbles
        captured by the player, or 0 if no marbles are captured.
        """
        pass

    def get_marble(self, coordinates):
        """
        Takes the coordinates of a cell as a tuple, and returns the marble at that
        location, or 'X' if no marble is present.
        """
        row_number, column_number = coordinates
        return self._board[row_number][column_number]

    def get_marble_count(self):
        """
        Returns the number of White marbles, Black marbles, and Red marbles as
        a tuple.
        """
        for row in self._board:
            for cell in row:
                if cell == "W":
                    self._w_count += 1

        for row in self._board:
            for cell in row:
                if cell == "B":
                    self._b_count += 1

        for row in self._board:
            for cell in row:
                if cell == "R":
                    self._r_count += 1
        return (self._w_count, self._b_count, self._r_count)

    def get_player_name(self):
        """Returns the name of the player."""
        pass

    def get_player_color(self):
        """Returns the player marble color."""
        pass

    def set_current_turn(self):
        """Sets self._current_turn to the other player when a valid move is made."""
        pass
