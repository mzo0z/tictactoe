#############################
# this game coded by @mzo0z #
# https://github.com/mzo0z  #
#############################

import random
import socket
import threading
import pyperclip
import pickle
import os
from tkinter import *
from tkinter import messagebox as msg
import sys

import pygame

def colors(msg, color):
    black=f'\033[30m{msg}\033[0;0m'
    red=f'\033[31m{msg}\033[0;0m'
    green=f'\033[32m{msg}\033[0;0m'
    orange=f'\033[33m{msg}\033[0;0m'
    blue=f'\033[34m{msg}\033[0;0m'
    purple=f'\033[35m{msg}\033[0;0m'
    cyan=f'\033[36m{msg}\033[0;0m'
    lightgrey=f'\033[37m{msg}\033[0;0m'
    darkgrey=f'\033[90m{msg}\033[0;0m'
    lightred=f'\033[91m{msg}\033[0;0m'
    lightgreen=f'\033[92m{msg}\033[0;0m'
    yellow=f'\033[93m{msg}\033[0;0m'
    lightblue=f'\033[94m{msg}\033[0;0m'
    pink=f'\033[95m{msg}\033[0;0m'
    lightcyan=f'\033[96m{msg}\033[0;0m'
    toReturn = {
        'black'      : black,
        'red'        : red,
        'green'      : green,
        'orange'     : orange,
        'blue'       : blue,
        'cyan'       : cyan,
        'purple'     : purple,
        'lightgrey'  : lightgrey,
        'darkgrey'   : darkgrey,
        'lightred'   : lightred,
        'lightgreen' : lightgreen,
        'yellow'     : yellow,
        'lightblue'  :lightblue,
        'pink'       :pink,
        'lightcyan'  :lightcyan}
    return toReturn[color]


os.system('cls' if os.name == 'nt' else 'clear')
print(colors("[!]", "red") + colors(" to close all windows just close this window", "yellow"))
print(colors("[*]", "blue") + colors(" app is running", "yellow"))
tk = Tk()
tk.geometry("500x500")
tk.title("tic tac toe (main screen)")
tk.configure(bg='#212534')
tk.resizable(False, False)
player_name = "player1"
running_game = ""
running_game_class = None
session_started = False
something_running = False
kill_program = False
games_points = {player_name:0}
lang = "en"
language = "العربية"
RED = "#952514"
b7 = None
detail=None
kill_pygame = False
def hover(button):
    button.bind("<Enter>", func=lambda e: button.config(bg="#212534", fg="gray"))
    button.bind("<Leave>", func=lambda e: button.config(bg="#343A40", fg="white"))

def hover2(button):
    button.bind("<Enter>", func=lambda e: button.config(bg="#212534", fg="gray"))
    button.bind("<Leave>", func=lambda e: button.config(bg=RED, fg="white"))

def texts(type):
    global lang
    global language
    if lang=='ar':
        data = {
            "wlc":"tic tac مرحبا بك في لعبة",
            "b1":"لعب ضد كمبيوتر",
            "b2":"لعب ضد صديق",
            "b3":"إنشاء جلسة",
            "b4":"إنضمام لجلسة",
            "urn":"ادخل اسمك",
            "b5":"حفظ",
            "b6":"إعادة تعيين",
            "b8":"English",
            "winner":"الفائز",
            "draw":"تعادل",
            "openedPage":"يوجد لعبة شغالة, اطفئها اولا",
            "stopServerF":'يجب إطفاء السيرفر اولا',
            "join":"إنضمام",
            "tern":"دور",
            "duwl":"هل تريد الخروج من السيرفر؟",
            "scbh":'تم اغلاق السيرفر من قبل المضيف!',
            "gcbh":"تم إطفاء اللعبة من قبل المضيف",
            "leaveS":"الخروج من السيرفر",
            "ewcts":"حدث خطأ اثناء الاتصال على هذا السيرفر الرجاء المحاولة مرة اخرى",
            "left":"خرج من اللعبة",
            "notpw":'لايوجد شخص يتم اللعب معه!',
            "copied":"تم النسخ",
            "copy":"نسخ",
            "dctp":"\nلاتطفئ هذه الصفحة إلا بعد الانتهاء",
            "startG":"بدأ اللعبة",
            "wuf":'بإنتظار إنضمام صديقك',
            "savedN":"تم حفط الاسم",
            "cantmt10":"لايمكن اختيار اسم اكثر من 10 حروف",
        }
    elif lang=='en':
        data = {
            "wlc":"welcome to tic tac toe",
            "b1":"play with pc",
            "b2":"play with friend",
            "b3":"create session",
            "b4":"join session",
            "urn":"enter your name",
            "b5":"save",
            "b6":"reset",
            "b8":"العربية",
            "winner":"winner",
            "draw":"draw",
            "openedPage":"there is working game close it first",
            "stopServerF":"you must stop the server first",
            "join":"join",
            "tern":"tern",
            "duwl":"do you want to leave the server?",
            "scbh":"server closed by the host!",
            "gcbh":"game stoped by the host",
            "leaveS":"leave server",
            "ewcts":"An error occurred while connecting to this server. Please try again.",
            "left":"left the game",
            "notpw":"there is no one to play with!",
            "copied":"copied",
            "copy":"copy",
            "dctp":"\ndon't close this page except after finish",
            "startG":"start game",
            "wuf":"waiting for your friend",
            "savedN":"saved",
            "cantmt10":"can't write name more than 10 letters",

        }
    return data[type]

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

    def destroy(self):
        global something_running
        something_running = False
        self.kill = True
        self.bt.destroy()

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
            print(colors("[&&]", "cyan") + colors(f" {self.player} place is [{x}, {y}]", "yellow"))
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
            games_points[self.players[player_xo]]+=1
            print(colors("[*]", "green") + colors(f" {player_xo} is the winner!", "yellow"))
            update_score()
            self.kill=True
            msg.showinfo(f"tic tac toe", f"{texts('winner')} {player_xo}!")

        if self.check_win(self.player_pos, self.player):
            games_points[self.players[self.player]]+=1
            print(colors("[*]", "green") + colors(f" {self.player} is the winner!", "yellow"))
            update_score()
            self.kill=True
            msg.showinfo(f"tic tac toe", f"{texts('winner')} {self.player}!")

        if self.check_draw(self.player_pos):
            print(colors("[!!]", "cyan") + colors(f" no winner!", "yellow"))
            self.kill=True
            msg.showinfo(f"tic tac toe", texts('draw'))
        return False

    def check_win(self, pos, player):
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for x in soln:
            if all(y in pos[player] for y in x):return True
        return False    

    def check_draw(self, player_pos):
        if len(player_pos['X']) + len(player_pos['O']) == 9:return True
        return False

