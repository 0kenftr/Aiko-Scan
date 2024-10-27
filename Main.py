from tkinter import *
from tkinter import filedialog
import re
import time
import os

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_file():
    logpath = filedialog.askopenfilename(title="Chọn file log", filetypes=[("Log File", "*.log",)])
    if logpath:
        content = read_txt_file(logpath)
        Log.delete('1.0', END)
        Log.insert('1.0', content)
        #movement modules
        highlight_red("flight")
        highlight_red("Flight")
        highlight_red("fly")
        highlight_red("Fly")
        highlight_red("Speed")
        highlight_red("speed")
        highlight_red("Step")
        highlight_red("step")
        highlight_red("sprint")
        highlight_red("Sprint")
        highlight_red("Packet-fly")
        highlight_red("packet-fly")
        highlight_red("elytra-fly")
        highlight_red("elytra fly")
        #combat modules
        highlight_red("Killaura")
        highlight_red("killaura")
        highlight_red("Kill-aura")
        highlight_red("kill-aura")
        highlight_red("kill aura")
        highlight_red("Kill aura")
        highlight_red("Kill Aura")
        highlight_red("kill Aura")
        highlight_red("aura")
        highlight_red("Aura")
        #addon modules
        highlight_red("Bridgadier Crash")
        highlight_red("Killaura")
        #meteor addon list
        highlight_red("meteor-client")
        highlight_red("meteor-rejects")
        highlight_red("seedcrackerx-api")
        highlight_red("meteorist")
        highlight_red("meteorplus")
        highlight_red("meteor+")
        highlight_red("navine")
        highlight_red("meteorplusplus")
        highlight_red("TrouserStreak")
        highlight_red("trouserstreak")
        highlight_red("Streak")
        highlight_red("streak")
        highlight_red("addon")
        highlight_red("Blackout")
        highlight_red("blackout")
        highlight_red("Vector Addon")
        highlight_red("vector addon")
        highlight_red("vectoraddon")
        highlight_red("serverseeker")
        highlight_red("Meteorist")
        highlight_red("meteorist")
        highlight_red("Orion")
        highlight_red("orion")
        highlight_red("Meteorist enabled")
        highlight_red("Starting navine2!")
        highlight_red("Starting navine3!")
        #client list
        highlight_red("meteor-client")
        highlight_red("Meteor")
        highlight_red("meteor")
        highlight_red("thunderhack")
        highlight_red("thunder-hack")
        highlight_red("Lambda")
        highlight_red("lambda")
        highlight_red("Presstige")
        highlight_red("presstige")
        highlight_red("Blooby")
        highlight_red("blooby")
        #modslist
        highlight_blue("sodium")
        highlight_blue("sodium-extra")
        highlight_blue("fabric-api")
        highlight_blue("servercountryflags")
        #tag
        highlight_orange("xray")
        highlight_red("hack")
        highlight_red("flight")
        highlight_orange("chunkbase")
        highlight_red("seed")
        highlight_red("cheat")
        #addon-warn
        highlight_red("""[14:40:53] [Render thread/WARN]: Failed to load texture: navine:sigma.png
java.io.IOException: Bad PNG Signature""")

#hightlight
def highlight_red(keyword):
    start_pos = '1.0'
    while True:
        start_pos = Log.search(keyword, start_pos, stopindex=END)
        if not start_pos:
            break
        end_pos = f"{start_pos}+{len(keyword)}c"
        Log.tag_add('highlight_red', start_pos, end_pos)
        start_pos = end_pos
    Log.tag_configure('highlight_red', foreground='red')

def highlight_blue(keyword):
    start_pos = '1.0'
    while True:
        start_pos = Log.search(keyword, start_pos, stopindex=END)
        if not start_pos:
            break
        end_pos = f"{start_pos}+{len(keyword)}c"
        Log.tag_add('highlight_blue', start_pos, end_pos)
        start_pos = end_pos
    Log.tag_configure('highlight_blue', foreground='blue')

