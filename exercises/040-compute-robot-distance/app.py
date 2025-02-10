# Your code here
def compute_robot_distance(array):
    height = 0
    width = 0

    for x in array:
        direction, steps = x.split()  
        steps = int(steps)

        if direction == 'UP' :
            height += steps
        elif direction == 'DOWN' :
            height -= steps
        elif direction == 'RIGHT' :
            width += steps
        elif direction == 'LEFT' :
            width -= steps
    
    distance = (height**2 + width**2)**0.5
    return round(distance)

print(compute_robot_distance(["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]))