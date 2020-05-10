from board import Direction, Rotation
from random import Random
import math


        
class Player:
    def __init__(self, seed=None):
        self.random = Random(seed)

    def choose_action(self, board):                    
        try:
            best_score = -1000000          # intialising data
            best_x = 0
            best_num = 0
            for x in range(board.width):     # all possible x co-ordinates
                for num in range(4):                    # all possible rotations
                    sandbox = board.clone()       
                    num_of_rotation = 0             # cloning the board and testing out best moves
                    move = x - sandbox.falling.left        # calculating which direction to move block. Negative is left and positive is right
                    if move < 0:                           # executing moves in sandbox
                        while num_of_rotation != num:
                            sandbox.rotate(Rotation.Anticlockwise)
                            num_of_rotation += 1
                        for number in range(abs(move)):
                            sandbox.move(Direction.Left)
                        sandbox.move(Direction.Drop)
                    elif move > 0:
                        while num_of_rotation != num:
                            sandbox.rotate(Rotation.Anticlockwise)
                            num_of_rotation += 1
                        for number in range(move):
                            sandbox.move(Direction.Right)
                        sandbox.move(Direction.Drop)
                    else:                           
                        while num_of_rotation != num:
                            sandbox.rotate(Rotation.Anticlockwise)
                            num_of_rotation += 1
                        sandbox.move(Direction.Drop)
                    score = self.evaluate(sandbox)
                    if score > best_score:        # updating best score and moves 
                        best_score = score
                        best_x = move
                        best_num = num
            for numb in range(best_num):        # executing best move
                yield Rotation.Anticlockwise
            if best_x > 0:
                for numbers in range(best_x):
                    yield Direction.Right
            elif best_x < 0:
                for numbers in range(abs(best_x)):
                    yield Direction.Left
            yield Direction.Drop
        except:
            for numb in range(best_num):       
                yield Rotation.Anticlockwise
            if best_x > 0:
                for numbers in range(best_x):
                    yield Direction.Right
            elif best_x < 0:
                for numbers in range(abs(best_x)):
                    yield Direction.Left
            yield Direction.Drop



    def evaluate(self, sandbox):
        score = 100
        list_of_heights = []             # find height of each coloumn
        for x in range(sandbox.width): 
            height = 0
            for y in range(sandbox.height):
                if (x,y) in sandbox.cells:
                    height = 24 - y
                    list_of_heights.append(height)
                    break
            if height == 0:
                list_of_heights.append(height)
                
        aggregate_height = 0       # calculating aggregate height
        for values in list_of_heights:
            aggregate_height += values
            
        bumpiness = 0              # calculating bumpiness
        for values in range(1,len(list_of_heights)):
            bumpiness = bumpiness + abs(list_of_heights[values] - list_of_heights[values-1])

        holes = 0                  # calculating holes
        for x in range(sandbox.width):
            for y in range(sandbox.height):
                if (x,y) in sandbox.cells:
                    if (x,y+1) not in sandbox.cells and y != 23:
                        holes += 1
    
        aggregate_height = aggregate_height / 200       # normalising aggregate height and bumpiness
        bumpiness = bumpiness / 50
        score = - bumpiness * 47 - holes**2 - aggregate_height * 100
        return score

SelectedPlayer = Player

