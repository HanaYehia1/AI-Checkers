import pygame
import tkinter as tk
from Checkers.constants import SQUARE_SIZE,WIDTH, HEIGHT , WHITE,BLACK
from Checkers.board import Board 
from Checkers.game import Game
from minimaxAlgo.algo import minimax,minimax_alpha

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
    depth = difficulty_depths[difficulty_level]
    root.withdraw()
    game = Game(WIN)
    # Set the game to run and create a clock to keep track of time
    run = True
    clock = pygame.time.Clock()
    # Create a new game object with the Pygame window
    if game_mode == "Player vs Player":
        
        # algorithm_label.pack_forget()
        # algorithm_dropdown.grid_forget()
        # difficulty_label.pack_forget()
        # difficulty_dropdown.grid_forget()

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
            if game.turn == WHITE:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        # Quit the game if the user clicks the close button
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # If the user clicks the mouse, get the row and column of the square they click on and select that square in the game
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row,col)
            else:
                if algorithm_type =="Minimax":
                    value, new_board = minimax(game.get_board(), depth, BLACK, game)
                    game.ai_move(new_board)
                    pygame.time.delay(300)
                elif algorithm_type == "Minimax with Alpha-Beta Pruning":
                    value, new_board = minimax_alpha(game.get_board(), depth,float('inf'),float('-inf'), BLACK, game)
                    game.ai_move(new_board)
                    pygame.time.delay(300)
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
                    value, new_board = minimax(game.get_board(), 2, WHITE, game)
                    game.ai_move(new_board)
                    pygame.time.delay(300)
            elif game.turn==BLACK:
                if game.winner()==BLACK:
                    run = False
                else:
                    if algorithm_type =="Minimax":
                        value, new_board = minimax(game.get_board(), depth, BLACK, game)
                        game.ai_move(new_board)
                        pygame.time.delay(300)
                    elif algorithm_type == "Minimax with Alpha-Beta Pruning":
                        value, new_board = minimax_alpha(game.get_board(), depth,float('inf'),float('-inf'), BLACK, game)
                        game.ai_move(new_board)
                        pygame.time.delay(300)
                # Update the game display
            game.update()

        # Quit Pygame after the game loop ends
        game.draw_winner()
        pygame.time.delay(10000)
        pygame.quit()





root = tk.Tk()
root.title("Checkers Game")
root.geometry("500x500")
root.configure(bg="#c0c0c0")
game_label = tk.Label(root, text="Select Game Mode:", font=("Helvetica", 14))
game_label.pack(pady=10)
game_options = ["Player vs Player", "Computer vs Player", "Computer vs Computer"]
game_var = tk.StringVar(root)
game_var.set(game_options[0])
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
# Define a dictionary to map the difficulty levels to the corresponding depths
difficulty_depths = {"Easy": 2, "Medium": 4, "Hard": 6}
# Call the main function to start the game
root.mainloop()

