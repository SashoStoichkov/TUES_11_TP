class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourMove(Exception):
    pass


class GameOver(Exception):
    pass


class TicTacToeBoard():
    def __init__(self):
        self.__board = {
            "A1": " ", "A2": " ", "A3": " ",
            "B1": " ", "B2": " ", "B3": " ",
            "C1": " ", "C2": " ", "C3": " "
        }
        self.__last_move = " "
        self.__all_winning_combinations = [
            ("A1", "A2", "A3"), ("B1", "B2", "B3"), ("C1", "C2", "C3"),
            ("A1", "B1", "C1"), ("A2", "B2", "C2"), ("A3", "B3", "C3"),
            ("A1", "B2", "C3"), ("C1", "B2", "A3")
        ]

    def __setitem__(self, key, value):
        self.__possible_keys = [
            "A1", "A2", "A3",
            "B1", "B2", "B3",
            "C1", "C2", "C3"
        ]
        self.__possible_values = ["X", "O"]

        if self.game_status() != "Game in progress.":
            exc_msg = "Game over! " + self.game_status()
            raise GameOver(exc_msg)

        elif key not in self.__possible_keys:
            exc_msg = "You think 'out of the box' ... that is good" +\
                      " but not in this game :)"
            raise InvalidKey(exc_msg)

        elif self.__board[key] != " ":
            exc_msg = "You want to make your game easier but that space" +\
                      " is already captured by your opponent." +\
                      " Please try with another one :)"
            raise InvalidMove(exc_msg)

        elif value not in self.__possible_values:
            exc_msg = "You probably haven't played Tic Tac Toe before." +\
                      " That's OK! Let me explain the rules of the game." +\
                      " You have to place ether 'X' or 'O' :)"
            raise InvalidValue(exc_msg)

        elif self.__last_move == value:
            exc_msg = "I understand that you are in hurry but let your" +\
                      " fellow opponent make their move first than" +\
                      " you are free to make your move :)"
            raise NotYourMove(exc_msg)

        else:
            self.__board[key] = value
            self.__last_move = value

    def __str__(self):
        A1, A2, A3 = self.__board["A1"], self.__board["A2"], self.__board["A3"]
        B1, B2, B3 = self.__board["B1"], self.__board["B2"], self.__board["B3"]
        C1, C2, C3 = self.__board["C1"], self.__board["C2"], self.__board["C3"]

        line1 = {"A1": A1, "B1": B1, "C1": C1}
        line2 = {"A2": A2, "B2": B2, "C2": C2}
        line3 = {"A3": A3, "B3": B3, "C3": C3}

        board = "\n  -------------\n" +\
                "3 | {A3} | {B3} | {C3} |\n".format(**line3) +\
                "  -------------\n" +\
                "2 | {A2} | {B2} | {C2} |\n".format(**line2) +\
                "  -------------\n" +\
                "1 | {A1} | {B1} | {C1} |\n".format(**line1) +\
                "  -------------\n" +\
                "    A   B   C  \n"

        return board

    def game_status(self):
        for combination in self.__all_winning_combinations:
            if all(self.__board[key] == "X" for key in combination):
                return "X wins!"
            elif all(self.__board[key] == "O" for key in combination):
                return "O wins!"

        if " " not in self.__board.values():
            return "Draw!"
        else:
            return "Game in progress."
