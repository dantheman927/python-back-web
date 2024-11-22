import tkinter as tk

r = tk.Tk()
r.title("rassbarry pi over lay ")


button = tk.Button(r, text="press fun button", width=50, command=r.destroy)
button.pack()

clipbord = tk.COMMAND=r.clipboard_get()

print(clipbord)

text = " this is what you have in your clipbord right now"

clip_all_together = clipbord + text
Message = tk.Message(text=clip_all_together)
Message.pack()

r.mainloop()