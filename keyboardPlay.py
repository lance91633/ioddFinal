# import the module
from pymouse import PyMouse
import time
import evdev
from evdev import categorize
#--------------
# Configuration 
#--------------
up_pos = [966, 152] 
down_pos = [932, 855]
right_pos = [1538, 500] 
left_pos = [400, 485]
x_axis = 948 
y_axis = 497
sensitivity = 20
mode = "ABS" # ABS or FREE
#print(myGamepad) # show the device's information

#----------------
# Initialization 
#----------------
m = PyMouse()
#----------------
# Function
#----------------
def printMousePos():
    "This shows the position of the mouse"
    print m.position()
    return

def keyboardPlay(mode):
    "Use keyboard to play this game"
    myKeyBoard = evdev.InputDevice('/dev/input/event6')
    print(myKeyBoard)
    if(mode == 'ABS'):
        for eventGame in myKeyBoard.read_loop():
            if eventGame.type == evdev.ecodes.EV_KEY:
                varGame = categorize(eventGame)
                keyGame = varGame.keycode
                if(keyGame == 'KEY_DOWN'):
                    m.move(down_pos[0], down_pos[1])
                elif(keyGame == 'KEY_RIGHT'):
                    m.move(right_pos[0], right_pos[1])
                elif(keyGame == 'KEY_LEFT'):
                    m.move(left_pos[0], left_pos[1])
                elif(keyGame == 'KEY_UP'):
                    m.move(up_pos[0], up_pos[1])
    elif(mode == 'FREE'):
        for eventGame in myKeyBoard.read_loop():
            if eventGame.type == evdev.ecodes.EV_KEY:
                varGame = categorize(eventGame)
                keyGame = varGame.keycode
                x_here = x_axis
                y_here = y_axis
                if(keyGame == 'KEY_DOWN'):
                    y_here = y_here + sensitivity
                elif(keyGame == 'KEY_RIGHT'):
                    x_here = x_here + sensitivity
                elif(keyGame == 'KEY_LEFT'):
                    x_here = x_here - sensitivity
                elif(keyGame == 'KEY_UP'):
                    y_here = y_here - sensitivity
                x_axis = x_here
                y_axis = y_here
    return

def gamePadPlay(mode):
    "Use gamepad to play this game"
    myGamepad = evdev.InputDevice('/dev/input/event16')
    if(mode == 'ABS'):
        for eventGame in myGamepad.read_loop():
            if eventGame.type == evdev.ecodes.EV_KEY:
                varGame = categorize(eventGame)
                keyGame = varGame.keycode
                if(keyGame[0] == 'BTN_A'):
                    m.move(down_pos[0], down_pos[1])
                elif(keyGame[0] == 'BTN_B'):
                    m.move(right_pos[0], right_pos[1])
                elif(keyGame[1] == 'BTN_X'):
                    m.move(left_pos[0], left_pos[1])
                elif(keyGame[1] == 'BTN_Y'):
                    m.move(up_pos[0], up_pos[1])
    elif(mode == 'FREE'):
        for eventGame in myGamepad.read_loop():
            if eventGame.type == evdev.ecodes.EV_KEY:
                varGame = categorize(eventGame)
                keyGame = varGame.keycode
                x_here = x_axis
                y_here = y_axis
                if(keyGame[0] == 'BTN_A'):
                    y_here = y_here + sensitivity
                elif(keyGame[0] == 'BTN_B'):
                    x_here = x_here + sensitivity
                elif(keyGame[1] == 'BTN_X'):
                    x_here = x_here - sensitivity
                elif(keyGame[1] == 'BTN_Y'):
                    y_here = y_here - sensitivity
                x_axis = x_here
                y_axis = y_here
    return

#--------------
# main program
#--------------

keyboardPlay('FREE')



# click works about the same, except for int button possible values are 1: left, 2: right, 3: middle
# m.click(500, 300, 1)
