a = [_, _, _]
b = [_, _, _]
c = [_, _, _] 
X = ['top_left', 'top_middle', 'top_right', 'middle_left', 'middle_middle', 'middle_right', 'bottom_left', 'bottom_middle', 'bottom_right']
print("Your moves are:", X)
# had used for loop: for x in X; but that kept looping only x input so i had to change that.
def xmove():
    x = input("enter your move for [X]: ")
    if x == 'top_left':
        X.remove('top_left') # list remove keeps the whole game from falling apart. you cannot choose same choices twice thanks to the error. and it was totally unintentional. but if it works, it works.
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
    y = input("enter your move for [O]: ")
    if y == 'top_left':
        X.remove('top_left')
        a[0] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('top_middle'):
        X.remove('top_left') 
        a[1] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('top_right'):
        X.remove('top_left') 
        a[2] = "O"
        print(a)
        print(b) 
        print(c)
    elif y == ('middle_left'):
        X.remove('top_left') 
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
while True: # so that it keeps looping, althou it will keep looping. so i need to change that.
    xmove()
    ymove()
    
# in summary. great progress. need to find a way to stop the game at some point, making it more compact, this looks like coding a big stone hammer for a tiny walnut. stay tuned!
