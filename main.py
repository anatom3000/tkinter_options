import tkinter as tk
import tkinter_options as tkopt

root = tk.Tk()

root.geometry("120x80")

config = tkopt.ConfigDialog(
    {
        "pen_size": 42,
        "log_level": 3.0,
        "msg": "Beautiful default message"
    },
    display={
        "pen_size": "Pen Size",
        "msg": "Message"
    }

)

butt = tk.Button(root, text="Configure...", command=config.spawn)

butt.pack(side="top", expand=True)

get_b = tk.Button(root, text="Print value", command=lambda: print(config["msg"], config["pen_size"]))
get_b.pack(side="top", expand=True)

root.mainloop()
