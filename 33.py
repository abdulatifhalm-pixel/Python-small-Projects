import tkinter as t

r = t.Tk();
r.config(bg="#1e1e1e")
d = [["Name", "Age", 'class'], ["Ali", 20, '12'], ["Sara", 22, '12'], ["Omar", 19, '11']]
for i, rw in enumerate(d):
    for j, v in enumerate(rw):
        c = "#444" if i else "#666"
        t.Label(r, text=v, bg=c, fg="white", font=("Segoe UI", 13), width=8, padx=6, pady=3).grid(row=i, column=j,
                                                                                                  padx=2, pady=2)
r.mainloop()
