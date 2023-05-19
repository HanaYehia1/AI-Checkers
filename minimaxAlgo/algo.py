from copy import deepcopy
from Checkers.board import Board
import pygame

WHITE = (255, 255, 255)
BLACK = (0,0,0)

#implementation of minimax algorithm for the player vs computer mode
def minimax(current_position, depth, max_player, game):
    if depth == 0 or current_position.winner() != None:
        return current_position.evaluate(), current_position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(current_position, BLACK, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(current_position, WHITE, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move
    
#implementation of minimax algorithm for the computer vs computer mode
def minimaxAI(current_position, depth, max_player, game):
    if depth == 0 or current_position.winner() != None:
        return current_position.evaluate(), current_position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(current_position, max_player, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(current_position, WHITE, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move
    
#implementation of minimax with alpha-beta pruning algorithm for the player vs computer mode
def minimax_alpha(current_position, depth, alpha, beta,max_player, game):
    if depth == 0 or current_position.winner() != None:
        return current_position.evaluate(), current_position
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(current_position, BLACK, game):
            evaluation = minimax_alpha(move, depth-1, alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(current_position, WHITE, game):
            evaluation = minimax_alpha(move, depth-1, alpha, beta, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval, best_move
    
#implementation of minimax with alpha-beta pruning algorithm for the computer vs computer mode
def minimax_alphaAI(current_position, depth, alpha, beta,maximizing_player, game):
    #checks if the maximum depth has been reached or 
    #if there is a winner in the current position.
    if depth == 0 or current_position.winner() != None:
        return current_position.evaluate(), current_position
    #checks if it is the maximizing player's turn
    if maximizing_player:
        maximumEvaluation = float('-inf')
        best_move = None
        for move in get_all_moves(current_position, maximizing_player, game):
            evaluation = minimax_alpha(move, depth-1, alpha, beta, False, game)[0]
            maximumEvaluation = max(maximumEvaluation, evaluation)
            if maximumEvaluation == evaluation:
                best_move = move
            alpha = max(alpha, maximumEvaluation)
            if beta <= alpha:
                break
        return maximumEvaluation, best_move
    else:
        minimumEvaluation = float('inf')
        best_move = None
        for move in get_all_moves(current_position, WHITE, game):
            evaluation = minimax_alpha(move, depth-1, alpha, beta, True, game)[0]
            minimumEvaluation = min(minimumEvaluation, evaluation)
            if minimumEvaluation == evaluation:
                best_move = move
            beta = min(beta, minimumEvaluation)
            if beta <= alpha:
                break
        return minimumEvaluation, best_move


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_pieces(color):
        valid_moves = board.get_valid_move(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


# def draw_moves(game, board, piece):
#     valid_moves = board.get_valid_move(piece)
#     board.draw(game.win)
#     pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
#     game.draw_valid_moves(valid_moves.keys())
#     pygame.display.update()
#     pygame.time.delay(400)

