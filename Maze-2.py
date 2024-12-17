def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while not at_goal():
    if wall_on_right() and wall_in_front() :
        while not front_is_clear():
            turn_left()  # Corrected: added parentheses to call the function
            
        
    elif right_is_clear() and front_is_clear():
        turn_right()
        move()

    elif wall_in_front() and not wall_on_right():
        turn_right()
        move()
        
    elif not wall_in_front()and not wall_on_right():
        turn_right()
        move()
        
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
        
        
    elif wall_on_right()and ( not front_is_clear()):  # Properly indented
        turn_right()
        move()
        
    elif not front_is_clear():
        turn_left()
    
    else:  # Properly indented
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
