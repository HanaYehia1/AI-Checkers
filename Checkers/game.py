import pygame
from .constants import BLACK, WHITE, SILVER,SQUARE_SIZE,WIDTH,HEIGHT
from Checkers.board import Board


class Game:
    def __init__(self,win):
        # Initialize the game by setting its initial state and creating a new board
        self._init()
        self.win = win

    def update(self):
        # Update the game by drawing the board and the valid moves and updating the display
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        # Set the initial state of the game by selecting no piece, creating a new board, setting the turn to white, and setting the valid moves to an empty dictionary
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    def reset(self):
        # Reset the game by setting its initial state
       self._init()

    def select(self, row, col):
        # Select a piece on the board by setting it to be the selected piece if it is the player's turn and has valid moves, and return True. Otherwise, return False.
        if self.selected:
            result = self._move(row,col)
            if not result:
                self.selected = None
                self.select(row,col)

        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_move(piece)
            return True
    
        return False

    def _move(self, row, col):
        # Move a piece on the board by updating the board state and changing the turn if the move is valid, and return True. Otherwise, return False.
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected, row , col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True
    

    def change_turn(self):
        # Change the turn from white to black or from black to white, and reset the valid moves to an empty dictionary
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def draw_valid_moves(self,moves):
        # Draw circles on the screen to indicate where the valid moves are for a selected piece
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, SILVER , (col* SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE //2),20)

    def winner(self):
        # Return the winner of the game by calling the winner method of the board
        return self.board.winner()
    
    def draw_winner(self):
        # Get the winner of the game
        winner = self.winner()
        # If there is a winner, draw the winner's color and a message indicating the winner
        if winner != None:
            font = pygame.font.SysFont('comicsans', 100)
            if winner == WHITE:
                text = font.render('White Wins!', 1, BLACK)
            else:
                text = font.render('Black Wins!', 1, WHITE)
            self.win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
            pygame.display.update()