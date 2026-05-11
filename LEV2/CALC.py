import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x300")
window.resizable(0, 0)

def press_num(num):
  text_in_box = entr_label.cget('text')
  entr_label.configure(text = text_in_box + str(num))

def press_op(operator):

  text_in_box = entr_label.cget('text')
  text_in_expr = expr_label.cget('text')
  
  expr_label.configure(text = text_in_expr + text_in_box + operator)
  entr_label.configure(text = '')

def press_C():
  expr_label.configure(text = '')
  entr_label.configure(text = '')

def press_eq():

  text_in_box = entr_label.cget('text')
  text_in_expr = expr_label.cget('text')

  expr_label.configure(text = text_in_expr + text_in_box + ' = ')

  try:
    result = eval(text_in_expr + text_in_box)
    entr_label.configure(text = str(result))
  except:
    entr_label.configure(text = 'ERROR !!!')
        
  


expr_label = tk.Label(window, text = '', bg = 'grey', width = 36, height= 3, borderwidth = 3, relief = 'ridge', anchor = tk.E)
expr_label.grid(column = 0, row = 0, columnspan = 5)


entr_label = tk.Label(window, text = '', bg = 'grey', font = ('Arial bold', 15), width = 22, height= 3, borderwidth = 3, relief = 'ridge', anchor = tk.E)
entr_label.grid(column = 0, row = 1, columnspan = 5)



tk.Button(text = ' 7 ', fg = 'black', bg = 'grey', command= lambda: press_num(7)).grid(row=2, column = 0, sticky= tk.NSEW)
tk.Button(text = ' 8 ', fg = 'black', bg = 'grey', command= lambda: press_num(8)).grid(row=2, column = 1, sticky= tk.NSEW)
tk.Button(text = ' 9 ', fg = 'black', bg = 'grey', command= lambda: press_num(9)).grid(row=2, column = 2, sticky= tk.NSEW)
tk.Button(text = ' / ', fg = 'black', bg = 'grey', command= lambda: press_op('/')).grid(row=2, column = 3, sticky= tk.NSEW)
tk.Button(text = ' C ', fg = 'black', bg = 'grey', command = press_C).grid(row=2, column = 4, rowspan= 2, sticky= tk.NSEW)

tk.Button(text = ' 4 ', fg = 'black', bg = 'grey', command= lambda: press_num(4)).grid(row=3, column = 0, sticky= tk.NSEW)
tk.Button(text = ' 5 ', fg = 'black', bg = 'grey', command= lambda: press_num(5)).grid(row=3, column = 1, sticky= tk.NSEW)
tk.Button(text = ' 6 ', fg = 'black', bg = 'grey', command= lambda: press_num(6)).grid(row=3, column = 2, sticky= tk.NSEW)
tk.Button(text = ' * ', fg = 'black', bg = 'grey', command= lambda: press_op('*')).grid(row=3, column = 3, sticky= tk.NSEW)

tk.Button(text = ' 1 ', fg = 'black', bg = 'grey', command= lambda: press_num(1)).grid(row=4, column = 0, sticky= tk.NSEW)
tk.Button(text = ' 2 ', fg = 'black', bg = 'grey', command= lambda: press_num(2)).grid(row=4, column = 1, sticky= tk.NSEW)
tk.Button(text = ' 3 ', fg = 'black', bg = 'grey', command= lambda: press_num(3)).grid(row=4, column = 2, sticky= tk.NSEW)
tk.Button(text = ' - ', fg = 'black', bg = 'grey', command= lambda: press_op('-')).grid(row=4, column = 3, sticky= tk.NSEW)
tk.Button(text = ' = ', fg = 'black', bg = 'grey', command= press_eq).grid(row=4, column = 4, rowspan= 2, sticky= tk.NSEW)


tk.Button(text = ' 0 ', fg = 'black', bg = 'grey', command= lambda: press_num(0)).grid(row=5, column = 0, columnspan = 2, sticky= tk.NSEW)
tk.Button(text = ' . ', fg = 'black', bg = 'grey', command= lambda: press_num('.')).grid(row=5, column = 2, sticky= tk.NSEW)
tk.Button(text = ' + ', fg = 'black', bg = 'grey', command= lambda: press_op('+')).grid(row=5, column = 3, sticky= tk.NSEW)





#hello = tk.Label(text="Hello world!")
#hello.pack()
#button = tk.Button(text="Click me!")
#button.pack()

tk.mainloop()