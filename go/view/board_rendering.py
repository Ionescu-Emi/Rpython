import pygame as p

B_WIDTH = 600  
B_HEIGHT = 600  
DIMENSION = 19 
LEFT_PANEL_WIDTH = 200
LEFT_PANEL_HEIGHT = B_HEIGHT

SQ_SIZE = B_HEIGHT // DIMENSION  

MAX_FPS = 60  # maximum frames per second for the display
IMAGES = {}




def draw_game_state(screen, gs):
    """
    Draw all the graphics within a current game state.

    Parameters:
    - screen (pygame.Surface): The game screen.
    - gs (GameState): The current game state.

    Returns:
    None
    """
    draw_board(screen) 

    draw_pieces(screen, gs.board)  

    draw_notation(screen)



def draw_board(screen):
    """
    Draw the goboard stones on the screen.

    Parameters:
    - screen (pygame.Surface): The game screen.

    Returns:
    None
    """
    
    color =  p.Color(185, 140, 75)


    rect = p.Rect(0, 0, B_WIDTH, B_HEIGHT)
    p.draw.rect(screen, color, rect)
    for rowline in range(0,B_WIDTH-SQ_SIZE,SQ_SIZE):
        p.draw.line(screen, (0, 0, 0), (SQ_SIZE//2+rowline, SQ_SIZE//2), (SQ_SIZE//2+rowline, B_HEIGHT-SQ_SIZE+3), 1)
    for columnline in range(0,B_HEIGHT-SQ_SIZE,SQ_SIZE):
        p.draw.line(screen, (0, 0, 0), (SQ_SIZE//2, SQ_SIZE//2+columnline), (B_WIDTH-SQ_SIZE+3, SQ_SIZE//2+columnline), 1)

    p.display.flip()


def draw_pieces(screen, board):
    """
    Draw the go pieces on the board using the current game state.

    Parameters:
    - screen (pygame.Surface): The game screen.
    - board (list): The 2D list representing the goboard.

    Returns:
    None
    """
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "-":
                # Draw the piece on the screen at the appropriate position
                if(piece == 'W'):
                    color=(255,255,255)
                else:
                    color=(0,0,0)
                p.draw.circle(screen, color, (SQ_SIZE*r+SQ_SIZE//2, SQ_SIZE*c+SQ_SIZE//2), SQ_SIZE//2, 0) 
    p.display.flip()


def draw_notation(screen):
    """
    Draw go notation on the side of the goboard.

    Parameters:
    - screen (pygame.Surface): The game screen.

    Returns:
    None
    """
    font = p.font.Font(None, 24)
    for i in range(DIMENSION):
        notation_text = font.render(str(DIMENSION - i), True, p.Color("black"))
        screen.blit(notation_text, (B_WIDTH + 6, i * SQ_SIZE + 24))  # Display row notation

    for i in range(DIMENSION):
        notation_text = font.render(chr(ord('a') + i), True, p.Color("black"))
        screen.blit(notation_text, (25 + i * SQ_SIZE + 5, B_HEIGHT + 5))  # Display column notation

    line = p.Rect(B_WIDTH, 0, 3, B_HEIGHT)
    p.draw.rect(screen, p.Color("black"), line)
    line = p.Rect(0, B_HEIGHT, B_WIDTH+3, 3)
    p.draw.rect(screen, p.Color("black"), line)





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