class vs_AI:
    def __init__(self, player_name):
        self.bt = Tk()
        self.bt.resizable(0,0)
        self.bt.title("tic tac toe")
        self.player = "O"
        self.players = {"X":player_name, "O":"bot"}
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
        self.AI_tern()

    def destroy(self):
        global something_running
        something_running = False
        self.kill = True
        self.bt.destroy()

    def place_selected(self, x, y):
        if self.kill:return
        if self.players[self.player].lower() != "bot":
            if self.states[x][y] == 0:
                self.buttons[x][y].configure(text = self.player)
                self.states[x][y] = self.player
                move = self.con_xy_num(x, y)
                self.values[move-1] = self.player
                self.player_pos[self.player].append(move)
                print(colors("[&&]", "cyan") + colors(f" {self.player} place is [{x}, {y}]", "yellow"))
                if self.check_to_end():return
                if self.player=='X':self.player="O"
                elif self.player=='O':self.player="X"
                self.AI_tern()

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

    def con_num_xy(self, num):
        if   num == 1: xy=[0,0]
        elif num == 2: xy=[0,1]
        elif num == 3: xy=[0,2]
        elif num == 4: xy=[1,0]
        elif num == 5: xy=[1,1]
        elif num == 6: xy=[1,2]
        elif num == 7: xy=[2,0]
        elif num == 8: xy=[2,1]
        elif num == 9: xy=[2,2]
        return xy

    def on_destroy(self, event):
        if event.widget.winfo_parent() == "":
            global something_running
            something_running = False
            self.kill = True

    def check_to_end(self):
        if self.player.lower()=='x':player_xo='O'
        if self.player.lower()=='o':player_xo='X'
        if self.check_win(self.player_pos, player_xo):
            games_points[self.players[player_xo]]+=1
            update_score()
            self.kill = True
            print(colors("[*]", "green") + colors(f" {player_xo} is the winner!", "yellow"))
            msg.showinfo(f"tic tac toe", f"{texts('winner')} {player_xo}!")
            return self.kill

        if self.check_win(self.player_pos, self.player):
            games_points[self.players[self.player]]+=1
            update_score()
            self.kill = True
            print(colors("[*]", "green") + colors(f" {self.player} is the winner!", "yellow"))
            msg.showinfo(f"tic tac toe", f"{texts('winner')} {self.player}!")
            return self.kill

        if self.check_draw(self.player_pos):
            self.kill = True
            print(colors("[!!]", "cyan") + colors(f" no winner!", "yellow"))
            msg.showinfo(f"tic tac toe", texts('draw'))
            return self.kill
        return False

    def check_win(self, pos, player):
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for x in soln:
            if all(y in pos[player] for y in x):return True
        return False    

    def check_draw(self, player_pos):
        if len(player_pos['X']) + len(player_pos['O']) == 9:return True
        return False

    def get_empty_places(self):
        emptys = []
        if self.values[0] == ' ':emptys.append(1)
        if self.values[1] == ' ':emptys.append(2)
        if self.values[2] == ' ':emptys.append(3)
        if self.values[3] == ' ':emptys.append(4)
        if self.values[4] == ' ':emptys.append(5)
        if self.values[5] == ' ':emptys.append(6)
        if self.values[6] == ' ':emptys.append(7)
        if self.values[7] == ' ':emptys.append(8)
        if self.values[8] == ' ':emptys.append(9)
        return emptys

    def AI_tern(self):
        if self.kill:return
        if self.players[self.player].lower() != "bot":return
        if self.player.lower()=='x':player_xo='O'
        if self.player.lower()=='o':player_xo='X'
        if len([i for i in self.values if i==' '])==9:coordinates=self.con_num_xy(random.randint(1, 9))
        elif len([i for i in self.values if i==' '])==7:coordinates=self.con_num_xy(random.choice(self.get_empty_places()))
        else:
            me = [i for i in self.player_pos[self.player]]
            vs = [i for i in self.player_pos[player_xo]]
            wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
            ws   = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
            options = ["X", "O"]
            for option in options:
                for x in wins:
                    for i in x:
                        if i in self.player_pos[option] or self.values[i-1] != ' ':x.remove(i)
            def try_to_win(wins:list, points:list):
                will_win = False
                for x in wins:
                    for _move in x:
                        if self.values[_move-1] != ' ':x.remove(_move)
                        else:
                            points.append(_move)
                            for row in ws:
                                if all(y in points for y in row):
                                    will_win=True
                                    break
                            points.remove(_move)
                            if will_win:break
                    if will_win:break
                return _move
            def will_i_when(points:list):
                for num in range(1, 9):
                    if self.values[num-1] == ' ':
                        points.append(num)
                        for row in ws:
                            if all(y in points for y in row):
                                return True, num
                        points.remove(num)
                return False, num
            i_win = try_to_win(wins, me)
            he_win = try_to_win(wins, vs)
            if i_win==he_win:coordinates=self.con_num_xy(i_win)
            else:
                iam = will_i_when(me)
                hes = will_i_when(vs)
                if iam[0]:coordinates=  self.con_num_xy(iam[1])
                elif hes[0]:coordinates=self.con_num_xy(hes[1])
                else:coordinates=self.con_num_xy(he_win)
        
        self.values[self.con_xy_num(coordinates[0], coordinates[1])-1] = self.player
        self.player_pos[self.player].append(self.con_xy_num(coordinates[0], coordinates[1]))
        self.buttons[coordinates[0]][coordinates[1]].configure(text = self.player)
        self.states[coordinates[0]][coordinates[1]] = self.player
        print(colors("[&&]", "cyan") + colors(f" {self.player} place is {coordinates}", "yellow"))
        if self.check_to_end():return
        if self.player=='X':self.player="O"
        elif self.player=='O':self.player="X"

