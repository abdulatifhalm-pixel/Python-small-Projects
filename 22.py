import tkinter as t

r = t.Tk();
r.configure(bg="#222")
d = [["Name", "Age"], ["Ali", 20], ["Sara", 22], ["Omar", 19]]
for i, rw in enumerate(d):
    for j, v in enumerate(rw):
        t.Label(r, text=v, width=8, font=("Arial", 14), bg="#333", fg="white", borderwidth=1, relief="ridge").grid(
            row=i, column=j, padx=2, pady=2)
r.mainloop()
