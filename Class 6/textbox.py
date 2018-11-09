import tkinter as tk
import tkinter.messagebox 

def show_results():
    print(f'{textbox1.get()} {textbox2.get()}')

def clear():
    #tk.messagebox.showwarning('nothing', 'nothing12')
    if tk.messagebox.askyesno('Confirmation', 'Are you sure?'):
        textbox1.delete(0, tk.END)
        textbox2.delete(0, tk.END)
    else:
        print('cancelled.')

root = tk.Tk()

tk.Label(root, fg='blue', text="first name").grid(row=0)
tk.Label(root, fg='blue', text="last name").grid(row=1)

textbox1 = tk.Entry(root)
textbox2 = tk.Entry(root)

textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)

#textbox1.insert()
textbox1.delete(0, tk.END)

tk.Button(root, text="Print", command=show_results).grid(row=3)
tk.Button(root, text="Clear", command=clear).grid(row=3, column=1)

root.mainloop()