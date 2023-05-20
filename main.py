import pygame
import tkinter as tk
from Checkers.constants import SQUARE_SIZE,WIDTH, HEIGHT , WHITE,BLACK
from Checkers.board import Board 
from Checkers.game import Game
from minimaxAlgo.algo import minimax,minimax_alpha,minimax_alphaAI,minimaxAI

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
def start_game():

    algorithm_type = algorithm_var.get()
    difficulty_level = difficulty_var.get()
    game_mode = game_var.get()
   
    if difficulty_level == "Easy":
        depth = 1
    elif difficulty_level == "Medium":
        depth = 3
    elif difficulty_level == "Hard":
        depth = 5

    root.withdraw()
    game = Game(WIN)
    # Set the game to run and create a clock to keep track of time
    run = True
    clock = pygame.time.Clock()
    # Create a new game object with the Pygame window
    if game_mode == "Player vs Player":

        while run:
        # Set the frame rate of the game and check if there is a winner
            clock.tick(FPS)
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

            game.update()
        game.draw_winner()
        pygame.time.delay(10000)
        pygame.quit()

    elif game_mode == "Computer vs Player":
        while run:
            clock.tick(FPS)

            if game.winner() != None:
                run = False

            #checks if it is currently the black player's turn to move.
            if game.turn == BLACK:
                if algorithm_type =="Minimax":
                    value, new_board = minimax(game.get_board(), depth, BLACK, game)
                    game.ai_move(new_board)
                    pygame.time.delay(300)
                    
                elif algorithm_type == "Minimax with Alpha-Beta Pruning":
                    value, new_board = minimax_alpha(game.get_board(), depth,float('-inf'),float('inf'), BLACK, game)
                    game.ai_move(new_board)
                    pygame.time.delay(300)
            elif game.turn == WHITE:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        # Quit the game if the user clicks the close button
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # If the user clicks the mouse, get the row and column of the square they click on and select that square in the game
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row,col)
            
            game.update()
        game.draw_winner()
        pygame.time.delay(10000)
        pygame.quit()

    elif game_mode == "Computer vs Computer":
    # Start the game loop
        while run:
            # Set the frame rate of the game and check if there is a winner
            clock.tick(FPS)

            if game.turn == WHITE:
                if game.winner()== WHITE:
                    run = False
                else:
                    value, new_board = minimaxAI(game.get_board(), 2, WHITE, game)
                    game.ai_move(new_board)
                    pygame.time.delay(300)
            elif game.turn==BLACK:
                if game.winner()==BLACK:
                    run = False
                else:
                    if algorithm_type =="Minimax":
                        value, new_board = minimaxAI(game.get_board(), depth, BLACK, game)
                        game.ai_move(new_board)
                        pygame.time.delay(300)
                    elif algorithm_type == "Minimax with Alpha-Beta Pruning":
                        value, new_board = minimax_alphaAI(game.get_board(), depth,float('-inf'),float('inf'), BLACK, game)
                        game.ai_move(new_board)
                        pygame.time.delay(300)
                # Update the game display
            game.update()

        # Quit Pygame after the game loop ends
        game.draw_winner()
        pygame.time.delay(10000)
        pygame.quit()




#creates a new Tkinter window object
root = tk.Tk()
#sets the title of the window to "Checkers Game".
root.title("Checkers Game")
#sets the size of the window to 500x500
root.geometry("400x400")
#sets the background color of the window to light gray
root.configure(bg="#c0c0c0")
#creates a label object 
game_label = tk.Label(root, text="Select Game Mode:", font=("Helvetica", 14))
game_label.pack(pady=10)
#creates a radio button object to select game mode
game_options = ["Player vs Player", "Computer vs Player", "Computer vs Computer"]
#creates a new string variable that will hold the selected game mode
game_var = tk.StringVar(root)
#sets the default value of the game mode variable to the first value in the game_options list.
game_var.set(game_options[0])
#creates a dropdown menu with game optionts to select game mode
game_dropdown = tk.OptionMenu(root, game_var, *game_options)
game_dropdown.pack(pady=10)
algorithm_label = tk.Label(root,text="Select Algorithm Type:",font=("Helvetica", 14))
algorithm_label.pack(pady=10)
algorithm_options = ["Minimax", "Minimax with Alpha-Beta Pruning"]
algorithm_var = tk.StringVar(root)
algorithm_var.set(algorithm_options[0])
algorithm_dropdown = tk.OptionMenu(root,algorithm_var,*algorithm_options)
algorithm_dropdown.pack(pady=10)
difficulty_label = tk.Label(root,text="Select Difficulty Level:",font=("Helvetica", 14))
difficulty_label.pack(pady=10)
difficulty_options = ["Easy", "Medium", "Hard"]
difficulty_var = tk.StringVar(root)
difficulty_var.set(difficulty_options[0])
difficulty_dropdown = tk.OptionMenu(root, difficulty_var, *difficulty_options)
difficulty_dropdown.pack(pady=10)
start_button = tk.Button(root,text="Start Game",command=start_game,bg="#008080", fg="white", font=("Helvetica", 14))
start_button.pack(pady=20)
# Call the main function to start the game
root.mainloop()