class join_session:
    def __init__(self):
        global session_started
        global something_running
        if not session_started:
            if not something_running:
                something_running = True
                self.kill_loops = False
                self.game_started = False
                self.data={}
                self.session = Tk()
                self.session.geometry("350x200")
                self.session.configure(bg='#212534')
                self.session.resizable(False, False)
                self.session.title("tic tac toe")
                self.session.bind("<Destroy>", self.session_destroy)
                self.make_things()
            else:msg.showerror('tic tac toe', texts("openedPage"))
        else:msg.showerror('tic tac toe', texts("stopServerF"))

    def make_things(self):
        Label(self.session, text="your name", fg='white', bg="#212534", font="times 15" ).place(x=20, y=20)
        self.get_name = Entry(self.session, width=15, font="times 15")
        self.get_name.place(x=110, y=20)
        Label(self.session, text="IP", fg='white', bg="#212534", font="times 15" ).place(x=20, y=50)
        self.get_ip = Entry(self.session, width=15, font="times 15")
        self.get_ip.place(x=80, y=50)
        Label(self.session, text="PORT", fg='white', bg="#212534", font="times 15" ).place(x=20, y=80)
        self.get_port = Entry(self.session, width=5, font="times 15")
        self.get_port.place(x=80, y=80)
        self.joingame = Button(self.session, text=texts("join"), width=25, font="times 12", fg='white', bg="#343A40", bd=1, command=self.join_game)
        self.joingame.place(x=20, y=120)
        hover(self.joingame)


    def start_game(self):
        self.game = Toplevel()
        self.game.resizable(0,0)
        self.someone_win = False
        self.game.title(f"{self.host}'s tic tac toe. ({self.players[self.player]} {texts('tern')})")
        self.player_pos = {'X':[], 'O':[]}
        self.buttons = [[0,0,0],[0,0,0],[0,0,0]]
        self.states  = [[0,0,0],[0,0,0],[0,0,0]]
        self.values  = [' ' for x in range(9)]
        self.game_started = True
        self.kill_loops=False
        self.killed_server = False
        update_score()
        threading.Thread(target=self.get_data_from_server).start()
        threading.Thread(target=self.update_game).start()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.game, height=5, width=10, font=("Helvetica","20"), command=lambda x = i, y = j : self.place_selected(x, y))
                self.buttons[i][j].grid(row = i, column = j)
        tk.wait_window(self.game)
        self.data['kill']=True
        self.server.send(pickle.dumps(self.data))
        self.kill_loops = True
        print(colors("[*]", "blue") + colors(f" started game!", "yellow"))
        leave_server = msg.askyesno(f"{self.host}'s tic tac toe", texts("duwl"))
        if leave_server:
            print(colors("[-]", "red") + colors(f" you have left the session!", "yellow"))
            try:self.server.close()
            except:pass
            global something_running
            global session_started
            something_running = False
            session_started = False
            self.b7.destroy()


    def session_destroy(self, event):
        if event.widget.winfo_parent() == "":
            global something_running
            something_running = False

    def update_game(self):
        while True:
            global kill_program
            if self.kill_loops or self.killed_server or kill_program or self.someone_win:break
            if self.player.lower() == 'x':
                try:
                    x = self.data['x']
                    y = self.data['y']
                    if self.states[x][y] == 0:
                        self.buttons[x][y].configure(text = self.player)
                        self.states[x][y] = self.player
                        move = self.con_xy_num(x, y)
                        self.values[move-1] = self.player
                        self.player_pos[self.player].append(move)
                        if self.check_to_end():return
                        if self.player=='X':self.player="O"
                        elif self.player=='O':self.player="X"
                        self.game.title(f"{self.host}'s tic tac toe. ({self.players[self.player]} {texts('tern')})")
                        print(colors("[##]", "blue") + colors(f" {self.player} place is [{x}, {y}]!", "yellow"))
                except:pass


    def place_selected(self, x, y):
        if self.someone_win:return
        if self.player.lower() == 'o':
            if self.states[x][y] == 0:
                self.buttons[x][y].configure(text = self.player)
                self.states[x][y] = self.player
                move = self.con_xy_num(x, y)
                self.values[move-1] = self.player
                self.player_pos[self.player].append(move)
                self.data['x']=x
                self.data['y']=y
                self.server.send(pickle.dumps(self.data))
                if self.check_to_end():return
                if self.player=='X':self.player="O"
                elif self.player=='O':self.player="X"
                self.game.title(f"{self.host}'s tic tac toe. ({self.players[self.player]} {texts('tern')})")
                print(colors("[##]", "blue") + colors(f" {self.player} place is [{x}, {y}]!", "yellow"))


    def get_main_data_from_server(self):
        try:
            global games_points
            data = pickle.loads(self.server.recv(1024*4))
            games_points    = data["games_points"]
            self.players    = data["players"]
            self.player    = data["player"]
            self.data['kill'] = data['kill']
            self.data['new_game'] = data['new_game']
            update_score()
            self.start_game()
        except:pass

    def get_data_from_server(self):
        while True:
            global kill_program
            if kill_program or self.killed_server :return
            try:
                data = pickle.loads(self.server.recv(1024*4))
                print(colors("[+]", "green") + colors(f" data has been recveived", "yellow"))
                if data == 'killed_server':
                    try:self.server.close()
                    except:pass
                    self.game.destroy()
                    msg.showerror(f"{self.host}'s tic tac toe.", texts("scbh"))
                    self.killed_server = True
                    self.kill_loops = True
                elif data == 'stop_game':
                    self.game.destroy()
                    msg.showerror(f"{self.host}'s tic tac toe.", texts("gcbh"))
                    self.kill_loops = True
                elif data['new_game']:
                    self.data={}
                    global games_points
                    games_points    = data["games_points"]
                    self.players    = data["players"]
                    self.player    = data["player"]
                    self.data['kill'] = data['kill']
                    self.data['new_game'] = data['new_game']
                    update_score()
                    self.start_game()
                else:
                    try:data['kill'] = self.data['kill']
                    except:pass
                    self.data=data
            except:pass

    def leave_server(self):
        try:
            self.data['kill']=True
            self.server.send(pickle.dumps(self.data))
            self.kill_loops = True
            try:self.server.close()
            except:pass
            global something_running
            global session_started
            something_running = False
            session_started = False
            self.b7.destroy()
        except:pass

    def join_game(self):
        global games_points
        ip = self.get_ip.get()
        port = self.get_port.get()
        self.host = ip
        self.server = socket.socket()
        try:
            global b7
            self.server.connect((ip, int(port)))
            self.server.send(self.get_name.get().encode())
            self.b7 = Button(tk, text=texts("leaveS"), width=10, font="times 12", fg='white', bg=RED, bd=1, command=self.leave_server)
            self.b7.place(x=200, y=320)
            b7 = self.b7
            hover2(self.b7)
            global something_running
            global session_started
            something_running = True
            session_started = True
            self.session.withdraw()
            threading.Thread(target=self.get_main_data_from_server).start()
            print(colors("[*]", "green") + colors(f" connected to the server!", "yellow"))
        except:
            print(colors("[-]", "red") + colors(f" can't connect to this server", "yellow"))
            msg.showerror(f"{self.host}'s tic tac toe.", texts("ewcts"))

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

    def on_destroy(self, event):
        if event.widget.winfo_parent() == "":
            global something_running
            something_running = False
            self.kill = True

    def check_to_end(self):
        if self.player.lower()=='x':player_xo='O'
        if self.player.lower()=='o':player_xo='X'
        if self.check_win(self.player_pos, player_xo):
            games_points[self.players[player_xo]]+=1
            update_score()
            self.someone_win = True
            print(colors("[*]", "green") + colors(f" {self.players[player_xo]} is the winner!", "yellow"))
            msg.showinfo(f"{self.host}'s tic tac toe.", f"{texts('winner')} {self.players[player_xo]}!")

        if self.check_win(self.player_pos, self.player):
            games_points[self.players[self.player]]+=1
            update_score()
            self.someone_win = True
            print(colors("[*]", "green") + colors(f" {self.players[self.player]} is the winner!", "yellow"))
            msg.showinfo(f"{self.host}'s tic tac toe.", f"{texts('winner')} {self.players[self.player]}!")

        if self.check_draw(self.player_pos):
            self.someone_win = True
            print(colors("[!!]", "cyan") + colors(f" there is no winner!", "yellow"))
            msg.showinfo(f"{self.host}'s tic tac toe.", texts("draw"))
        return False

    def check_win(self, pos, player):
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for x in soln:
            if all(y in pos[player] for y in x):return True
        return False    

    def check_draw(self, player_pos):
        if len(player_pos['X']) + len(player_pos['O']) == 9:return True
        return False

