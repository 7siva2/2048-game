from utilities import generate_piece, print_board
import copy
DEV_MODE = False
#----------------------------------------------------------------------------------------------------------------------------
def shiftright(game_board): # This shifts the Matrix to Right
    for x in  range(4):
        for i in range(len(game_board)):
            for j in range(len(game_board[i]) - 1, 0, -1):
                if game_board[i][j] == 0:
                    game_board[i][j],game_board[i][j-1] = game_board[i][j-1],game_board[i][j]
#----------------------------------------------------------------------------------------------------------------------------
def shiftleft(game_board): # This shifts the Matrix to left 
    for j in range(4):
        for i in range(len(game_board)):
            for j in range(len(game_board[i])-1):
                if game_board[i][j] == 0:
                    game_board[i][j+1],game_board[i][j] = game_board[i][j],game_board[i][j+1]
#-----------------------------------------------------------------------------------------------------------------------------
def shifttop(game_board):# shift the Matrix elements to the right 
    for x in range(4):
        for i in range(len(game_board)):
            for j in range(len(game_board[i])-1):
                
                if game_board[j][i] == 0:
                    
                    game_board[j][i],game_board[j+1][i] = game_board[j+1][i],game_board[j][i]
#------------------------------------------------------------------------------------------------------------------------------
def shiftdown(game_board):
    for x in range(4):
        for i in range(len(game_board)):
            
            for j in range(len(game_board[i])-1):
                    
                if game_board[j+1][i] == 0:
                    game_board[j][i],game_board[j+1][i] = game_board[j+1][i],game_board[j][i]
#---------------------------------------------------------------------------------------------------------------------------
def win_check(game_board):
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 2048:
                return 0
#---------------------------------------------------------------------------------------------------------------------------
def game_over(game_board):

    for i in game_board:
        if 0 in i:
            return True

    for i in range(len(game_board)-1): 
        for j in range(len(game_board[0])-1):
            if game_board[i][j] == game_board[i+1][j] or game_board[i][j+1] == game_board[i][j] or game_board[i][j] == 0:
                return True

    for j in range(len(game_board)-1):
        if(game_board[3][j]== game_board[3][j + 1] or game_board[3][j] == 0):
            return True
 
    for i in range(len(game_board)-1):
        if(game_board[i][3]== game_board[i + 1][3] or game_board[i][3] == 0):
            return True

    return False
def copy_list(game_board):
    new_list = []
    new_list = game_board
    return new_list

#----------------ABOVE ARE THE FUNCTIONS-----------------------------------------------------------------------------------------------------------
#--------------------------------------------------ABOVE ARE THE FUNCTIONS-------------------------------------------------------------------------                  
def main(game_board: [[int, ], ]) -> [[int, ], ]:

    for i in range(2):
        d = generate_piece(game_board)
        game_board[d['row']][d['column']] = d['value']
    print_board(game_board)
    user_input = input()
    
    while True:
        
        temp_board = copy.deepcopy(game_board)       
        if user_input == 'q':
            print("Goodbye")
            break
        check = game_over(game_board)
        print(check)
        #-----------------------------------------------------------------------------------------------------------------------
        if check == False:
            print("Game Over No moves")
            break
        #---------------------------------------------------------------------------------------------------------------------------
        
        if check == True:
            print("GAME NOT OVER PLAY!")
        #---------------------------------------------------------------------------------------------------------------------------
        if user_input == 'd' or user_input == 'D' and check == True:  # This shifts the Matrix to Right
            shiftright(game_board)               
            for j in range(4):
                for i in range(len(game_board[j])-1, 0, -1):
                    if game_board[j][i] == game_board[j][i-1] and game_board[j][i] != 0:
                        
                        game_board[j][i] = game_board[j][i] + game_board[j][i-1]
                        game_board[j][i-1] = 0

            shiftright(game_board)
            if temp_board != game_board:
                
                d = generate_piece(game_board)
                game_board[d['row']][d['column']] = d['value']
            
            print_board(game_board)
            To_check_winning = win_check(game_board)            
            if To_check_winning == 0:
                break

        #---------------------------------------------------------------------------------------------------------------------------
        elif user_input == 'a' or user_input == 'A' and check == True:  # This shifts the Matrix to Left
            shiftleft(game_board)     
            for i in range(len(game_board)):
                for j in range(len(game_board[i])-1):
        
                    if game_board[i][j+1] != 0 and game_board[i][j] == game_board[i][j+1]:
            
                        game_board[i][j] = game_board[i][j] + game_board[i][j+1]
                        game_board[i][j+1] = 0
            shiftleft(game_board)
            if temp_board != game_board:
                
                d = generate_piece(game_board)
                game_board[d['row']][d['column']] = d['value']
            
            print_board(game_board)
            To_check_winning = win_check(game_board)
            if To_check_winning == 0:
                break
        #---------------------------------------------------------------------------------------------------------------------------
        elif user_input == 'w' or user_input == 'W' and check == True:  # This shifts the Matrix to Top:
            shifttop(game_board)
            for i in range(len(game_board)):
                for j in range(len(game_board[i])-1):
        
                    if game_board[j][i] != 0 and game_board[j][i] == game_board[j+1][i]:
            
                        game_board[j][i] = game_board[j][i] + game_board[j+1][i]
            
                        game_board[j+1][i] = 0

            shifttop(game_board)
            if temp_board != game_board:
                
                d = generate_piece(game_board)
                game_board[d['row']][d['column']] = d['value']
           
            print_board(game_board)
            To_check_winning = win_check(game_board)
            if To_check_winning == 0:
                break
        #---------------------------------------------------------------------------------------------------------------------------
        
        elif user_input == 's' or user_input == 'S' and check == True:  # This shifts the Matrix to Down:
            
            
            shiftdown(game_board)
            for i in range(len(game_board)):
                for j in range(len(game_board[i])-1,0,-1):
                    if game_board[j][i] != 0 and game_board[j][i] == game_board[j-1][i]:
                        
                        game_board[j][i] = game_board[j][i] + game_board[j-1][i]
                        game_board[j-1][i] = 0
                
            shiftdown(game_board)
            if temp_board != game_board:
                d = generate_piece(game_board)
                game_board[d['row']][d['column']] = d['value']
            
            print_board(game_board)
            To_check_winning = win_check(game_board)
            if To_check_winning == 0:
                break
        
            
        #---------------------------------------------------------------------------------------------------------------------------        

        if user_input == 'q':
            print("Goodbye")
            break
        check = game_over(game_board)
        
        if check == False:
            print("Game Over No moves")
            break
        
        user_input = input()
    return game_board

if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])


    
