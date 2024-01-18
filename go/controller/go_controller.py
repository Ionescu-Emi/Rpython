from model import go_model as model
from view import go_view as view
from model.game_state_class import GameState
from view import menu_buttons_view as menu
import pygame as p
import sys


class goController:
    """
        Controller class for the go game, handling user input and managing the game flow.

        Attributes:
        - go_model (goModel): An instance of the go model.
        - go_view (goView): An instance of the go view.

        Methods:
        - handle_input(screen, event): Handles user input during the game.
        - handle_menu_input(event): Handles user input in the game menu.
        - game_initialization(white_player, black_player, game_situation, running): Initializes the game parameters.
        - end_game(screen): Displays the end game message based on the game state.
    """
    def __init__(self):
        """
        Initializes the goController by creating instances of goModel and goView.
        """
        self.go_model = model.goModel()
        self.go_model.valid_moves = self.go_model.game_state.get_valid_moves()
        self.go_view = view.goView()

    def handle_input(self, screen, event):
        """
        Handles user input during the go game.

        Args:
            - screen: The Pygame screen surface.
            - event: The Pygame event to be handled.
        """
        # model part
        human_turn = (self.go_model.game_state.black_to_move and not self.go_model.white_player) or (
                    not self.go_model.game_state.black_to_move and not self.go_model.black_player)
        # Quit 
        if event.type == p.QUIT:
            self.go_model.running = False
        

        # Mouse event handlers
        elif event.type == p.MOUSEBUTTONDOWN:
            if not self.go_model.game_over and human_turn:
                location = p.mouse.get_pos()
                col = location[0] // view.SQ_SIZE
                row = location[1] // view.SQ_SIZE
                if row < view.DIMENSION and col < view.DIMENSION:
                    if (col,row) in self.go_model.valid_moves:
                        self.go_model.game_state.make_move((col,row))
                        self.go_model.move_made = True

                    




        elif event.type == p.KEYDOWN:
            if event.key == p.K_q:
                self.go_model.running = False
                self.go_model.game_over = True
                sys.exit()
            elif event.key==p.K_SPACE:
                self.go_model.game_state.make_move("PAS")
                self.go_model.move_made = True



                # AI move
        if not self.go_model.game_over and not human_turn:
            move = self.go_model.game_state.random_move(self.go_model.valid_moves)
            self.go_model.game_state.make_move(move)
            self.go_model.move_made = True
                    # view part
        if self.go_model.move_made:
            self.go_model.valid_moves = self.go_model.game_state.get_valid_moves()
            self.go_model.move_made = False
        if len(list(set(self.go_model.game_state.move_log[-2:])))==1 and list(set(self.go_model.game_state.move_log[-2:]))[0]=="PAS":
            self.end_game(screen)


    def handle_menu_input(self, event):
        """
        Handles user input in the go game menu.

        Args:
            - event: The Pygame event to be handled.
        """

        # Quit the game
        if event.type == p.QUIT:
            self.go_view.game_situation = "quit"
            sys.exit()

        for button in menu.BUTTONS:
            button.check_click(event)

    def game_initialization(self, white_player, black_player, game_situation, running):
        """
        Initializes the game parameters, sending the settings selected in the menu interface.

        Args:
            - white_player (bool): True if the white player is human, False if AI.
            -  black_player (bool): True if the black player is human, False if AI.
            - game_situation (str): The initial game situation.
            - running (bool): True if the game is running, False otherwise.
        """
        self.go_model.white_player = white_player
        self.go_model.black_player = black_player
        self.go_model.game_situation = game_situation
        self.go_model.running = running
        self.go_view.game_initialization()

    def end_game(self, screen):
        """
        Displays the end game message based on the game state.

        Args:
            - screen: The Pygame screen surface.
        """
        self.go_model.game_over = True
        if(self.go_model.game_state.BlackCaptured<self.go_model.game_state.WhiteCaptured):
            view.draw_end_game(screen, "Black won")
        else:
            view.draw_end_game(screen,"White won")
            
        return