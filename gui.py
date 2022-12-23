import tello
import tkinter as tk

def get_command():

    def on_change(e):
        command = e.widget.get()
        e.widget.delete(0, 'end')
        response = tello.send_command(command)
        cmd.set(response)

    window = tk.Tk()
    window.title("tello")

    cmd = tk.StringVar()

    label = tk.Label(text="Enter command")
    entry = tk.Entry()
    label2 = tk.Label(text="Response")
    label3 = tk.Label(textvariable = cmd)

    label.pack()
    entry.pack()
    label2.pack()
    label3.pack()

    entry.bind("<Return>", on_change)

    window.mainloop()