class create_session:
    def __init__(self):
        global session_started
        global server
        global games_points
        global something_running
        if not session_started:
            if not something_running:
                something_running = True
                games_points ={}
                self.server = self.build_server()
                server = self.server
                self.server.listen(1)
                threading.Thread(target=self.accept_player).start()
                self.ready_to_play   = False
                self.already_playing = False
                self.alone = False
                self.new_game=False
                games_points[player_name]=0
                self.session = Tk()
                self.session.geometry("315x200")
                self.session.configure(bg='#212534')
                self.session.resizable(False, False)
                self.session.title("tic tac toe")
                self.session.bind("<Destroy>", self.session_destroy)
                self.make_things()

            else:msg.showerror("tic tac toe", texts('openedPage'))
        else:msg.showerror("tic tac toe", texts("stopServerF"))

    def start_game(self, player2_name):
        self.ready_to_play   = False
        self.already_playing = True
        self.someone_win = False
        self.game = Tk()
        self.game.resizable(0,0)
        self.player = random.choice(["X", "O"])
        self.player2_name = player2_name
        if self.player2_name not in games_points:games_points[self.player2_name]=0
        self.game.title(f"tic tac toe. ({self.players[self.player]} {texts('tern')})")
        self.player_pos = {'X':[], 'O':[]}
        self.kill = False
        self.kill_loops = False
        self.buttons = [[0,0,0],[0,0,0],[0,0,0]]
        self.states  = [[0,0,0],[0,0,0],[0,0,0]]
        self.values  = [' ' for x in range(9)]
        self.data_received = {}


        threading.Thread(target=self.send_data).start()
        if self.alone:return
        else:
            update_score()
            threading.Thread(target=self.update_game).start()
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j] = Button(self.game, height=5, width=10, font=("Helvetica","20"), command=lambda x = i, y = j : self.place_selected(x, y))
                    self.buttons[i][j].grid(row = i, column = j)
            self.game.bind("<Destroy>", self.Destroy)
            self.game.mainloop()

    def receiving(self):
        while True:
            global kill_program
            try:
                if self.alone or self.kill_server or kill_program:break
                self.data_received = pickle.loads(self.client.recv(1024*4))
                print(colors("[+]", "blue") + colors(f" data has been recveived!", "yellow"))
                if self.data_received['kill']:
                    print(colors("[-]", "red") + colors(f" killed server", "yellow"))
                    self.ready_to_play=True
                    self.kill_loops = True
                    try:self.game.destroy()
                    except:pass
                    msg.showerror('tic tac toe', f'{self.players["O"]} {texts("left")}')
            except ConnectionResetError:
                self.ready_to_play=True
                self.kill_loops = True
                self.alone=True
                try:self.game.destroy()
                except:pass
                print(colors("[-]", "red") + colors(f" killed server", "yellow"))
                msg.showerror('tic tac toe', f'{self.players["O"]} {texts("left")}')


    def update_game(self):
        while True:
            global kill_program
            if kill_program or self.kill or self.someone_win or self.alone or self.kill_server or self.kill_loops:return
            if self.player.lower() == 'o':
                try:
                    x = self.data_received['x']
                    y = self.data_received['y']
                    if self.states[x][y] == 0:
                        self.buttons[x][y].configure(text = self.player)
                        self.states[x][y] = self.player
                        move = self.con_xy_num(x, y)
                        self.values[move-1] = self.player
                        self.player_pos[self.player].append(move)
                        print(colors("[&&]", "cyan") + colors(f" {self.player} place is [{x}, {y}]", "yellow"))
                        if self.check_to_end():return
                        if self.player=='X':self.player="O"
                        elif self.player=='O':self.player="X"
                        self.game.title(f"tic tac toe. ({self.players[self.player]} {texts('tern')})")
                except:pass

    def place_selected(self, x, y):
        if self.kill or self.kill_loops or self.someone_win:return
        if self.player.lower() == 'x':
            if self.states[x][y] == 0:
                self.buttons[x][y].configure(text = self.player)
                self.states[x][y] = self.player
                move = self.con_xy_num(x, y)
                self.values[move-1] = self.player
                self.player_pos[self.player].append(move)
                self.data_received['x']=x
                self.data_received['y']=y
                self.data_received['new_game']=self.new_game
                print(colors("[&&]", "cyan") + colors(f" {self.player} place is [{x}, {y}]", "yellow"))
                try:self.client.send(pickle.dumps(self.data_received))
                except:
                    self.game.destroy()
                    print(colors("[-]", "red") + colors(f" you are alone!", "yellow"))
                    msg.showerror('tic tac toe', texts("notpw"))
                    return
                if self.check_to_end():return
                if self.player=='X':self.player="O"
                elif self.player=='O':self.player="X"
                self.game.title(f"tic tac toe. ({self.players[self.player]} {texts('tern')})")

    def send_data(self):
        data = {}
        data["games_points"]=games_points
        data["players"]=self.players
        data["player"]=self.player
        data['kill']=False
        data['new_game']=self.new_game
        if self.new_game:self.new_game=False
        data = pickle.dumps(data)
        try:self.client.send(data);print(colors("[+]", "green") + colors(f" data has benn sent!", "yellow"))
        except ConnectionResetError:
            self.game.destroy()
            self.alone = True
            print(colors("[-]", "red") + colors(f" you are alone!", "yellow"))
            msg.showerror('tic tac toe', texts("notpw"))

    def copy_ip(self):
        pyperclip.copy(self.host)
        self.copyip.configure(bg='green', text=texts("copied"))
        print(colors("[@]", "cyan") + colors(f" ip has been copied!", "yellow"))

    def make_things(self):
        global session_started
        session_started = True
        Label(self.session, text=f"ip:{self.host}\nport:{self.port}",font="times 20", fg='white', bg="#212534").place(x=20, y=30)
        self.copyip = Button(self.session, text=texts("copy"), width=5, font="times 12", fg='white', bg="#343A40", bd=1, command=self.copy_ip)
        self.copyip.place(x=250, y=30)
        hover(self.copyip)
        Label(self.session, text=texts("dctp"),font="times 15", fg='white', bg="#212534").place(x=20, y=100)
        self.run_game_b = Button(self.session, text=texts("startG"),font="times 15", fg='white', bg="#343A40", command=self.run_game)
        self.run_game_b.place(x=75, y=150)
        hover(self.run_game_b)
        self.session.bind("<Destroy>", self.on_destroy)

    def run_game(self):
        if self.ready_to_play:
            if self.alone:msg.showerror('tic tac toe', texts("notpw"));return
            else:self.start_game(self.player2_name)
        elif self.already_playing:
            print(colors("[!]", "red") + colors(f" close the other windows!", "yellow"))
            msg.showerror('tic tac toe', texts("openedPage"))
        else:
            print(colors("[!]", "red") + colors(f" waiting for your friend!", "yellow"))
            msg.showerror('tic tac toe', texts("wuf"))

    def build_server(self):
        ipv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ipv4.connect(("8.8.8.8", 80))
        self.host = ipv4.getsockname()[0]
        self.kill_server = False
        ipv4.close()
        server = socket.socket()
        for self.port in range(1000, 9999):
            try:server.bind((self.host, self.port));break
            except:pass
        return server

    def accept_player(self):
        while True:
            global kill_program
            if kill_program:break
            if self.kill_server:break
            print(colors("[++]", "blue") + colors(f" listening...", "yellow"))
            try:
                self.client, self.address = self.server.accept()
                self.player2_name = self.client.recv(1024).decode()
                if self.player2_name.lower() == player_name.lower():self.player2_name = str(self.address[0])
                self.players = {"X":player_name, "O":self.player2_name}
                threading.Thread(target=self.receiving).start()
                self.ready_to_play = True
                print(colors("[*]", "green") + colors(f" {self.address[0]} connected!", "yellow"))
                msg.showinfo('tic tac toe', f"{self.address[0]} joined!")
                return
            except:pass
 
    def session_destroy(self, event):
        global something_running
        if event.widget.winfo_parent() == "":
            something_running = False


    def Destroy(self, event):
        if event.widget.winfo_parent() == "":
            self.client.send(pickle.dumps("stop_game"))
            self.ready_to_play   = True
            self.already_playing = False
            self.kill = True

    def on_destroy(self, event):
        if event.widget.winfo_parent() == "":
            global something_running
            global session_started
            try:self.client.send(pickle.dumps("killed_server"))
            except:pass
            session_started = False
            something_running = False
            self.kill_server = True
            self.kill = True
            self.server.close()
            print(colors("[--]", "red") + colors(f" server closed!", "yellow"))



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
            games_points[self.players[player_xo]]+=1
            update_score()
            self.new_game=True
            self.someone_win = True
            print(colors("[*]", "green") + colors(f" {self.players[player_xo]} is the winner!", "yellow"))
            msg.showinfo(f"tic tac toe", f"{texts('winner')} {self.players[player_xo]}!")

        if self.check_win(self.player_pos, self.player):
            games_points[self.players[self.player]]+=1
            update_score()
            self.new_game=True
            self.someone_win = True
            print(colors("[*]", "green") + colors(f" {self.players[self.player]} is the winner!", "yellow"))
            msg.showinfo(f"tic tac toe", f"{texts('winner')} {self.players[self.player]}!")

        if self.check_draw(self.player_pos):
            self.new_game=True
            self.someone_win = True
            print(colors("[!!]", "cyan") + colors(f" there is no winner!", "yellow"))
            msg.showinfo(f"tic tac toe", texts("draw"))
        return False

    def check_win(self, pos, player):
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for x in soln:
            if all(y in pos[player] for y in x):return True
        return False    

    def check_draw(self, player_pos):
        if len(player_pos['X']) + len(player_pos['O']) == 9:return True
        return False

