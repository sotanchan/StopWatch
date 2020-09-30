import tkinter as tk
import tkinter.scrolledtext
import time
import threading

timer_switch=False
start_time=0.0
rap_num=1
rap_time=0.0
split_time=0.0
split_num=1
rap_row=1.0
split_row=1.0

def timer():
    global timer_switch
    global start_time
    global rap_time
    while(True):
        if timer_switch==True:
            time.sleep(0.1)
            start_time+=0.1
            rap_time+=0.1
            time_var.set(round(start_time,1))
        else:
            continue

#スタートボタンの関数
def start(event):
    global timer_switch
    timer_switch=True

#ストップボタンの関数
def stop(event):
    global timer_switch
    timer_switch=False

#リセットボタンの関数
def reset(event):
    global start_time
    global rap_num
    global split_num
    start_time=0.0
    rap_num=1
    split_num=1
    time_var.set(round(start_time,1))
    rap_list.delete('1.0','end')
    split_list.delete('1.0','end')

#ラップボタンの関数
def rap(event):
    global rap_num
    global rap_time
    global rap_row
    rap_list.insert(rap_row,"ラップ{0}：{1}\n".format(rap_num,round(rap_time,1)))
    rap_num+=1
    rap_row+=1
    rap_time=0.0

#スプリットボタンの関数
def split(event):
    global split_time
    global split_num
    global split_row
    split_time=start_time
    split_list.insert(split_row,"スプリット{0}：{1}\n".format(split_num,round(split_time,1)))
    split_num+=1
    split_row+=1


#ボタン作成するための関数
def button_rayout(button_name,text,button_func,x,y):
    button_name=tk.Button(root,text=text,width=10)
    button_name.bind("<Button-1>",button_func)
    button_name.place(x=x,y=y)

#ウィンドウの作成
root=tk.Tk()
root.geometry("300x500")
root.title("ストップウォッチ")

#測定時間の表示
time_var=tk.StringVar()
time_var.set(start_time)
Time=tk.Label(root,textvariable=time_var)
Time.pack()

thread1=threading.Thread(target=timer)
thread1.start()


#ラップリストの表示
rap_list=tk.scrolledtext.ScrolledText(root,width=15,height=10)
rap_list.place(x=20,y=240)

#スプリットリストの表示
split_list=tk.scrolledtext.ScrolledText(root,width=15,height=10)
split_list.place(x=120,y=240)

#それぞれのボタン作成
button_rayout("start_button","スタート",start,20,40)

button_rayout("stop_button","ストップ",stop,20,80)

button_rayout("reset_button","リセット",reset,20,120)

button_rayout("rap_button","ラップ",rap,20,160)

button_rayout("split_buton","スプリット",split,20,200)


root.mainloop()