"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, 

returns the number of possible arrangements of the board where N queens 

can be placed on the board without threatening each other,

i.e. no two queens share the same row, column, or diagonal.

"""

n = int(input(" Enter the no of queens to get the solutions ! "))
current_sol = [0 for x in range(n)]
solutions = []

def is_safe(t_row,t_col):
    #no need to check for the first queen 
    if t_row == 0:
        return True
    for row in range(0,t_row):
        #checking vertically 
        if t_col==current_sol[row]:
            return False
        #checking the diagonals 
        if abs(t_row-row)==abs(t_col-current_sol[row]):
            return False
    return True 

def queens(row):
    global n,current_sol,solutions
    for col in range(n):
        if not is_safe(row,col):
            continue 
        else:
            current_sol[row]=col
            if row==(n-1):
                solutions.append(current_sol.copy())
            else:
                queens(row+1)

queens(0)
print(len(solutions),"solutions found !")
for solution in solutions :
    print(solution)
