import tkinter as tk
import tkinter.messagebox as tkmg
import random

#margeテスト
class Aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=380,height=480,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):

        #結果表示部分
        Text_sp = tk.Label(self,text="結果",font = (20))
        self.Text = tk.StringVar()#別のdefで参照する変数はself.~にする
        self.Text.set ("-")
        label = tk.Label(self,textvariable = self.Text,font = ("Times",30,'bold'))

        #抽選ボタン
        start_btn = tk.Button(self, text="抽選開始",command=self.button_click)#command=~でdef~に飛ぶ

        #履歴部分
        self.rireki_sp = tk.LabelFrame(self,text="履歴",padx=10,pady=10)
        self.Text2 = tk.StringVar()
        self.Text2.set("-")
        rireki1 = tk.Message(self.rireki_sp,textvariable = self.Text2,width=270,anchor="nw")

        #回数カウント
        ct_sp = tk.Label(self,text="現在の抽選回数")
        self.count_Text = tk.StringVar()
        self.count_Text.set(0)
        count = tk.Label(self,textvariable = self.count_Text)

        #リセットボタン
        reset_btn = tk.Button(self, text="リセット",command =self.reset_click)#command=~でdef~に飛ぶ

        #検索画面
        self.sort_sp=tk.LabelFrame(self,text="検索",padx=10,pady=10)
        self.sort_box=tk.Entry(width=10)
        sort_button=tk.Button(self,text="検索",command=self.sort_click)

        #閉じるボタン
        quit_btn = tk.Button(self)
        quit_btn['text'] ='終了'
        quit_btn['command'] = self.root.destroy

        #Widgetの配置
        Text_sp.place(relx=0.5,y=20,anchor=tk.CENTER)
        label.place(relx = 0.5,y = 70,anchor=tk.CENTER)
        start_btn.place(relx=0.5,y=120,anchor=tk.CENTER)
        self.rireki_sp.place(relx=0.5,relwidth=0.8,y=220,height=150,anchor=tk.CENTER)
        rireki1.grid(in_=self.rireki_sp,row=0,column=0)
        ct_sp.place(relx = 0.5,y=320,anchor=tk.CENTER)
        count.place(relx=0.5,y=340,anchor=tk.CENTER)
        self.sort_sp.place(relx=0.5,y=390,anchor=tk.CENTER)
        self.sort_box.grid(in_=self.sort_sp,row=0,column=0)
        sort_button.grid(in_=self.sort_sp,row=0,column=1)
        reset_btn.place(relx=0.2,y=450,anchor=tk.CENTER)
        quit_btn.place(relx=0.8,y=450,anchor=tk.CENTER)

    def button_click(self):
        kazu = len(hyouzi)
        #乱数生成
        kari=random.randint(1,75)
        print(kari)
        #重複回避
        while True:
            if not kari in hyouzi:
                hyouzi.insert(0,kari)
                break
            else:
                #75個以上のときの実装
                if kazu < 75: 
                    kari=random.randint(1,75)
                else:
                    tkmg.showinfo("テスト","リセットしてください")
                    break

        print(hyouzi)#リスト内確認
        #print(kazu)
        #各表示の更新
        self.Text.set(hyouzi[0])
        if kazu >= 1:
            self.Text2.set(hyouzi[1:kazu+1])
        else:
            pass
        self.count_Text.set(kazu+1)

    def reset_click(self):
        hyouzi.clear()
        #print(hyouzi)
        kazu = len(hyouzi)
        #print(kazu)
        self.Text.set("-")
        self.Text2.set("-")
        self.count_Text.set(kazu)

    def sort_click(self):
        kennsaku = self.sort_box.get()
        if int(kennsaku) in hyouzi:
            text3="抽選済みです"
        else:
            text3="抽選されていません"
        tkmg.showinfo("検索結果",text3)

root = tk.Tk()
hyouzi = []#空のリスト
#hyouzi.clear()
root.title("bingo!!")#title
#root.geometry("400x500")
app = Aplication(root=root)
app.mainloop()