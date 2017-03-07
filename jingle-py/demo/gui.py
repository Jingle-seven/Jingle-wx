from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='ok,alert', command=self.hello)
        self.alertButton.pack()
        root = Tk()
        self.b1 = Button(root, bitmap="gray50", width=100, height=10)
        self.b1.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

myTk = Tk() # 初始化Tk()
myTk.title("frame-test")    # 设置窗口标题
myTk.geometry("300x200")    # 设置窗口大小 注意：是x 不是*
myTk.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

app = Application(myTk)
app.master.title('Hello World')
app.mainloop()