def highlight_orange(keyword):
    start_pos = '1.0'
    while True:
        start_pos = Log.search(keyword, start_pos, stopindex=END)
        if not start_pos:
            break
        end_pos = f"{start_pos}+{len(keyword)}c"
        Log.tag_add('highlight_orange', start_pos, end_pos)
        start_pos = end_pos
    Log.tag_configure('highlight_orange', foreground='orange')

def highlight_white(keyword):
    start_pos = '1.0'
    while True:
        start_pos = Log.search(keyword, start_pos, stopindex=END)
        if not start_pos:
            break
        end_pos = f"{start_pos}+{len(keyword)}c"
        Log.tag_add('highlight_white', start_pos, end_pos)
        start_pos = end_pos
    Log.tag_configure('highlight_white', foreground='white')

def display_version():
    getlog = Log.get("1.0", "end-1c")
    version_match = re.search(r'Loading Minecraft (\d+\.\d+\.\d+)', getlog)
    if version_match:
        version = version_match.group(1)
    version_label = Label(win, text=f"Version : {version}", font=("Helvetica", 16), bg='#6490FF')
    version_label.place(x=775, y=400, width=150, height=39)

win = Tk()
win.maxsize(height=650, width=1180)
win.minsize(height=650, width=1180)
win.configure(bg='#Ffb6c1')
win.title('Aiko - Scan')

Checkbutton = PhotoImage(file='image/Comp 10.png')
importbutton = PhotoImage(file='image/importbutton.png')

c = Canvas(win, bg="gray16", height=650, width=1180)
c.pack()
frames = [PhotoImage(file=f"image/frame/Comp {i}.png") for i in range(15900, 15959)]

first_frame = c.create_image(0, 0, anchor="nw", image=frames[0])

def animate(frames, delay):
    for frame in frames:
        c.itemconfig(first_frame, image=frame)
        win.update()
        time.sleep(delay)
animate(frames, 0.04167)


# Log
Log = Text(win, wrap='word', width=50, height=10, bg='#A9FFCB', fg='#A9a9a9', bd=0)
Log.place(x=60, y=275, width=640, height=300)

#detect
def detect():
    getlog = Log.get("1.0", "end-1c")
    if "meteor-client" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 16), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "thunderhack" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "thunder-hack" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "boze" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "rise" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "rise6" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "vape-v4" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "vapev4" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "vape" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "bleach-hack" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "bleach" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "liquid-bounce" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "liquid-bounce-plus" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "liquidbounceplus" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "liquidbounce" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "Breeze" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "Trouser-Streak" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "Thunderhack deluxe" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "thunderhack deluxe" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "Thunderhack-deluxe" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "thunderhack-deluxe" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "Pyro" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    if "Lambda" in getlog:
        clientdetect = Label(win, text='Cheat : True', font=("Helvetica", 12), bg='#6490FF')
        clientdetect.place(x=775, y=500, width=125,height=39)
    ## loaer detect
    if "fabric" in getlog:
        loaderdetect = Label(win, text='Loader : Fabric', font=("Helvetica", 16), bg='#6490FF')
        loaderdetect.place(x=770, y=450, width=160, height=39)
    if "forge" in getlog:
        loaderdetect = Label(win, text='Loader : Forge', font=("Helvetica", 16), bg='#6490FF')
        loaderdetect.place(x=768, y=450, width=160, height=39)
    display_version()

# Check button
Check = Button(win, image=Checkbutton, bg='#FFA9F2', activeforeground='#FFA9F2', activebackground='#FFA9F2', border=0, command=detect)
Check.place(x=775, y=260, height=45, width=160)

# Import file txt vào log
importlog = Button(win, image=importbutton, command=load_file, bd=0, bg='#FFA9F2', activebackground='#FFA9F2', activeforeground='#FFA9F2')
importlog.place(x=947, y=260, height=45, width=160)

win.mainloop()
