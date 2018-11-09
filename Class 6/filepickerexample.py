import tkinter as tk
import tkinter.messagebox 
import tkinter.filedialog
import tkinter.colorchooser

def choose_file_to_open():
    with tkinter.filedialog.askopenfile(filetypes = (("XML files", "*.xml")
                                                         ,("Text files", "*.txt;")
                                                         ,("All files", "*.*") )) as f:
        print(f.read())
        ##f.write('hello')

def choose_file_to_save():
    with tkinter.filedialog.asksaveasfile() as f:
        print(f.write('Almost end of class'))

def choose_color():
    color = tkinter.colorchooser.askcolor()
    print(color)

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save", command=choose_file_to_save)
filemenu.add_command(label="Open", command=choose_file_to_open)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=quit)

tk.Label(root, fg='blue', text="File test").grid(row=0)

tk.Button(root, text="Open...", command=choose_file_to_open).grid(row=1, column=0)
tk.Button(root, text="Save...", command=choose_file_to_save).grid(row=1, column=1)
tk.Button(root, text="Select Color", command=choose_color).grid(row=2, column=0)


root.mainloop()