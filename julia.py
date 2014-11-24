from Tkinter import *
from time import sleep



def julia(obj, x, y, c, n):

	for i in range(x):
		for j in range(y):
			z = (3.0*i/x-1.5) + (3.0*j/y-1.5)*1j 
			
			for k in range(n):
				z = z**2 + c

			if abs(z) > 2:
				obj.create_line(i, j, i+1, j+1,fill="green")
				



WIDHT  = 500
HEIGHT = 500
c = -0.72-0.196j
#0.285-0.01j, -1.3+0.00525j, -0.72 - 0.196j, -0.1+0.87j, -0.51-0.601j

tk = Tk()
'''
canvas = Canvas(tk, width=WIDHT, height=HEIGHT)
julia(canvas, WIDHT, HEIGHT, c, 9)
canvas.pack()
canvas.mainloop()

'''
for n in range(9):
	canvas = Canvas(tk, width=WIDHT, height=HEIGHT)
	julia(canvas, WIDHT, HEIGHT, c, n)
	canvas.pack()
	tk.update()
	sleep(2)
	canvas.destroy()

