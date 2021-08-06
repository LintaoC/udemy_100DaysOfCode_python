def turn_right():
    turn_left()
    turn_left()
    turn_left()

loop_count = 0
while not at_goal():
    while not wall_on_right():
        if right_is_clear():
            turn_right()
            move()
            loop_count += 1
            
        if loop_count >4:
            if front_is_clear():
                move()
                loop_count = 0
            else:
                loop_count = 0
                turn_left()
            
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    loop_count = 0
