import os, keyboard, curses
from pickle import FALSE

appname = "DuckExplorer"
focus = 0
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.start_color()

def handleUpKey(e):
    global focus
    focus = (focus - 1) % len(os.listdir(os.getcwd()))
    render()

def handleDownKey(e):
    global focus
    focus = (focus + 1) % len(os.listdir(os.getcwd()))
    render()

def handleRightKey(e):
    global focus
    filename = os.listdir(os.getcwd())[focus]
    if os.path.isdir(filename):
        os.chdir(filename)
        focus = focus % len(os.listdir(os.getcwd()))
        render()
    else:
        os.system(f"start {filename}")

def handleLeftKey(e):
    os.chdir("..")
    global focus
    focus = focus % len(os.listdir(os.getcwd()))
    render()

keyboard.on_release_key("up", handleUpKey)
keyboard.on_release_key("down", handleDownKey)
keyboard.on_press_key("right", handleRightKey)
keyboard.on_press_key("left", handleLeftKey)

isTypingCommand = False
typedCommand = ""

def render():
    stdscr.clear()

    stdscr.addstr(0, 0, os.getcwd(), curses.A_BOLD)

    idx = 0
    for filename in os.listdir(os.getcwd()):
        if idx <= os.get_terminal_size()[1] - 3:
            if idx == focus:
                stdscr.addstr(idx + 1, 0, filename,  curses.A_STANDOUT)
            else:
                stdscr.addstr(idx + 1, 0, filename)

        idx = idx + 1
   
    stdscr.refresh()

render()

isRunning = True

while isRunning:
    if keyboard.is_pressed("esc"):
        isRunning = FALSE

stdscr.clear()
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

os.system("cls")
print(f"\033[94mQuit {appname}.\033[0m")