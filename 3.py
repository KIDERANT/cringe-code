from random import randint
from tkinter import *
colors = ['white', 'gray', 'brown', 'yellow', 'blue', 'red','green', 'pink', 'magenta', 'black']




def change_square():
    n = randint(1,3)
    if n == 1:
        canvas.delete("all")
        canvas.create_polygon(x, y, x+side, y, x+side//2, y-side//2, fill=colors[4], outline='white')
    elif n == 2:
        canvas.delete("all")
        canvas.create_oval(x, y, x+side, y+side, fill=colors[4], outline='white')
    elif n == 3:
        canvas.delete("all")
        canvas.create_rectangle(x, y, x+side, y+side, fill=colors[4], outline='white')
    



side = 200
canvas_width, canvas_height = 500, 500
x, y = 150, 300
root = Tk()
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
square = canvas.create_rectangle(x, y, x+side, y+side, fill=colors[2], outline='white')
roof = canvas.create_polygon(x, y, x+side, y, x+side//2, y-side//2, fill=colors[1], outline='white')
sun = canvas.create_oval(canvas_width - side//2, 0, canvas_width, side//2, fill=colors[3], outline='white')
Button(text='Основание', command=change_square).pack()
root.mainloop()
