import tkinter as tk

root = tk.Tk()
root.title("Hello VGP")
img = tk.PhotoImage(file='megaman.png')
#w = tk.Label(root, compound= tk.CENTER, text="Hello world", image=img)
msg = """
lksjalkjf
aslkdfj;lakdsj
aldkfj;alkjf
asdlfjalfdj
"""

#w = tk.Label(root, justify=tk.LEFT, text=msg, image=img)
w = tk.Message(text=msg)
w.config(bg='yellow', fg='blue', font=('times', 24, 'bold'))


w.pack(side="right")

root.mainloop()