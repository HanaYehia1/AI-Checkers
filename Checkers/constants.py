import pygame

# Define the width and height of the screen
WIDTH, HEIGHT = 800, 800
# Define the number of rows and columns on the board
ROWS, COLUMNS = 8, 8
# Calculate the size of each square on the board based on the width and number of columns
SQUARE_SIZE = WIDTH//COLUMNS

# Define some colors in RGB format
WHITE = (255,255,255)       #AI
BLACK = (0,0,0)             #board
SILVER = (192,192,192)      #board
DIMGRAY = (105,105,105)     #Computer
SLATEGRAY = (112,128,144)   #outline
DARKBROWN = (92, 64, 51)
DESERTSAND = (237, 201, 175)
BURLYWOOD = (222,184,135)
SIENNA = (160,82,45)

# Load the crown image and scale it to a size of 45x25 pixels
CROWN = pygame.transform.scale(pygame.image.load('CrownKing/crown.png'), (45,25))