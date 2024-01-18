import pygame as p

BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_MARGIN = 20

B_WIDTH = 600  # width of the goboard display window
B_HEIGHT = 600  # height of the goboard display window

MENU_IMAGES = []
BUTTONS = []


class Button:
    """
    Button class for the Go game:
            A class representing a clickable button.

            Methods:
                __init__(self, text, x, y, width, height, color, hover_color, action):
                    Initializes a Button instance.

                draw(self, screen, font):
                    Draws the button on the screen.

                check_click(self, event):
                    Checks if the button is clicked and performs the associated action.
    """
    def __init__(self, screen, x, y, image, action):
        """
            Initializes a Button instance.

            Args:
                image (pygame.Surface): The image of the button.
                x (int): The x-coordinate of the button.
                y (int): The y-coordinate of the button.
                action (function): The function to be executed when the button is clicked.
            """
        self.screen = screen
        self.action = action
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_clicked = False
        self.hovered = False
        self.i = 0

    def draw(self, screen):
        """
            Draws the button on the screen.

            Args:
                screen (pygame.Surface): The game screen.

            Returns:
                None
        """
        scaled_image = p.transform.scale(self.image, (BUTTON_WIDTH, BUTTON_HEIGHT))

        x_offset = (BUTTON_WIDTH - scaled_image.get_width()) // 2
        y_offset = (BUTTON_HEIGHT - scaled_image.get_height()) // 2

        screen.blit(self.image, (self.rect.x + x_offset, self.rect.y + y_offset))

    def check_click(self, event):
        """
        Checks if the button is clicked and performs
        the associated action.

        Args:
            event(pygame.event.Event): The pygame event.

        Returns:
            None
        """
        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()
                self.is_clicked = not self.is_clicked
                if self.is_clicked:
                    self.image.set_alpha(150)
                else:
                    self.image.set_alpha(255)

        if event.type == p.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                for self.i in range(4):
                    if MENU_IMAGES[self.i] == self.image:
                        self.image = MENU_IMAGES[self.i]
                        break
            else:
                for self.i in range(10):
                    if MENU_IMAGES[self.i] == self.image:
                        self.image = MENU_IMAGES[self.i]
                        if self.is_clicked:
                            self.image.set_alpha(130)
                        else:
                            self.image.set_alpha(255)
                        break


def load_images():
    """
        Load images for the game menu.

        Returns:
            None
    """
    # Menu
    global MENU_IMAGES
    ai_white = p.transform.scale(p.image.load("view/images/menu/ai_white.png"), (BUTTON_WIDTH, BUTTON_HEIGHT)) 
    ai_black = p.transform.scale(p.image.load("view/images/menu/ai_black.png"), (BUTTON_WIDTH, BUTTON_HEIGHT)) 
    play_button = p.transform.scale(p.image.load("view/images/menu/play_button.png"),
                                    (BUTTON_WIDTH, BUTTON_HEIGHT))
    quit_button = p.transform.scale(p.image.load("view/images/menu/quit_button.png"),
                                    (BUTTON_WIDTH, BUTTON_HEIGHT)) 

    MENU_IMAGES.append(ai_white)
    MENU_IMAGES.append(ai_black)
    MENU_IMAGES.append(play_button)
    MENU_IMAGES.append(quit_button)


