# AI Checkers Game
This is a project for a checkers game where there's several game modes whether PVP, CVP and CVC.

> **We Didn't use any help from ChatGPT or any Helping bot so we don't have screenshots for a conversation**

## To Run This project :

 1. install pygame (open cmd -> pip install pygame)
 2. install tkinter (open cmd -> pip install tk)
 3. run main.py 
 4. choose the mode , algorithm type and difficulty level "in case of pvp press start without choosing"
 5. **ENJOY**

> **We are going to a little tour around our files**
## Checkers folder

 - **board.py** **->** *initializes the board dimensions and design. also it checks for the winner and get all valid moves for a specific checkers on board.*
 > This file is only for assistance to used along all of the files of the code "constants.py"
 - **constants.py ->** *initializes the screen dimensions, row and columns number and the size of each square on the board along with the colors used in the game.*  
 
 
 - **game.py ->** *the file that contains the initialization of the game and it updates the game screen after every move. it also contains most of our game logic.*
 
 - **piece.py ->** *this file contains the design of each checker whether its a normal piece or a king piece.*

## minimaxAlgo folder

 - **algo.py ->** *contains the implementation of minimax algorithm and minimaxAI which is for the Computer vs Compter mode also contains a modified minimax with alpha-beta pruning.*

## main.py

 - contains a window that starts at the beginning of the game to choose the game option, algorithm type and difficulty level then prompts the user to the game screen to play

 ## Graphs Measuring The Performance
 

>  The Following Graphs Explains The Difference in performance of
> difficulty levels whether the algorithm is Minimax or Minimax with
> Alpha-Beta Pruning it measures the performance according to Time taken
> for each piece to move over the total number of moves taken to finish
> the game
 
## *Easy Mode Graph :-*

![Easy](https://github.com/HanaYehia1/AI-Checkers/assets/119138360/609342b6-ab50-4c28-b1a6-4bb23d7d63f0)

## *Medium Mode Graph :-*

![Medium](https://github.com/HanaYehia1/AI-Checkers/assets/119138360/1d686cab-5e36-4188-bf31-4d62f9922559)

## *Hard Mode Graph :-*

![Hard](https://github.com/HanaYehia1/AI-Checkers/assets/119138360/085e2154-5ec0-455d-9556-76aab6d0947a)

