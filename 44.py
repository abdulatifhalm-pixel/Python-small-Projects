import tkinter as t

r = t.Tk();
r.title("Multiplication Table")
for i in range(1, 11):
    for j in range(1, 11):
        t.Label(r, text=i * j, width=4, bg="#eee" if (i + j) % 2 == 0 else "#ccc", font=("Arial", 12), borderwidth=1,
                relief="solid").grid(row=i, column=j)
r.mainloop()
