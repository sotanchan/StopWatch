import tkinter as tk
import time
import threading

class stopwatch():
    def __init__(self):
        self.timer_switch=False
        self.start_time=0.0

        #ウィンドウの作成
        self.root=tk.Tk()
        self.root.geometry("300x500")
        self.root.title("ストップウォッチ")

        #測定時間の表示
        self.time_var=tk.StringVar()
        self.time_var.set(self.start_time)
        self.Time=tk.Label(self.root,textvariable=self.time_var)
        self.Time.pack()

    def timer(self):
        while(True):
            if self.timer_switch==True:
                time.sleep(0.1)
                self.start_time+=0.1
                self.time_var.set(round(self.start_time,1))
            else:
                continue
    
    #スタートボタンの関数
    def start(self,event):
        self.timer_switch=True

    #ストップボタンの関数
    def stop(self,event):
        self.timer_switch=False

    #リセットボタンの関数
    def reset(self,event):
        self.start_time=0.0
        self.time_var.set(round(self.start_time,1))
        
    #ボタン作成するための関数
    def button_rayout(self,button_name,text,button_func,x,y):
        button_name=tk.Button(self.root,text=text,width=10)
        button_name.bind("<Button-1>",button_func)
        button_name.place(x=x,y=y)

stopwatch=stopwatch()

#それぞれのボタン作成
stopwatch.button_rayout("start_button","スタート",stopwatch.start,20,40)
stopwatch.button_rayout("stop_button","ストップ",stopwatch.stop,20,80)
stopwatch.button_rayout("reset_button","リセット",stopwatch.reset,20,120)

thread1=threading.Thread(target=stopwatch.timer)
thread1.start()

stopwatch.root.mainloop()