import pygame as p

from .board_rendering import *
from controller import go_controller as controller
from view import menu_buttons_view as menu

B_WIDTH = 600  # width of the goboard display window
B_HEIGHT = 600  # height of the goboard display window
DIMENSION = 19  # size of the goboard (19x19)
LEFT_PANEL_WIDTH = 200

SQ_SIZE = B_HEIGHT // DIMENSION  # distance between intersections on the goboard

MAX_FPS = 60  # maximum frames per second for the display

FONT_SIZE = 32


class goView:
    """
    Class representing the view for the go game.

    Attributes:
        - screen (pygame.Surface): The game screen.
        - clock (pygame.time.Clock): The game clock.
        - game_situation (str): The current situation of the game (e.g., "menu" or "game").
        - white_player (bool): Flag is on if white player is controlled by AI.
        - black_player (bool): Flag is on if black player is controlled by AI.
        - running (bool): Flag indicating whether the game is currently running.

    Methods:
        - __init__(self): Initializes the goView object.
        - draw(self, game_state, game_situation="game"): Draws the game state.
        - create_buttons(self, screen): Creates buttons for the menu.
        - draw_menu(self): Draws the menu screen.
        - start_game(self): Initiates the go game.
        - set_ai_white(self): Toggles AI control for the white player.
        - set_ai_black(self): Toggles AI control for the black player.
        - quit_game(self): Quits the game.
        - draw_board(self, game_state): Draws the goboard.
        - game_initialization(self): Initializes the game.

    """
    def __init__(self):
        """
        Initialize the goView object.
        This method initializes the game screen, clock, and other attributes for the goView.
        Parameters:
            self (goView): The goView object to be initialized.
        Returns:
            None
        """
        p.init()
        self.boardDrawn=False
        self.screen = p.display.set_mode((B_WIDTH, B_HEIGHT))
        self.screen.fill(p.Color("white"))
        p.display.set_caption("go")
        self.clock = p.time.Clock()

        menu.load_images()
        self.game_situation = "menu"
        self.white_player = False
        self.black_player = False
        self.running = True

        self.create_buttons(self.screen)

    def draw(self, game_state, game_situation="game"):
        """
            Draw the game state on the screen.

            Parameters:
                - game_state: The current state of the go game.
                - game_situation (str): The current situation of the game.

            Returns:
                None
        """
        if game_situation == "menu":
            self.draw_menu()
        elif game_situation == "game":
            self.draw_board(game_state)

    def create_buttons(self, screen):
        """
            Create buttons for the menu.

            Parameters:
                - screen (pygame.Surface): The game screen.

            Returns:
                None
        """
        player_one_button = menu.Button(screen, B_WIDTH // 2 - menu.BUTTON_WIDTH // 2,
                                        B_HEIGHT // 2 - 35 - menu.BUTTON_HEIGHT - menu.BUTTON_MARGIN,
                                        menu.MENU_IMAGES[0], self.set_ai_white)
        player_two_button = menu.Button(screen, B_WIDTH // 2 - menu.BUTTON_WIDTH // 2, B_HEIGHT // 2 - 35,
                                        menu.MENU_IMAGES[1], self.set_ai_black)
        play_button = menu.Button(screen, B_WIDTH // 2 - menu.BUTTON_WIDTH // 2,
                                  B_HEIGHT // 2 - 35 + menu.BUTTON_HEIGHT + menu.BUTTON_MARGIN,
                                  menu.MENU_IMAGES[2], self.start_game)
        quit_button = menu.Button(screen, B_WIDTH // 2 - menu.BUTTON_WIDTH // 2,
                                  B_HEIGHT // 2 + 3 * (menu.BUTTON_HEIGHT + menu.BUTTON_MARGIN),
                                  menu.MENU_IMAGES[3], self.quit_game)

        menu.BUTTONS = [player_one_button, player_two_button, play_button, quit_button]

    def draw_menu(self):
        """
            Draw the menu screen.

            Parameters:
                None

            Returns:
                None
        """
        self.screen.blit(menu.MENU_IMAGES[4], (0, 0))
        for button in menu.BUTTONS:
            button.draw(self.screen)

    def start_game(self):
        """
            Start the go game.

            Parameters:
                None

            Returns:
                None
        """
        self.game_situation = "game"

        print("start game")

    def set_ai_white(self):
        """
            Toggle AI control for the white player.

            Parameters:
                None

            Returns:
                None
        """
        self.white_player = not self.white_player
        print("set ai white")

    def set_ai_black(self):
        """
            Toggle AI control for the black player.

            Parameters:
                None

            Returns:
                None
        """
        self.black_player = not self.black_player
        print("set ai black")

    def quit_game(self):
        """
            Quit the game.

            Parameters:
                None

            Returns:
                None
        """
        self.running = False
        self.game_situation = "game"
        print("quit game")

    def draw_board(self, game_state):
        """
        Draw the goboard on the screen.

        Parameters:
            - game_state (goGameState): The current state of the go game.

        Returns:
            None
        """
        if(self.boardDrawn and not game_state.Captured):
            draw_pieces(self.screen, game_state.board)  # draw pieces on top
            draw_notation(self.screen)
        else:
            draw_game_state(self.screen, game_state)
            self.boardDrawn=True
            game_state.Captured=False


    def game_initialization(self):
        """
            Initialize the game screen to the proper dimensions.

            Parameters:
                None

            Returns:
                None
        """
        self.screen = p.display.set_mode((B_WIDTH + LEFT_PANEL_WIDTH, B_HEIGHT + 25))
        self.screen.fill(p.Color("white"))


def draw_end_game(screen, text):
    """
    Draw the end game screen with the specified text.

    Parameters:
    - screen (pygame.Surface): The game screen.
    - text (str): The text to be displayed on the end game screen.

    Returns:
    None
    """
    font = p.font.Font(None, 32)
    text_object = font.render(text, 0, p.Color('Gray'))
    text_location = p.Rect(0, 0, B_WIDTH, B_HEIGHT).move(B_WIDTH / 2 - text_object.get_width() / 2,
                                                         B_HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)
    text_object = font.render(text, 0, p.Color('Black'))
    screen.blit(text_object, text_location.move(2, 2))
