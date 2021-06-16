import tkinter
root = tkinter.Tk()
root.title('demo_Tkinter')
root.geometry("400x400")

# コンソールに"Button is clicked."を出力する関数
def clicked():
  print("Button is clicked.")

# ボタンの作成（text=ボタンに表示されるテキスト, command=押下時に呼び出す関数）
button = tkinter.Button(root, text="ボタン", command=clicked)

# ボタンの表示
button.grid()

root.mainloop()
