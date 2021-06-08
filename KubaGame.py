# Author: Rebecca Paolucci
# Date: 5/30/2021
# Description: A program for the Kuba board game.

import copy

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
        self._player_1_captured = 0
        self._player_2_captured = 0
        self._w_count = 8
        self._b_count = 8
        self._r_count = 13
        self._previous_board = None
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
        if self.get_current_turn() is None:
            self._current_turn = playername
        if self.get_current_turn() != playername:
            return False

        # if game has already been won
        if self.get_winner() is not None:
            return False

        row, column = coordinates
        # if coordinates are not valid
        if (row < 0) or (row > 6):
            return False
        if (column < 0) or (column > 6):
            return False

        player_marble_color = self.get_marble(coordinates)
        # if marble color does not match player color or is empty
        if player_marble_color != self.get_player_color(playername):
            return False

        # saves copy of board
        temp_board = copy.deepcopy(self._board)

        # moves Right
        if direction == "R":

            # checks for adjacent blank cell and returns False if spot to the left
            # of marble being moved is occupied
            if (column - 1) >= 0:  # when player marble is not in leftmost column
                if temp_board[row][column - 1] != "X":
                    return False

            # TODO: account for player marble in last column
            # checks if player's own marble would be pushed off
            if column == 6:  # other marble colors are already weeded out
                return False

            # slices list after marble and determines if an empty cell would
            # save a player's own marble from being pushed off
            if temp_board[row][-1] == player_marble_color:
                if "X" not in temp_board[row][(column + 1):]:
                    return False

            # TODO: shift each marble in a row to the right by one column and
            #  account for captured Red marbles or removed marbles of the
            #  other player's color
            temp_board[row][column] = "X"

            for marble in self._board[row][column + 1:]:
                if marble != "X":  # if cell is not empty
                    if (column + 1) == 6:
                        if marble == "R":
                            self.set_captured(playername)
                            self._r_count -= 1
                        if marble == "W":
                            self._w_count -= 1
                        if marble == "B":
                            self._b_count -= 1
                        temp_board[row][column + 1] = self._board[row][column]
                        print(self._board)
                        print(temp_board)
                        break
                    else:
                        temp_board[row][column + 1] = self._board[row][column]
                        column += 1
                else:
                    temp_board[row][column + 1] = self._board[row][column]
                    print(temp_board)
                    break


            # for marble in self._board[row][column + 1:]:
            #     if marble != "X":
            #         if (column + 1) == 6:
            #             if marble == "R":
            #                 self.set_captured(playername)
            #         temp_board[row][column + 2] = marble
            #         column += 1
            #         print(temp_board)
            #     if marble == "X":
            #         temp_board[row][column + 2] = marble
            #         break
            #         print(temp_board)



        # moves Left
        if direction == "L":

            # checks for adjacent blank cell
            if temp_board[row][column + 1] != "X":
                return False

            # checks if player's own marble would be pushed off
            if temp_board[row][0] == player_marble_color:
                if "X" not in temp_board[row][:column]:
                    return False

        # disallows a move that would move the board back to previous state
        if temp_board == self._previous_board:
            return False

        # sets new previous board and sets board to temporary board
        self._previous_board = copy.deepcopy(self._board)
        self._board = copy.deepcopy(temp_board)
        print(self._previous_board)
        print(self._board, "hello")

        # sets current turn to other player after a valid move
        self.set_current_turn(playername)

        # TODO: set winner if all opposing marbles are removed from the board
        if self.get_captured(playername) == 7:
            self.set_winner(playername)


        # TODO: returns True after a valid move
        return True

    def get_winner(self):
        """Returns the name of the winning player, or None if no player has won yet."""
        return self._winner

    def set_winner(self, player):
        self._winner = player

    def get_captured(self, player):
        """
        Takes a player's name as a parameter and returns the number of Red marbles
        captured by the player, or 0 if no marbles are captured.
        """
        if player == self._player_1_name:
            return self._player_1_captured

        if player == self._player_2_name:
            return self._player_2_captured

    def set_captured(self, player):
        if player == self._player_1_name:
            self._player_1_captured += 1
        if player == self._player_2_name:
            self._player_2_captured += 1


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
        # for row in self._board:
        #     for cell in row:
        #         if cell == "W":
        #             self._w_count += 1
        #
        # for row in self._board:
        #     for cell in row:
        #         if cell == "B":
        #             self._b_count += 1
        #
        # for row in self._board:
        #     for cell in row:
        #         if cell == "R":
        #             self._r_count += 1
        return (self._w_count, self._b_count, self._r_count)

    def get_player_name(self):
        """Returns the name of the player."""
        pass

    def get_player_color(self, playername):
        """Returns the player marble color."""
        if playername == self._player_1_name:
            return self._player_1_color
        if playername == self._player_2_name:
            return self._player_2_color
        pass

    def get_player(self, playername):
        if playername == self._player_1_name:
            return self._player_1
        if playername == self._player_2_name:
            return self._player_2

    def set_current_turn(self, playername):
        """Sets self._current_turn to the other player when a valid move is made."""
        if playername == self._player_1_name:
            self._current_turn = self._player_2_name
        if playername == self._player_2_name:
            self._current_turn = self._player_1_name


# game = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))
# game.get_marble_count()
# print(game.get_marble_count()) #returns (8,8,13)
#
# print(game.get_captured('PlayerA')) #returns 0
# game.get_winner() #returns None
# #print(game.make_move('PlayerA', (0, 0), 'R'))
# print(game.make_move('PlayerA', (6,5), 'R'))
# print(game.make_move('PlayerA', (6,5), 'F'))
# game.make_move('PlayerA', (6,5), 'L') #Cannot make this move
# game.get_marble((5,5)) #returns 'W'
# print(game.get_marble_count())
# print(game.get_current_turn())