def run_details():
    global detail
    global kill_program
    global kill_pygame
    if kill_program:return
    if detail==None:
        pygame.init()
        detail = pygame.display.set_mode((500, 400))
        pygame.display.set_caption("بيانات المسابقة")
        image = pygame.image.load("details.jpeg")
        image = pygame.transform.scale(image, (500, 400))
        detail.blit(image, (0, 0))
        pygame.display.update()
        while not kill_pygame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    kill_pygame=True
                    detail=None
        pygame.quit()

def details():
    global detail
    global kill_pygame
    if detail!=None:
        kill_pygame = True
        detail=None
        return
    kill_pygame=False
    threading.Thread(target=run_details).start()


def pc():
    global player_name
    global games_points
    global something_running
    global running_game
    global running_game_class
    if not something_running:
        running_game = "pc"
        something_running = True
        if player_name == 'player2':player_name='player1'
        if 'player2' in games_points:del games_points['player2'];games_points[player_name] = 0;games_points['bot'] = 0
        if 'bot' not in games_points:games_points['bot'] = 0
        update_score()
        running_game_class =vs_AI(player_name)
        print(colors("[**]", "blue") + colors(" game started vs bot", "yellow"))
    else:
        if running_game == "pc":
            running_game_class.destroy()
            running_game = "pc"
            something_running = True
            if player_name == 'player2':player_name='player1'
            if 'player2' in games_points:del games_points['player2'];games_points[player_name] = 0;games_points['bot'] = 0
            if 'bot' not in games_points:games_points['bot'] = 0
            update_score()
            running_game_class =vs_AI(player_name)
            print(colors("[**]", "blue") + colors(" game started vs bot", "yellow"))
        else:
            print(colors("[!]", "red") + colors(" there is an opened window!", "yellow"))
            msg.showerror('tic tac toe', texts("openedPage"))

