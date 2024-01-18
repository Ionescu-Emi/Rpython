"""
Main Module for go Game



Data: 18/01/2024
Autor: Ionescu Emi-Marian
"""
from view import go_view as view
from controller import go_controller as controller
import pygame as p


def main():
    """
        Main function to run the go game.

        This function initializes the goView and goController, manages the menu loop, and controls the game loop.

        Returns:
            None
        """

    # Initialize goView and goController
    go_view = view.goView()
    go_controller = controller.goController()

    # menu loop
    while go_controller.go_view.game_situation == "menu":
        for event in p.event.get():
            go_controller.handle_menu_input(event)

        go_view.draw(go_controller.go_model.game_state, go_controller.go_model.game_situation)

        p.display.flip()
        go_view.clock.tick(view.MAX_FPS)

    # game initialization - # Initialize the game based on menu choices
    go_controller.game_initialization(go_controller.go_view.white_player,
                                         go_controller.go_view.black_player,
                                         go_controller.go_view.game_situation,
                                         go_controller.go_view.running)
    # game loop
    while go_controller.go_model.running and go_controller.go_model.game_situation == "game":
        for event in p.event.get():
            go_controller.handle_input(go_view.screen, event)

        go_view.draw(go_controller.go_model.game_state)

        if go_controller.go_model.game_over:
            go_controller.end_game(go_view.screen)

        p.display.flip()
        go_view.clock.tick(view.MAX_FPS)


if __name__ == "__main__":
    main()
