import tkinter as tk
from tkinter import *


label_tags = {}
button_tags = {}
chk_tags = {}







def delete_widget(tag):
    for widget, widget_tag in list(label_tags.items()):
        if widget_tag == tag:
            widget.destroy()
            #del label_tags[widget]

    for widget, widget_tag in list(button_tags.items()):
        if widget_tag == tag:
            widget.destroy()
            #del button_tags[widget]
    for widget, widget_tag in list(chk_tags.items()):
        if widget_tag == tag:
            widget.destroy()
            #del chk_tags[widget]


def create_label():
    count = len(label_frm.winfo_children())+1
    todo_label = tk.Label(label_frm, text=f" Todo #{count} :"+txt.get(), font=("Arial", 15))
    todo_label.pack(side=TOP)
    label_tags[todo_label] = count

    delete_button = tk.Button(btn_frm, text="Delete",font=("Arial", 10), command=lambda: delete_widget(count))
    delete_button.pack(side=TOP)
    button_tags[delete_button] = count

    chk = tk.Checkbutton(check_frm)
    chk.pack(side=TOP)
    chk_tags[chk] = count
    cleartxt()







def cleartxt():
    txt.delete(0, END)








root = tk.Tk()
root.geometry("500x600")

inputfrm = tk.Frame(root)
inputfrm.pack(fill='x', padx=5)

txt = tk.Entry(inputfrm, font=('Arial', 16))
txt.pack(expand=1 ,fill="x", side=LEFT)

btn = tk.Button(inputfrm, text="Add", font=('Arial', 10), command=create_label)
btn.pack(padx=5, side=RIGHT)


frm = tk.Frame(root)
frm.pack(pady=5, fill=BOTH)

frm.columnconfigure(0, weight=3)
frm.columnconfigure(1, weight=1)
frm.columnconfigure(2, weight=1)



label_frm = tk.Frame(frm)
label_frm.grid(row=0, column=0)

btn_frm = tk.Frame(frm)
btn_frm.grid(row=0, column=2)

check_frm = tk.Frame(frm,width=50, height=50)
check_frm.grid(row=0, column=1)





root.mainloop()
