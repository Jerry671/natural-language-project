# NPL
通过自然语言处理分析和预测任意两个人为好友的可能性

## 项目介绍
基于开源项目linkpred实现网络关系的预测
使用到了机器学习的逻辑回归算法进行人群分类
使用到了TF-IDF算法对文字进行处理
<br>用户可以通过修改训练集预测不同人际关系之间的好友关系可能性
<br>每次预测显示四组人之间的好友关系可能性，通过点击NEXT按钮进行下一组预测
<br>(支持python3.+版本)
## 使用说明
默认使用斯坦福大学的soc-pokec-relationships数据集进行训练，详情参考项目介绍

<br>编译运行GUIshow.py，将会显示如下图的结果
<br>![yucejieguo](https://github.com/Twinklight/Network-relation-prediction/blob/godzyp/%E9%A2%84%E6%B5%8B%E7%BB%93%E6%9E%9C.jpg "预测结果")
<br>其中前两列代表人物标号，第三列为两人可能为好友关系的概率
### 使用到的开源项目
[linkpred](https://github.com/rafguns/linkpred)

### 项目主要功能实现代码
```python
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
```
