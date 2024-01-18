
from collections import deque
import copy as c
import random



class GameState:
    """)
    Represents the state of a go game, including the current board configuration, player turns, liberties on the board.
    Attributes:
        - board (list): A 2D matrix representing the go board configuration.
        - black_to_move (bool): True if black's turn, False otherwise
        - move_log (list): A list to store past moves.
        - IntersectionAdjacents (dictionary) : Given a position on the board given as a tuple it returns (number of adjacent white stone,number of adjacent black stone) 
        - BlackCaptured (int) : Number of black stones captured
        - WhiteCaptured (int) : Number of white stones captured
        - GroupLiberties (dictionary) : For every stone grouping it keeps count of all it's liberties(empty intersections adjacent with the stone group)
        - CapturedList (list) : A list that keeps track of captured stones
        - Captured (bool) : Boolean that keeps track of when a stone is captured so that the board view is refreshed.


    Methods:
        - make_move(move): Executes the given go move on the board, updating the game state.
        - get_valid_moves(): Generates all possible correct moves.
        - random_move(valid_moves): Generates a random move from the list of valid moves.

    """
    def __init__(self):
        """
            Initialize the game state.
        """
        self.board = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        ]


        self.black_to_move = True
        self.move_log = []
        self.IntersectionAdjacents={}
        self.GroupLiberties={} # dictionary that has as key stone groups and value as liberties. Problems dictionary key must be hashable . I need a function that converts from hashable unique id for groups to groups as a list
        self.BlackCaptured=0
        self.WhiteCaptured=0
        self.CapturedList=[]
        self.Captured=False
    def CapturedStones(self,move):
        l=[]
        for group in self.GroupLiberties.keys():
            if len(self.GroupLiberties[group])==1 and self.GroupLiberties[group][0]==move and ((self.black_to_move and self.board[list(group)[0][0]][list(group)[0][1]]=='W') or ((not self.black_to_move) and self.board[list(group)[0][0]][list(group)[0][1]]=='B')) :
                for pos in group:
                    l+=[pos]
        return l


    def UpdateGroupLiberties(self,move):
        adjacents=[(0,-1),(1,0),(0,1),(-1,0)]
        for group,liberties in self.GroupLiberties.items():
            while move in liberties:
                self.GroupLiberties[group].remove(move)
        
        self.GroupLiberties[frozenset([move])]=[]
        adjacents=[(0,-1),(1,0),(0,1),(-1,0)]
        for nghbrs in adjacents:
            if (0<=nghbrs[0]+move[0]<len(self.board) and 0<=nghbrs[1]+move[1]<len(self.board)) and self.board[nghbrs[0]+move[0]][nghbrs[1]+move[1]]=='-':
                self.GroupLiberties[frozenset([move])]+=[(nghbrs[0]+move[0],nghbrs[1]+move[1])]
        adjacents+=[(0,0)]

        combinedGroups=frozenset([])
        combinedLiberties=[]
        for nghbrs in adjacents:
            for group in list(self.GroupLiberties.keys()):
                if  0 <=nghbrs[0]+move[0]<len(self.board) and 0 <=nghbrs[1]+move[1]<len(self.board) and self.board[move[0]][move[1]]==self.board[move[0]+nghbrs[0]][move[1]+nghbrs[1]] and ((nghbrs[0]+move[0],nghbrs[1]+move[1]) in group): # check if colours match when combining groups
                    combinedGroups=combinedGroups.union(group)

                    combinedLiberties+=self.GroupLiberties[group]

                    del self.GroupLiberties[group]

        self.GroupLiberties[combinedGroups]=combinedLiberties

        adjacents=adjacents[:4]
        for group in list(self.GroupLiberties.keys()):
            if(len(self.GroupLiberties[group])==0):
                for piece in group:
                    if(self.board[piece[0]][piece[1]]=="B"):
                        self.BlackCaptured+=1
                    else:
                        self.WhiteCaptured+=1
                    self.board[piece[0]][piece[1]]="-"
                    for group in list(self.GroupLiberties.keys()):
                        for nghbrs in adjacents:
                            (a,b)=(nghbrs[0]+piece[0],nghbrs[1]+piece[1])
                            npiece=(a,b)
                            if 0 <=npiece[0]<len(self.board) and 0 <=npiece[1]<len(self.board) and npiece in group:
                                self.GroupLiberties[group]+=[piece]

                    self.CapturedList+=[piece]
                    self.Captured=True
        









    def is_valid_move(self,move):
        adjacents=[(0,-1),(1,0),(0,1),(-1,0)]
        number=0
        if move=='PAS':
            return True
        elif type(move)==str:
            return False
        if self.black_to_move:
          
            for nghbrs in adjacents:
                if (0<=nghbrs[0]+move[0]<len(self.board) and 0<=nghbrs[1]+move[1]<len(self.board)) and self.board[nghbrs[0]+move[0]][nghbrs[1]+move[1]]=='W':
                    number+=1
                
            
        else:
            for nghbrs in adjacents:
                if (0<=nghbrs[0]+move[0]<len(self.board) and 0<=nghbrs[1]+move[1]<len(self.board)) and self.board[nghbrs[0]+move[0]][nghbrs[1]+move[1]]=='B':
                    number+=1
        captured=self.CapturedStones(move)
        if(number<4):
            if(len(captured)==0):
                return True
            else:
                if(len(self.CapturedList)>=2):
                    lastTwo=self.CapturedList[-2:]
                    if (lastTwo[0]!=captured):
                        return True
                    else:
                        return False
                else:
                    return True
        elif(len(captured)>0):
            return True
        else:
            return False






    def make_move(self, move):
        """
        Executes the given go move on the board.

        Parameters:
            move (tuple): The move to be executed.

        Returns:
            None

        Raises:
            None



        Args:
            move (tuple): The move element containing information about the move.
        - Update Turn:
            - Changes the player turn to the next player.
        """
        if move != "PAS":
            if self.is_valid_move(move):
                if self.black_to_move:
                    self.board[move[0]][move[1]] = "B"
                else:
                    self.board[move[0]][move[1]] = "W"

                self.move_log.append(move)  # for  history of the game
                self.UpdateGroupLiberties(move)
                #print(self.CapturedStones(move))
                #print(self.GroupLiberties)
                self.black_to_move = not self.black_to_move  # swap players
        else:
            self.move_log.append(move)
            self.black_to_move = not self.black_to_move
    def get_valid_moves(self):
        """
            Get all valid moves considering checks.

            Returns:
                list: List of valid goMove objects.

            This method retrieves all possible moves and filters out those that would leave
            the current player in check. It also checks for checkmate and stalemate conditions.
        """
        moves=[]

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(self.board[i][j]=="-" and self.is_valid_move((i,j))):
                    moves+=[(i,j)]
        moves+="PAS"


        return moves # should this return a set

   
    def random_move(self, valid_moves):
        """
        Return a random move

        Args:
            valid_moves (list): A list of valid moves

        Returns:
            Move(tuple): A random move from the list of valid moves.
        """
        return valid_moves[random.randint(0, len(valid_moves) - 1)]
