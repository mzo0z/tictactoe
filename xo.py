#################################
# this game coded by @mzo0z     #
# https://discord.gg/3psKD4pH4G #
# https://github.com/mzo0z      #
#################################

import random
import webbrowser as web
import os
from tkinter import *
from tkinter import messagebox as msg

def mzo0z(server, invite):
    HEADER    = '\033[96m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    YELLOW    = '\033[93m'
    icon = f"""
======================================================================================
   {OKGREEN}\__\\                   \__\\ {ENDC}      {BOLD}{HEADER}github{ENDC}
   {OKGREEN} \  \\[*]             [*]\  \\ {ENDC}      └──{OKBLUE}https://github.com/mzo0z{ENDC}
   {OKGREEN}  \  \\  [*]         [*]  \  \\ {ENDC}    {BOLD}{HEADER}discord{ENDC}
   {OKGREEN}   \  \\   [*]      [*]    \  \\ {ENDC}    └──{OKBLUE}{server}{ENDC}
   {OKGREEN}    \  \\    [*]   [*]      \  \\ {ENDC}  {BOLD}{HEADER}insta{ENDC}
   {OKGREEN}     \  \\      [*]          \  \\ {ENDC}  └──{OKBLUE}https://instagram.com/mzo0z{ENDC}
   {OKGREEN}      \  \\                   \  \\ {ENDC}
   {OKGREEN}       \  \\{ENDC} {YELLOW}[>>tic tac toe<<]{ENDC} {OKGREEN}\  \\{ENDC}
   {OKGREEN}      __\__\\__               __\__\\__ {ENDC}

    {BOLD}{HEADER}bot invite{ENDC}
     └──{OKBLUE}{invite}{ENDC}
======================================================================================
"""
    return icon
os.system('cls' if os.name == 'nt' else 'clear')
print(mzo0z('https://discord.gg/3psKD4pH4G', f"https://discord.com/api/oauth2/authorize?client_id=901111890300796938&permissions=8&scope=bot%20applications.commands"))

tk = Tk()
tk.geometry("500x500")
tk.title("tic tac toe (main screen)")
tk.configure(bg='#212534')
tk.resizable(False, False)
player_name = "player1"
session_started = False
something_running = False
kill_program = False
games_points = {player_name:0}
def hover(button):
    button.bind("<Enter>", func=lambda e: button.config(bg="#212534", fg="gray"))
    button.bind("<Leave>", func=lambda e: button.config(bg="#343A40", fg="white"))


class vs_friend:
    def __init__(self, player_name):
        self.bt = Tk()
        self.bt.resizable(0,0)
        self.bt.title("tic tac toe")
        self.player = random.choice(["X", "O"])
        self.players = {"X":player_name, "O":"player2"}
        self.player_pos = {'X':[], 'O':[]}
        self.kill = False
        self.buttons = [[0,0,0],[0,0,0],[0,0,0]]
        self.states  = [[0,0,0],[0,0,0],[0,0,0]]
        self.values  = [' ' for x in range(9)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.bt, height=5, width=10, font=("Helvetica","20"), command=lambda x = i, y = j : self.place_selected(x, y))
                self.buttons[i][j].grid(row = i, column = j)
        self.bt.bind("<Destroy>", self.on_destroy)
        msg.showinfo("tic tac toe", f"{self.players[self.player]} tern")

    def on_destroy(self, event):
        if event.widget.winfo_parent() == "":
            global something_running
            something_running = False
            self.kill = True

    def place_selected(self, x, y):
        if self.kill:return
        if self.states[x][y] == 0:
            self.buttons[x][y].configure(text = self.player)
            self.states[x][y] = self.player
            move = self.con_xy_num(x, y)
            self.values[move-1] = self.player
            self.player_pos[self.player].append(move)
            if self.check_to_end():return
            if self.player=='X':self.player="O"
            elif self.player=='O':self.player="X"

    def con_xy_num(self, x, y):
        if [x, y] == [0,0]:num =1
        elif [x, y] == [0,1]:num =2
        elif [x, y] == [0,2]:num =3
        elif [x, y] == [1,0]:num =4
        elif [x, y] == [1,1]:num =5
        elif [x, y] == [1,2]:num =6
        elif [x, y] == [2,0]:num =7
        elif [x, y] == [2,1]:num =8
        elif [x, y] == [2,2]:num =9
        return num


    def check_to_end(self):
        if self.player.lower()=='x':player_xo='O'
        if self.player.lower()=='o':player_xo='X'
        if self.check_win(self.player_pos, player_xo):
            msg.showinfo(f"tic tac toe", f"winner {player_xo}!")
            games_points[self.players[player_xo]]+=1
            update_score()
            self.kill=True

        if self.check_win(self.player_pos, self.player):
            msg.showinfo(f"tic tac toe", f"winner {self.player}!")
            games_points[self.players[self.player]]+=1
            update_score()
            self.kill=True

        if self.check_draw(self.player_pos):
            msg.showinfo(f"tic tac toe", f"draw")
            self.kill=True
        return False

    def check_win(self, pos, player):
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for x in soln:
            if all(y in pos[player] for y in x):return True
        return False    

    def check_draw(self, player_pos):
        if len(player_pos['X']) + len(player_pos['O']) == 9:return True
        return False

def shows_error():
    yesno = msg.askyesno('tic tac toe', "this feature doesn't work here. you must download the game to open this feautrue.\ndo you want to download it?")
    if yesno:
        web.open('https://github.com/mzo0z/xo')

def v_friend():
    global player_name
    global games_points
    global something_running
    if not something_running:
        something_running = True
        if player_name == 'player2':player_name='player1'
        if 'bot' in games_points:del games_points['bot'];games_points[player_name] = 0;games_points['player2'] = 0
        if player_name not in games_points:games_points[player_name] = 0
        if 'player2'   not in games_points:games_points['player2'] = 0
        update_score()
        vs_friend(player_name)
        print("[!] game started with friend")
    else:
        msg.showerror('tic tac toe', 'tern off the first window!')

def update_score():
    text = ""
    for name in games_points.keys():
        text +=f"{name} : {games_points[name]}\n"
    points.configure(text=text)

def reset():
    global games_points
    if 'bot' in games_points:del games_points['bot']
    if 'player2' in games_points:del games_points['player2']
    if player_name in games_points:games_points[player_name] = 0
    update_score()

def save_name():
    global player_name
    old_points = games_points[player_name]
    games_points.pop(player_name)
    player_name = name.get()
    games_points[player_name] = old_points
    update_score()
    msg.showinfo("tic tac toe", f"name saved {player_name}")

def kill_all(event):
    global session_started
    global something_running
    global server
    global kill_program
    if event.widget.winfo_parent() == "":
        if session_started:server.close()
        kill_program = True
        session_started = False
        something_running = True
        exit()
tk.bind("<Destroy>", kill_all)

Label(tk, text="welcome to tic tac", fg='white', bg="#212534", font="times 25" ).place(x=120, y=20)
Label(tk, text="discord.gg/3psKD4pH4G", fg='white', bg="#212534", font="times 25" ).place(x=75, y=450)

b1 =Button(tk, text="play with bot", width=15, font="times 15", fg='white', bg="#343A40", bd=1, command=shows_error)
b1.place(x=50, y=125)
hover(b1)
b2 =Button(tk, text="play with friend", width=15, font="times 15", fg='white', bg="#343A40", bd=1, command=v_friend)
b2.place(x=250, y=125)
hover(b2)
b3 =Button(tk, text="create session", width=15, font="times 15", fg='white', bg="#343A40", bd=1, command=shows_error)
b3.place(x=50, y=200)
hover(b3)
b4 = Button(tk, text="join session", width=15, font="times 15", fg='white', bg="#343A40", bd=1, command=shows_error)
b4.place(x=250, y=200)
hover(b4)
Label(tk, text="enter your name", fg='white', bg="#212534", font="times 25" ).place(x=60, y=245)
name = Entry(tk, width=15, font="times 15")
name.place(x=50, y=280)
b5 = Button(tk, text="save", width=5, font="times 12", fg='white', bg="#343A40", bd=1, command=save_name)
b5.place(x=220, y=280)
hover(b5)
b6 = Button(tk, text="reset", width=10, font="times 12", fg='white', bg="#343A40", bd=1, command=reset)
b6.place(x=300, y=280)
hover(b6)

points = Label(tk, text=f"{player_name} : {games_points[player_name]}", fg='white', bg="#212534", font="times 25" )
points.place(x=50, y=320)


tk.mainloop()


