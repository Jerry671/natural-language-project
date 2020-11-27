import tkinter as tk
import sys
root = tk.Tk()
path = r'soc-pokec-relationships_sub-CommonNeighbours-predictions_2019-10-27_21.30.txt'
lst = []
 
f = open(path, "r")
for line in f:
    subList = line.replace('\n', '').split('\t')
    lst.append(subList)
f.close()
for i in range(20):
    sys.stdout.write(str(lst[i]) + '\n')
sys.stdout.write("list is done")
root.title("link prediction")

list_box = tk.Listbox(root)

def go():
    sys.stdout.write("changed\n")
    for i in range(4):  # 每次多显示4个
        list_box.delete(8)
        slist = lst.pop(0)
        str = slist[0] + '   ' + slist[1] + '   ' + slist[2]
        list_box.insert(0,str)


but = tk.Button(root,text='next',bg='white', command=go)

for i in range(8):
    slist = lst.pop(0)
    str = slist[0] + '   ' + slist[1] + '   ' + slist[2]
    list_box.insert(0, str)
list_box.pack()
but.pack()
root.mainloop()