def v_friend():
    global player_name
    global games_points
    global something_running
    global running_game
    global running_game_class
    if not something_running:
        running_game = "v_friend"
        something_running = True
        if player_name == 'player2':player_name='player1'
        if 'bot' in games_points:del games_points['bot'];games_points[player_name] = 0;games_points['player2'] = 0
        if player_name not in games_points:games_points[player_name] = 0
        if 'player2'   not in games_points:games_points['player2'] = 0
        update_score()
        running_game_class = vs_friend(player_name)
        print(colors("[**]", "blue") + colors(" game started vs friend!", "yellow"))
    else:
        if running_game == "v_friend":
            running_game_class.destroy()
            running_game = "v_friend"
            something_running = True
            if player_name == 'player2':player_name='player1'
            if 'bot' in games_points:del games_points['bot'];games_points[player_name] = 0;games_points['player2'] = 0
            if player_name not in games_points:games_points[player_name] = 0
            if 'player2'   not in games_points:games_points['player2'] = 0
            update_score()
            running_game_class = vs_friend(player_name)
            print(colors("[**]", "blue") + colors(" game started vs friend!", "yellow"))
        else:
            msg.showerror('tic tac toe', texts("openedPage"))

def update_score():
    text = ""
    for name in games_points.keys():
        text +=f"{name} : {games_points[name]}\n"
    points.configure(text=text)

