from tkinter import *
from idas_search import *

def center_window(w, h, window):
    # 获取屏幕 宽、高
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2) - 30
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window = Tk()
window.title('Flood-it')
center_window(650, 650, window)
frame1 = Frame(window)
frame1.pack()

frame10 = Frame(frame1)
frame10.pack()
l0 = Label(frame10, text='Size of game board', width=20)
l0.pack(side='left')
e0 = Entry(frame10, width=30)
# e0.insert(END, 'a single integer N (1<N<10)')
e0.pack(side='right')

frame13 = Frame(frame1, height=10)
frame13.pack()

frame12 = Frame(frame1)
frame12.pack()

frame14 = Frame(frame1, height=10)
frame14.pack()

l1 = Label(frame12, text='The game board', width=20)
l1.pack(side='left')
t1 = Text(frame12, width=20, height=10)
t1.pack(side='right')


frame11 = Frame(frame1)
frame11.pack()

frame16 = Frame(frame1, height=10)
frame16.pack()

frame15 = Frame(frame1)
frame15.pack()

l1 = Label(frame15, text='Result', width=20)
l1.pack()
t2 = Text(frame15, width=70, height=30)
t2.pack()

def generate():
    t2.delete('0.0', 'end')
    result = main(e0.get(), t1.get('0.0', 'end'))
    t2.insert('0.0', result)

#button
button = Button(frame11, text='submit', width=10, font=('Ariai',12), command=generate)
button.pack(side='right')

window.mainloop()
