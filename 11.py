import tkinter as t

r = t.Tk()
d = [["Name", "Age", 'add', 'ph', 'blood', ''], ["Ali", 20], ["Sara", 22], ["Omar", 19]]
for i in range(len(d)):
    for j in range(len(d[i])):
        t.Label(r, text=d[i][j], width=10, bg="lightyellow", borderwidth=1, relief="solid").grid(row=i, column=j)
r.mainloop()
