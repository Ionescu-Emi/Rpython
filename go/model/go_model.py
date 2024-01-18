from .game_state_class import GameState


class goModel:
    """
    Represents the model of the go game, managing game state and player interactions.

    Attributes:
        - valid_moves (list): List of valid moves for the current game state.
        - game_situation (str): Represents the current situation of the game (e.g., "menu", "playing").
        - game_over (bool): True if the game is over, False otherwise.
        - move_made (bool): Flag variable indicating whether a move has been made.
        - running (bool): True if the game is running, False otherwise.
        - game_state (GameState): An instance of the GameState class representing the current state of the game.
        - white_player (bool): False if AI, True if white player is human.
        - black_player (bool): False if AI, True if black player is human.

    Methods:
        - update(move): Update the game state after a move is made.

    """

    def __init__(self):
        """
           Initializes the goModel with default attributes and an instance of the GameState class.
        """
        self.valid_moves = []  

        self.game_situation = "menu"

        self.game_over = False
        self.move_made = False  

        self.running = True

        self.game_state = GameState()
        self.valid_moves = self.game_state.get_valid_moves()

        self.white_player = False
        self.black_player = False

    def update(self, move):
        """
            Update the game state after a move is made.
            Args:
                move (Move): The move to be made.
        """
        self.game_state.make_move(move)
        self.move_made = True
