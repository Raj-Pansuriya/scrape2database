import curses
import traverse
import admin as ad

# Defining an curses object
screen=curses.initscr()

# Maximum size of the terminal screen
h, w = screen.getmaxyx()



# Necessary menus
privilege_menu=("Admin","User","Exit")

admin_menu=("Add a new admin","Remove an existing admin","Traverse the database","Edit database","EXIT")
edit_menu=("Add new entry","Remove an existing entry","Change an existing entry","EXIT")

user_menu=("Traverse the database","EXIT")


def print_menu(menu,selected_row_index):
    if menu is privilege_menu:
        screen.clear()
        for index, row in enumerate(menu):
            x = w//2 - len(row)//2
            y = h//2 - len(menu)//2 + index
            if index == selected_row_index:
                screen.attron(curses.color_pair(1))
                screen.addstr(y, x, row)
                screen.attroff(curses.color_pair(1))
            elif(index==len(menu)-1):
                screen.attron(curses.color_pair(2))
                screen.addstr(y, x, row)
                screen.attroff(curses.color_pair(2))                
            else:
                screen.addstr(y, x, row)
        screen.refresh()
    else:
        screen.clear()
        for index,row in enumerate(menu):
            x=w//4-len(row)//2
            y=h//4-len(menu)//2+index
            if index == selected_row_index:
                screen.attron(curses.color_pair(1))
                screen.addstr(y, x, row)
                screen.attroff(curses.color_pair(1))
            elif(index==len(menu)-1):
                screen.attron(curses.color_pair(2))
                screen.addstr(y, x, row)
                screen.attroff(curses.color_pair(2))                
            else:
                screen.addstr(y, x, row)
        screen.refresh()

def preview(screen,text):
    x=w//4+len(text)//4
    y=10
    screen.addstr(y,x,text)
    screen.refresh

def admin_tui():
    current_row=0
    print_menu(admin_menu,current_row)
    while True:
        key=screen.getch()
        if(key == curses.KEY_UP and current_row > 0):
            current_row -= 1
        elif(key == curses.KEY_DOWN and current_row < len(admin_menu)-1):
            current_row += 1
        elif(key==curses.KEY_ENTER or key in (10,13) and current_row==0):
            screen.clear()
            screen.refresh()
            ad.add_admin()
        elif(key==curses.KEY_ENTER or key in (10,13) and current_row==1):
            ad.remove_admin()
        elif(key==curses.KEY_ENTER or key in (10,13) and current_row==2):
            pass
        elif(key == curses.KEY_ENTER or key in (10,13) and current_row==len(admin_menu)-1):
            break
        elif(key==curses.KEY_BACKSPACE):
            break
        print_menu(admin_menu,current_row)

def user_tui():
    current_row=0
    while True:
        print_menu(user_menu,current_row)
        key=screen.getch()
        if(key == curses.KEY_UP and current_row > 0):
            current_row -= 1
        elif(key == curses.KEY_DOWN and current_row < len(user_menu)-1):
            current_row += 1
        elif(key == curses.KEY_ENTER or key in (10,13) and current_row==0):
            pass
        elif(key==curses.KEY_ENTER or key in (10,13) and current_row==len(user_menu)-1):
            break
        elif(key==curses.KEY_BACKSPACE):
            break


def main(screen):
    # turn off cursor blinking
    curses.curs_set(0)

    # Color Schemes
    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    # color scheme for EXIT
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    # specify the current selected row
    current_row = 0

    while True:
        print_menu(privilege_menu,current_row)
        key=screen.getch()
        if(key == curses.KEY_UP and current_row > 0):
            current_row -= 1
        elif(key == curses.KEY_DOWN and current_row < len(privilege_menu)-1):
            current_row += 1
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row==0):
            admin_tui()
            screen.refresh
        elif(key==curses.KEY_ENTER or key in (10,13) and current_row==1):
            user_tui()
            screen.refresh()
        elif(key==curses.KEY_ENTER or key in (10,13) and current_row==2):
            break
        elif(key==curses.KEY_BACKSPACE):
            break



curses.wrapper(main)