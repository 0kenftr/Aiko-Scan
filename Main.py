from tkinter import *
from tkinter import filedialog

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_file():
    file_path = filedialog.askopenfilename(title="Chọn log", filetypes=[("Text Files", "*.log")])
    if file_path:
        content = read_txt_file(file_path)
        Log.insert('1.0', content)

win = Tk()
win.maxsize(height=522, width=1008)
win.minsize(height=522, width=1008)
win.configure(bg='#Ffb6c1')
win.title('Aiko - Scan')

Checkbutton = PhotoImage(file='image/Comp 10.png')
AikoLogo = PhotoImage(file='image/Aikologo.png')
importbutton = PhotoImage(file='image/importbutton.png')
#logo
Logo = Label(win, bg='#Ffb6c1', image=AikoLogo)
Logo.place(x=700, y=20, height=200, width=200)
#log
Log = Text(win, wrap='word', width=50, height=10, bg='#ABF97A')
Log.place(x=0, y=0, width=620, height=522)

#check
def Cheatcheck():
    getlog = Log.get("1.0", "end-1c")
    print('đã chạy')
    if "meteor-client" in getlog:
        Meteordetect = Label(win, text='Phát hiện meteor client', font=("Helvetica", 14), bg='#Ffb6c1')
        Meteordetect.place(x=650, y=300, width=200, height=39)
        print('phát hiện meteor client')

#check button
Check = Button(win, image=Checkbutton, bg='#Ffb6c1', activeforeground='#Ffb6c1', activebackground='#Ffb6c1', border=0, command=Cheatcheck)
Check.place(x=650, y=200, height=45, width=160)

#import file txt vào log
importlog = Button(win, image=importbutton, command=load_file, bd = 0, bg = '#Ffb6c1', activebackground='#Ffb6c1', activeforeground='#Ffb6c1')
importlog.place(x=815, y=200, height=45, width=160)

win.mainloop()
