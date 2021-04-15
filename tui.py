import curses
import traverse as tr
import admin as ad

# Defining an curses object
screen = curses.initscr()

# Maximum size of the terminal screen
h, w = screen.getmaxyx()

# Necessary menus
privilege_menu = ("Admin".center(50), "User".center(50), "Exit".center(50))

admin_menu = ("Add a new admin".ljust(50), "Remove an existing admin".ljust(
    50), "Traverse the database".ljust(50), "Edit database".ljust(50), "EXIT".ljust(50))
edit_menu = ("Add new entry".ljust(50), "Remove an existing entry".ljust(
    50), "Change an existing entry".ljust(50), "EXIT".ljust(50))

user_menu = ("Traverse the database".ljust(50), "EXIT".ljust(50))


# menu 1
menu1_list = tr.display_all("module_list")
menu1_list.append("EXIT")
menu1 = [i.ljust(30) for i in menu1_list]


# Creating 3 different windows
win1=curses.newwin(h-2,2*w//9,1,1)
win2=curses.newwin(h-2,3*w//9,1,2*w//9+1)
win3=curses.newwin(h-2,4*w//9,1,5*w//9+2)




def print_menu_center(menu, selected_row_index):
    screen.clear()
    for index, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + index
        if index == selected_row_index:
            screen.attron(curses.color_pair(1))
            screen.addstr(y, x, row)
            screen.attroff(curses.color_pair(1))
        elif(index == len(menu)-1):
            screen.attron(curses.color_pair(2))
            screen.addstr(y, x, row)
            screen.attroff(curses.color_pair(2))
        else:
            screen.addstr(y, x, row)
    screen.refresh()


def print_data_menu(win,menu, selected_row_index):
    win.clear()
    for index, row in enumerate(menu):
        y = index
        x=0
        if index == selected_row_index:
            win.attron(curses.color_pair(1))
            win.addstr(y, x, row)
            win.attroff(curses.color_pair(1))
        elif(index == len(menu)-1):
            win.attron(curses.color_pair(2))
            win.addstr(y, x, row)
            win.attroff(curses.color_pair(2))
        else:
            win.addstr(y, x, row)
    win.refresh()


def admin_tui():
    current_row = 0
    print_menu_center(admin_menu, current_row)
    while True:
        key = screen.getch()
        if(key == curses.KEY_UP and current_row > 0):
            current_row -= 1
        elif(key == curses.KEY_DOWN and current_row < len(admin_menu)-1):
            current_row += 1
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row == 0):
            screen.clear()
            screen.refresh()
            ad.add_admin()
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row == 1):
            ad.remove_admin()
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row == 2):
            pass
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row == len(admin_menu)-1):
            break
        elif(key == curses.KEY_BACKSPACE):
            break
        print_menu_center(admin_menu, current_row)


def user_tui():
    current_row = 0
    while True:
        print_menu_center(user_menu, current_row)
        key = screen.getch()
        if(key == curses.KEY_UP and current_row > 0):
            current_row -= 1
        elif(key == curses.KEY_DOWN and current_row < len(user_menu)-1):
            current_row += 1
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row == 0):
            screen.clear()
            traverse_menu1()
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row == len(user_menu)-1):
            break
        elif(key == curses.KEY_BACKSPACE):
            break


def traverse_menu1():
    menu1_current_row = 0
    while True:
        print_data_menu(win1,menu1, menu1_current_row)
        menu1_key = screen.getch()
        if(menu1_key == curses.KEY_UP and menu1_current_row > 0):
            menu1_current_row -= 1
            traverse_menu2(menu1[menu1_current_row])
        elif(menu1_key == curses.KEY_DOWN and menu1_current_row < len(menu1)-1):
            menu1_current_row += 1
            traverse_menu2(menu1[menu1_current_row])
        elif(menu1_key == curses.KEY_ENTER or menu1_key in (10, 13) and menu1_current_row == len(menu1)-1):
            break
        elif(menu1_key == curses.KEY_ENTER or menu1_key in (10, 13)):
            # win3.addstr(2,0, tr.get_by_name(menu1[menu1_current_row].strip(),table="module_list"))
            # traverse_menu2(menu1[menu1_current_row])
            # win3.refresh()
            pass
        elif(menu1_key == curses.KEY_BACKSPACE):
            break


def traverse_menu2(table_name):
    menu2_current_row = 0
    menu2_list = tr.display_all(table_name)
    menu2_list.append("EXIT")
    menu2 = [i.ljust(30) for i in menu2_list]
    print_data_menu(win2,menu2[:20],menu2_current_row)
    while True:
        print_data_menu(win2,menu2[:20], menu2_current_row)
        menu2_key = screen.getch()
        if(menu2_key == curses.KEY_UP and menu2_current_row > 0):
            menu2_current_row -= 1
            win3.clear()
            win3.addstr(0, 0, tr.get_by_name(menu2[menu2_current_row].strip(), table_name))
            win3.refresh()
        elif(menu2_key == curses.KEY_DOWN and menu2_current_row < len(menu2)-1):
            menu2_current_row += 1
            win3.clear()
            win3.addstr(0, 0, tr.get_by_name(menu2[menu2_current_row].strip(), table_name))
            win3.refresh()
        elif(menu2_key == curses.KEY_ENTER or menu2_key in (10, 13) and menu2_current_row == len(menu2)-1):
            break
        elif(menu2_key == curses.KEY_ENTER or menu2_key in (10, 13)):
            # win3.clear()
            # win3.addstr(0, 0, tr.get_by_name(menu2[menu2_current_row].strip(), table_name))
            # win3.refresh()
            pass
        elif(menu2_key == curses.KEY_BACKSPACE):
            break


def main(screen):
    # turn off cursor blinking
    curses.curs_set(0)

    # Color Schemes
    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    # color scheme for EXIT
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # color scheme for text
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # specify the current selected row
    current_row = 0

    while True:
        print_menu_center(privilege_menu, current_row)
        key = screen.getch()
        if(key == curses.KEY_UP and current_row > 0):
            current_row -= 1
        elif(key == curses.KEY_DOWN and current_row < len(privilege_menu)-1):
            current_row += 1
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row == 0):
            admin_tui()
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row == 1):
            user_tui()
        elif(key == curses.KEY_ENTER or key in (10, 13) and current_row == 2):
            break
        elif(key == curses.KEY_BACKSPACE):
            break


curses.wrapper(main)