def reset():
    global games_points
    games_points = {}
    games_points[player_name] = 0
    update_score()

def save_name():
    global player_name
    old_points = games_points[player_name]
    new_player_name = name.get().replace(" ", "_")
    if new_player_name !="" and len(new_player_name)<=10:
        games_points.pop(player_name)
        player_name = new_player_name
        games_points[player_name] = old_points
        update_score()
        msg.showinfo("tic tac toe", f"{texts('savedN')} {player_name}")
    elif len(new_player_name)>10:
        msg.showinfo("tic tac toe", f"{texts('cantmt10')}")

def kill_all(event):
    global session_started
    global something_running
    global server
    global kill_program
    global kill_pygame
    if event.widget.winfo_parent() == "":
        if session_started:
            try:server.close()
            except:pass
        kill_program = True
        session_started = False
        something_running = True
        kill_pygame=True
        try:exit()
        except:sys.exit()
tk.bind("<Destroy>", kill_all)

def change_lang():
    global lang
    global language
    if lang.lower()=='en':lang="ar"
    elif lang.lower()=='ar':lang="en"
    if language.lower()=='english':language="العربية"
    elif language=="العربية":language='English'
    reload()



def reload():
    global b7
    data = {
        "wlc":wlc,
        "b1":b1,
        "b2":b2,
        "b3":b3,
        "b4":b4,
        "urn":urn,
        "b5":b5,
        "b6":b6,
        "leaveS":b7,
        "b8":b8,
    }
    for i in data:
        try:data[i].configure(text=texts(i))
        except:pass

