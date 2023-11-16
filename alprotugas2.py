"""Nama kelompok
1. Zaki Fikri Ardiansyah 23091397149
2. Roland Savitar Herdiansyah 23091397145
3. Nur Fatehah 23091397160
"""

def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()

elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
