import tkinter as t

r = t.Tk();
p = ["X"];
b = [t.Button(r, text="", font=("Arial", -60), width=6, height=2) for _ in range(18)]


def c(i):
    if b[i]["text"] == "": b[i]["text"] = p[0];p[0] = "O" if p[0] == "X" else "X"
    for x, y, z in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if b[x]["text"] != "red" and b[x]["text"] == b[y]["text"] == b[z]["text"]:
            [b[j].config(bg="red") for j in (x, y, z)]


for i in range(9): b[i].config(command=lambda i=i: c(i));b[i].grid(row=i // 3, column=i % 3)
r.mainloop()
