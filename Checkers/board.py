import pygame
from .constants import BLACK, ROWS, DIMGRAY, SQUARE_SIZE, COLUMNS, WHITE, SILVER, DARKBROWN, DESERTSAND, BURLYWOOD, SIENNA
from .piece import Piece

class Board:
    def __init__(self):
        # Initialize the board as an empty 2D list
        self.board = []
        # Set the initial number of pieces for each color
        self.white_left = self.black_left = 12
        # Set the initial number of kings for each color to 0
        self.white_kings = self.black_kings = 0
        # Create the starting position for the game
        self.create_board()

    def draw_square(self, win):
        # Fill the window with a brown color
        win.fill(SIENNA)
        # Draw alternating squares in a lighter color
        for row in range(ROWS):
            for col in range(row % 2, COLUMNS, 2):
                pygame.draw.rect(win, BURLYWOOD, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        # Create the starting position for the game by placing the pieces in their initial positions on the board
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLUMNS):
                # Check if the current position is a valid position for a piece
                if col % 2 == ((row + 1) % 2):
                    # If the current position is a valid position for a black piece, place a black piece there
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    # If the current position is a valid position for a white piece, place a white piece there
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE))
                    # If the current position is not a valid position for a piece, place a 0 there to represent an empty space
                    else:
                        self.board[row].append(0)
                # If the current position is not a valid position for a piece, place a 0 there to represent an empty space
                else:
                    self.board[row].append(0)

    def move(self, piece, row, col):
        # Move the piece from its current position to the new position (row, col)
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        # Update the piece's position on the board
        piece.move(row, col)
        self.moves__done = 0
        # If the piece reaches the opposite end of the board, it becomes a king
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            # Update the count of kings for the piece's color
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1


    def get_piece(self, row, col):
        # Return the piece at position (row, col) on the board
        return self.board[row][col]


    def draw(self, win):
        # Draw the board by calling draw_square() and then drawing each piece on the board
        self.draw_square(win)
        for row in range(ROWS):
            for col in range(COLUMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    def get_valid_move(self, piece):
        # Get all the valid moves for the given piece on the board
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        # Check if the piece is a white piece or a king
        if piece.color == WHITE or piece.king:
            # If the piece is a white piece or a king, check for valid moves in the left direction
            moves.update(self._move_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            # If the piece is a white piece or a king, check for valid moves in the right direction
            moves.update(self._move_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        # Check if the piece is a black piece or a king
        if piece.color == BLACK or piece.king:
            # If the piece is a black piece or a king, check for valid moves in the left direction
            moves.update(self._move_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            # If the piece is a black piece or a king, check for valid moves in the right direction
            moves.update(self._move_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        # Return the dictionary of valid moves
        return moves

    def winner(self):
        # Check if one color has no pieces left
        if self.white_left <= 0:
            return BLACK
        elif self.black_left <= 0:
            return WHITE
        return None
    
    def get_pieces(self,color):
        # Returns the pieces of the specified color
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
    
    #this function recursively explores all valid moves
    #a piece can make in the left direction, taking into account 
    #any pieces that need to be skipped over during the move.
    def _move_left(self, start, stop, step, color, left, skipped=[]):
        #initializes an empty dictionary to store the valid moves found by the function
        moves = {}
        #initializes an empty list to store any pieces that have been skipped over during the current move
        last = []
        #iterates over the rows from start to stop
        for r in range(start, stop, step):
            #checks if the current column is out of bounds
            if left < 0:
                break
            #gets the piece located at the current row and column on the board
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._move_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._move_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves
    

    #this function recursively explores all valid moves
    #a piece can make in the right direction, taking into account 
    #any pieces that need to be skipped over during the move.
    def _move_right(self, start, stop, step, color, right, skipped=[]):
        # Helper function used by get_valid_move() to find all the valid moves in the right direction for a given piece
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._move_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._move_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves
    
    def remove(self, pieces):
    # Remove the specified pieces from the board and update the count of remaining pieces for each color
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == WHITE:
                    self.white_left -=1
                else:
                    self.black_left -=1
                


    def evaluate(self):
        # Calculates the evaluation of the current position
        return self.black_left - self.white_left + (self.black_kings * 0.5 - self.white_kings * 0.5)
    
