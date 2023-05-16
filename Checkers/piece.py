from .constants import DIMGRAY , SQUARE_SIZE , SLATEGRAY, CROWN
import pygame


class Piece:
    # Set class variables for the padding and outline of the piece
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        # Initialize the piece with its row, column, and color
        self.row = row
        self.col = col
        self.color = color
        # Set the piece to not be a king by default
        self.king = False
        # Set the initial position of the piece on the board
        self.x = 0
        self.y = 0
        # Calculate the actual position of the piece on the screen
        self.calc_pos()

    def calc_pos(self):
        # Calculate the position of the piece on the screen based on its row, column, and the size of each square
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        # Set the piece to be a king
        self.king = True
    
    def draw(self, win):
        # Define the radius of the piece
        radius = SQUARE_SIZE//2 - self.PADDING
        # Draw the outline of the piece
        pygame.draw.circle(win, SLATEGRAY, (self.x, self.y), radius + self.OUTLINE)
        # Draw the actual piece with its color
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        # If the piece is a king, draw a crown on top of it
        if self.king:
            win.blit(CROWN,(self.x - CROWN.get_width()//2 , self.y - CROWN.get_height()//2))

    def move(self, row, col):
        # Move the piece to a new position on the board
        self.row = row
        self.col = col
        # Calculate the new position of the piece on the screen
        self.calc_pos()

    def __repr__(self):
        # Return a string representation of the piece's color
        return str(self.color)