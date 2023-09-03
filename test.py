while not at_goal():
 if front_is_clear():
    move()
 elif  wall_in_front():
    turn_left()
    move()
    while  wall_on_right():
      turn_left()
      move()
else :    
    turn_right() 


    i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1



while not at_goal():
 if front_is_clear():
    move()
  
 elif wall_in_front():
        turn_left()
    
 while wall_on_right():
   move()
 if not wall_on_right():
        break
 turn_right()
 move()
 turn_right()
 move()
    

def pass_wall():
    turn_left()
    walk_count =0
    while wall_on_right():
       walk_count += 1
       move()
    turn_right()
    move()
    turn_right()
    while walk_count > 0 :
        move()
        walk_count-=1
    turn_left()
while not at_goal():
   if wall_in_front():
       pass_wall()
   else:
       move()    


while not at_goal():
    if front_is_clear():
        move 
    elif front_is_clear() and not right_is_clear():
        turn_left() 
        move
    
    

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    turn_right()
    while wall_on_right() and not wall_in_front():
        move()
        if wall_in_front():
           turn_left()
        elif wall_on_right()
             move()



   
def turn_right():
    turn_left()
    turn_left()
    turn_left()
tuck_left = 0
while not at_goal():
      while front_is_clear():
            move()
      if wall_in_front() and wall_on_right():
           turn_left() 
           tuck_left +=1
      elif wall_in_front() and  right_is_clear():
           turn_right()
      elif tuck_left>=1():
           turn_right()         


     while front_is_clear():
            move()     
      if   wall_in_front() and wall_on_right():
           turn_left() 
           tuck_left +=1
      elif wall_in_front() and  right_is_clear():
           turn_right()
      elif tuck_left==2:
           turn_right()