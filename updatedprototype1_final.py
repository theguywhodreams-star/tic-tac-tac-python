a = [_, _, _]
b = [_, _, _]
c = [_, _, _] 
X = ['top_left', 'top_middle', 'top_right', 'middle_left', 'middle_middle', 'middle_right', 'bottom_left', 'bottom_middle', 'bottom_right']
def winning_conditions():
    if a[0] =='X' and  b[0] =='X' and c[0] == 'X':
        print ("the game is finished, X had won the game")
        exit()   # manually added the exit because i didnt know how to actually do it.
    elif a[0] == 'X' and b[1] == 'X' and c[2] == 'X':
        print ("the game is finished, X had won the game")
        exit()
    elif a[2] =='X' and  b[1] =='X' and c[0] == 'X':
        print ("the game is finished, X had won the game")
        exit()
    elif a[0] =='X' and  a[1] =='X' and a[2] == 'X':
        print ("the game is finished, X had won the game")
        exit()
    elif b[0] =='X' and  b[1] =='X' and b[2] == 'X':
        print ("the game is finished, X had won the game")
        exit()
    elif c[0] =='X' and  c[1] =='X' and c[2] == 'X':
        print ("the game is finished, X had won the game")
        exit()
    elif a[0] =='O' and  b[0] =='O' and c[0] == 'O':
        print ("the game is finished, O had won the game")
        exit()
    elif a[0] == 'O' and b[1] == 'O' and c[2] == 'O':
        print ("the game is finished, O had won the game")
        exit()
    elif a[2] =='O' and  b[1] =='O' and c[0] == 'O':
        print ("the game is finished, O had won the game")
        exit()
    elif a[0] =='O' and  a[1] =='O' and a[2] == 'O':
        print ("the game is finished, O had won the game")
        exit()
    elif b[0] =='O' and  b[1] =='O' and b[2] == 'O':
        print ("the game is finished, O had won the game")
        exit()
    elif c[0] =='O' and  c[1] =='O' and c[2] == 'O':
        print ("the game is finished, O had won the game")
        exit()
    else:
        print("no one has won the game, its a tie")

def xmove():
    print("Your moves are:", X)
    x = input("enter your move for [X]: ")
    if x == 'top_left':
        X.remove('top_left') 
        a[0] = "X"
        print(a)
        print(b) 
        print(c)
    elif x == ('top_middle'):
        X.remove('top_middle') 
        a[1] = "X"
        print(a)
        print(b) 
        print(c)
    elif x == ('top_right'):
        X.remove('top_right') 
        a[2] = "X"
        print(a)
        print(b) 
        print(c)
    elif x == ('middle_left'):
        X.remove('middle_left') 
        b[0] = "X"
        print(a)
        print(b) 
        print(c) 
    elif x == ('middle_middle'):
        X.remove('middle_middle') 
        b[1] = "X"
        print(a)
        print(b) 
        print(c)
    elif x == ('middle_right'):
        X.remove('middle_right') 
        b[2] = "X"
        print(a)
        print(b) 
        print(c)
    elif x == ('bottom_left'):
        X.remove('bottom_left') 
        c[0] = "X"
        print(a)
        print(b) 
        print(c)
    elif x == ('bottom_middle'):
        X.remove('bottom_middle') 
        c[1] = "X"
        print(a)
        print(b) 
        print(c)
    elif x == ('bottom_right'):
        X.remove('bottom_right') 
        c[2] = "X"
        print(a)
        print(b) 
        print(c)      
def ymove():
    print("Your moves are:", X)
    y = input("enter your move for [O]: ")
    if y == 'top_left':
        X.remove('top_left')
        a[0] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('top_middle'):
        X.remove('top_middle') 
        a[1] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('top_right'):
        X.remove('top_right') 
        a[2] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('middle_left'):
        X.remove('middle_left') 
        b[0] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('middle_middle'):
        X.remove('middle_middle') 
        b[1] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('middle_right'):
        X.remove('middle_right') 
        b[2] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('bottom_left'):
        X.remove('bottom_left') 
        c[0] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('bottom_middle'):
        X.remove('bottom_middle') 
        c[1] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('bottom_right'):
        X.remove('bottom_right') 
        c[2] = "O"
        print(a)
        print(b) 
        print(c)
xmove()
ymove()
xmove()
ymove()
xmove()
winning_conditions()
ymove()
winning_conditions()
xmove()
winning_conditions()
ymove()
winning_conditions()
xmove()
winning_conditions()
# couldnt find a better way to do this, my knowledge is limited, the code is heavy, unrefined and slow, wait for prototype 2!!
