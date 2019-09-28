from turtle import*
def draw(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'L':
        left(val)
    elif do == 'R':
        right(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('Unknown Command')
        
def str_art(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ':', cmd_type, num)
        draw(cmd_type, num)

instructions = '''Enter a program for the turtle(Start with N-):
eg. N-F100-R45-U-F100-L45-D-F100-R90-B50
N = New drawing
U/D = Pen up/Pen down
F(intergers) = Forward(intergers)steps
B(intergers) = Backward(intergers)steps
L(intergers) = Left turn(intergers)degrees
R(intergers) = Right turn(intergers)degrees'''
screen = getscreen()
while True:
    t_program = screen.textinput('Drawing Machine', instructions)
    print(t_program)
    if t_program == None or t_program.upper() == 'END':
        break
    str_art(t_program)[/quote]
