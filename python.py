from tkinter import*
from game import *


root = Tk()
root.geometry('400x400')
root.title = ('2048')
root.resizable(False, False)

canvas = Canvas(root, width=400, height=400)
canvas.place(x=0, y=0)

my_image = PhotoImage(file='D:\\Downloads\\2048-androappinfo-e1401292098210.png')
canvas.create_image(0,0, anchor=NW, image=my_image)

btns = Frame(root)
btns.place(x=125, y=300)

def play_btn():
    global root
    print('game')
    root.destroy()
    size = 4
    grid = Grid(size)
    panel = GamePanel(grid)
    game2048 = Game(grid, panel)
    game2048.start()
    
    
btn = Button(btns, text='Play', width='20', height='2', command=play_btn)
btn.pack()

def quit_btn():
    print('quit')
    root.destroy()
    
btn_2 = Button(btns, text='Quit', width='20', height='2', command = quit_btn)
btn_2.pack()

root.mainloop()
    
