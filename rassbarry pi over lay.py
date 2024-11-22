import tkinter as tk

r = tk.Tk()
r.title("rassbarry pi over lay ")

screen_width = r.winfo_screenwidth()
screen_height = r.winfo_screenheight()
 


r.geometry(f"{screen_width}x{screen_height}")


button = tk.Button(r, text="press fun button", width=50, command=r.destroy)
button.grid(row = 0, column = 0)


r.mainloop()