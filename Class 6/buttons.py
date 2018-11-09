import tkinter as tk

def write_something():
    print("You pressed me...")

def increment():
    count.set(count.get() + 1)

def show_greeting():
    myData.set("Welcome, how are you today?")

root = tk.Tk()

count=tk.IntVar()
myData=tk.StringVar()

frame = tk.Frame(root)
frame.pack()

#label = tk.Label(frame, text="dummy text")
label = tk.Label(frame, textvariable=count)
label.pack()

greetingsLbl = tk.Label(frame, textvariable=myData)
greetingsLbl.pack()

button = tk.Button(frame,
                    text="Quit",
                    fg="red",
                    command=quit)
button.pack(side=tk.LEFT)

button2 = tk.Button(frame,
text="Press me",
fg="blue",
command=myData)
button2.pack()

root.mainloop()