wlc = Label(tk, text=texts("wlc"), fg='white', bg="#212534", font="times 25" )
wlc.place(x=120, y=20)
Label(tk, text="https://github.com/mzo0z", fg='white', bg="#212534", font="times 25" ).place(x=75, y=450)

b1 =Button(tk, text=texts("b1"), width=15, font="times 15", fg='white', bg="#343A40", bd=1, command=pc)
b1.place(x=50, y=125)
hover(b1)
b2 =Button(tk, text=texts("b2"), width=15, font="times 15", fg='white', bg="#343A40", bd=1, command=v_friend)
b2.place(x=250, y=125)
hover(b2)
b3 =Button(tk, text=texts("b3"), width=15, font="times 15", fg='white', bg="#343A40", bd=1, command=create_session)
b3.place(x=50, y=200)
hover(b3)
b4 = Button(tk, text=texts("b4"), width=15, font="times 15", fg='white', bg="#343A40", bd=1, command=join_session)
b4.place(x=250, y=200)
hover(b4)
urn = Label(tk, text=texts("urn"), fg='white', bg="#212534", font="times 25" )
urn.place(x=60, y=245)
name = Entry(tk, width=15, font="times 15")
name.place(x=50, y=280)
b5 = Button(tk, text=texts("b5"), width=5, font="times 12", fg='white', bg="#343A40", bd=1, command=save_name)
b5.place(x=220, y=280)
hover(b5)
b6 = Button(tk, text=texts("b6"), width=10, font="times 12", fg='white', bg="#343A40", bd=1, command=reset)
b6.place(x=300, y=280)
hover(b6)
b8 = Button(tk, text=texts("b8"), width=10, font="times 12", fg='white', bg="#343A40", bd=1, command=change_lang)
b8.place(x=300, y=320)
hover(b8)

def b9_hover(button):
    button.bind("<Enter>", func=lambda e: button.config(bg="#00d5ff", fg="black"))
    button.bind("<Leave>", func=lambda e: button.config(bg="white", fg="black"))


b9 = Button(tk, text="بيانات المسابقة", width=25, font="times 12", fg='black', bg="white", bd=1, command=details)
b9.place(x=120, y=400)
b9_hover(b9)

points = Label(tk, text=f"{player_name} : {games_points[player_name]}", fg='white', bg="#212534", font="times 25" )
points.place(x=50, y=320)


tk.mainloop()


