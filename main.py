import pygame
from Checkers.constants import SQUARE_SIZE,WIDTH, HEIGHT , WHITE,BLACK
from Checkers.board import Board 
from Checkers.game import Game
from minimaxAlgo.algo import minimax

# Set the frames per second and create a Pygame window
FPS = 60
pygame.init() # Initialize Pygame's display module
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers')

# Define a function to get the row and column of a square based on the mouse position
def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col

# Define the main function of the game
def main():
    # Set the game to run and create a clock to keep track of time
    run = True
    clock = pygame.time.Clock()
    # Create a new game object with the Pygame window
    game = Game(WIN)
  
    # Start the game loop
    while run:
        # Set the frame rate of the game and check if there is a winner
        clock.tick(FPS)

        if game.turn == BLACK:
            value, new_board = minimax(game.get_board(),2,BLACK,game)
            game.ai_move(new_board)
        
        if game.winner() != None:
            run = False

        # Check for events in the Pygame window
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                # Quit the game if the user clicks the close button
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicks the mouse, get the row and column of the square they click on and select that square in the game
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)

        # Update the game display
        game.update()

    game.draw_winner()
    pygame.time.delay(10000)
    # Quit Pygame after the game loop ends
    pygame.quit()

# Call the main function to start the game
main()

