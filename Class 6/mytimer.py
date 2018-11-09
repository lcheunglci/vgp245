import tkinter as tk

counter = 0

def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

root = tk.Tk()
root.title("My timer")
label = tk.Label(root, fg='red')
label.pack()

counter_label(label)

root.mainloop()



    

