# Follow Us On Twitter @PY4ALL

from tkinter import *
from tkinter import ttk
import numpy as np
import math

class MainWindow:

    def __init__(self, master):

        master.title('Connect4 Game')
        master.resizable(False, False)
        master.configure(background = 'white')
        self.a = []

        self.turn = 'red'
        self.w = Canvas(master, width=780, height=590, bg='white')
        self.w.pack()

        self.frame_control = ttk.Frame()
        self.frame_control.pack()


        ttk.Button(master, text = 'Clear',
                   command = self.clear).pack()

        self.a.append( self.w.create_oval(40, 20, 40+70, 20+70, fill=self.turn, outline=self.turn, width=4, tags=('delete',)) )

        self.w.bind("<Button 1>",self.get_loc)
        self.w.bind('<Motion>',self.mouseCoords)

        self.draw_loc = []
        for x in range(40,699,106):
            temp = []
            for y in range(120,510,77):
                temp.append((x,y))
            self.draw_loc.append(temp)

        self.game = [['','','','','',''],
                     ['','','','','',''],
                     ['','','','','',''],
                     ['','','','','',''],
                     ['','','','','',''],
                     ['','','','','',''],
                     ['','','','','','']]
        self.gif1 = PhotoImage(file='pngkit_connect-four-png_7125400.png')
        self.w.create_image(3, 103, image=self.gif1, anchor=NW, tags=('front',))
        self.w.tag_raise('front')
        self.game_end = False

    def mouseCoords(self,event):
        pointxy = (event.x-35, 20, event.x+35, 20+70) 
        self.w.coords(self.a[-1], pointxy) 

        
    def get_loc(self, event):
        if not self.game_end and len(self.draw_loc[event.x//111]) > 0:
            if self.turn == 'red':
                self.loc = self.draw_loc[event.x//111].pop()
                self.game[event.x//111][len(self.draw_loc[event.x//111])]= self.turn
                self.move_object(self.a[-1], self.loc)
                print(self.game)
                self.turn = 'black'
                self.a.append( self.w.create_oval(event.x-35, 20, event.x+35, 20+70, fill=self.turn, outline=self.turn, width=4, tags=('delete',)) )
                self.w.tag_raise('front')
            else:
                self.loc = self.draw_loc[event.x//111].pop()
                self.game[event.x//111][len(self.draw_loc[event.x//111])]= self.turn
                self.move_object(self.a[-1], self.loc)
                print(self.game)
                self.turn = 'red'
                self.a.append( self.w.create_oval(event.x-35, 20, event.x+35, 20+70, fill=self.turn, outline=self.turn, width=4, tags=('delete',)) )
                self.w.tag_raise('front')
        self.game_end = self.check()

    def check(self):
        if not any('' in sublist for sublist in self.game):
            self.w.create_text(400,50,font='Times 40 bold',text='Tie!', tags=('delete',), fill='blue')
            return True
        for col in range(0,4):
            for row in range(0,6):
                if (self.game[col][row] != '' and
                   self.game[col][row] == self.game[col+1][row] and
                   self.game[col][row] == self.game[col+2][row] and
                   self.game[col][row] == self.game[col+3][row]):
                       self.winner(self.game[col][row])
                       return True
        for col in range(0,7):
            for row in range(0,3):
                if (self.game[col][row] != '' and
                   self.game[col][row] == self.game[col][row+1] and
                   self.game[col][row] == self.game[col][row+2] and
                   self.game[col][row] == self.game[col][row+3]):
                       self.winner(self.game[col][row])
                       return True

        for col in range(0 , 4):
            for row in range(0 , 3):
                if (self.game[col][row] != '' and
                   self.game[col][row] == self.game[col+1][row+1] and
                   self.game[col][row] == self.game[col+2][row+2] and
                   self.game[col][row] == self.game[col+3][row+3]):
                       self.winner(self.game[col][row])
                       return self.game[col][row]

        for col in range(3 , 7):
            for row in range(0 , 3):
                if (self.game[col][row] != '' and
                   self.game[col][row] == self.game[col-1][row+1] and
                   self.game[col][row] == self.game[col-2][row+2] and
                   self.game[col][row] == self.game[col-3][row+3]):
                       self.winner(self.game[col][row])
                       return self.game[col][row]




    def clear(self):
        self.w.delete('delete')
        self.game_end = False
        self.a = []
        self.a.append( self.w.create_oval(40, 20, 40+70, 20+70, fill=self.turn, outline=self.turn, width=4, tags=('delete',)) )
        self.draw_loc = []
        for x in range(40,699,106):
            temp = []
            for y in range(120,510,77):
                temp.append((x,y))
            self.draw_loc.append(temp)

        self.game = [['','','','','',''],
                     ['','','','','',''],
                     ['','','','','',''],
                     ['','','','','',''],
                     ['','','','','',''],
                     ['','','','','',''],
                     ['','','','','','']]
        self.w.tag_raise('front')

    def winner(self,name):
        self.w.create_text(400,50,font='Times 40 bold',text=f'{name} won!', tags=('delete',), fill=name)
            
    def move_object(self, object_id, destination, speed=0):
        dest_x, dest_y = destination
        coords = self.w.coords(object_id)
        current_x = coords[0]
        current_y = coords[1]

        new_x, new_y = current_x, current_y
        delta_x = delta_y = 0
        if current_x < dest_x:
            delta_x = 1
        elif current_x > dest_x:
            delta_x = -1

        if current_y < dest_y:
            delta_y = 1
        elif current_y > dest_y:
            delta_y = -1

        if (delta_x, delta_y) != (0, 0):
            self.w.move(object_id, delta_x, delta_y)

        if (new_x, new_y) != (dest_x, dest_y):
            self.w.after(speed, self.move_object, object_id, destination, speed)     
            
def main():            
    
    root = Tk()
    mainwindow = MainWindow(root)
    root.mainloop()
    
if __name__ == "__main__": main()
