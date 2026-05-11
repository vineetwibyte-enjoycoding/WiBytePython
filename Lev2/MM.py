import tkinter as tk


def calculate():
	start = start_station.get()
	stop = stop_station.get()

  	# determine which lines are the stations 
	if start in stn_sL:
		start_line = stn_sL
	else:
		start_line = stn_pL
	
	if stop in stn_sL:
		stop_line = stn_sL
	else:
		stop_line = stn_pL
		
	if start_line is stop_line:
		# on the same line
		n_stops = abs(start_line.index(start) - start_line.index(stop))
	else:
		# Different lines
		n_stops = start_line.index(start) - start_line.index('WiByte')
		n_stops = abs(n_stops) + abs(stop_line.index('WiByte') - stop_line.index(stop))
	
	fare = n_stops*20
	farelabel.configure(text = 'FARE = INR ' + str(fare))


window = tk.Tk()
window.title("WiByte Metro Map")
window.configure(bg='Darkgreen')
window.geometry("600x600+10+0")  




# window.geometry("900x450+10+100")



c = tk.Canvas(window, width = 550, height=500)
c.pack()




stn_sL = ['SpriteLand', 'GoNGlide', 'Costumes', 'Broadcast', 'WiByte', 'Cloning', 'MyBlocks']


x_s = 50
y_s = 200
d_stn = 70
r_stn = 6



for stn in stn_sL:
  if stn != stn_sL[-1]:
	  c.create_line(x_s, y_s, x_s + d_stn, y_s, fill = 'DarkOrange')
  c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill = 'DarkOrange')
  c.create_text(x_s, y_s + 30, text = stn, fill = 'DarkOrange', font = ('Helvetica 6 bold'))
  x_s = x_s + d_stn

# Python Line
stn_pL = ['EscapeChar', 'WhileLoop', 'WiByte', 'IfElifElse', 'Range', 'Dictionary', 'TurtlePark']

x_s = 330
y_s = 40
d_stn = 70
r_stn = 6

for stn in stn_pL:
	if stn != stn_pL[-1]:
		c.create_line(x_s, y_s, x_s, y_s + d_stn, fill = 'blue')
	c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill = 'blue')
	c.create_text(x_s + 40, y_s, text = stn, fill = 'blue', font = ('Helvetica 6 bold'))
	y_s = y_s + d_stn









# Get all the stations but remove the interchange station
all_stations = stn_sL  + stn_pL
all_stations.remove('WiByte')

c.create_text(30, 250, text='Start')
start_station = tk.StringVar()
drop_start = tk.OptionMenu(window, start_station, *all_stations)
drop_start.place(x = 30, y = 270)

c.create_text(240, 250, text='Stop')
stop_station = tk.StringVar()
drop_stop = tk.OptionMenu(window, stop_station, *all_stations)
drop_stop.place(x = 240, y = 270)




button = tk.Button(text="Calculate Fare", command = calculate)
button.pack()



farelabel = tk.Label(window, text='FARE = ', font = ('Helvetica 12 bold'))
farelabel.pack() 
tk.mainloop()


'''
r_stn = 6


def draw_metro_line(stn_list, init_pos, step, label_offset, clr):
	x_s = init_pos[0]
	y_s = init_pos[1]
	x_step = step[0]
	y_step = step[1]
	for stn in stn_list:
		if stn != stn_list[-1]:
			c.create_line(x_s, y_s, x_s + x_step, y_s + y_step, fill = clr)
		c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill = clr)
		c.create_text(x_s + label_offset[0], y_s + label_offset[1], text=stn, fill=clr, font=('Helvetica 6 bold'))

		x_s = x_s + x_step
		y_s = y_s + y_step

draw_metro_line(stn_sL, [50, 200], [70, 0], [0, 30], 'DarkOrange')
draw_metro_line(stn_pL, [330, 40], [0, 70], [35, 0], 'blue')


'''
