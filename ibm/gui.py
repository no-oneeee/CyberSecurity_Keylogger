from tkinter import *
import tkmacosx
import subprocess
import psutil
program_process = None

def start_program():
    button1.config(bg='green', activebackground='green')
    global program_process
    if program_process is None or program_process.poll() is not None:
        program_process = subprocess.Popen(["python3", "keylogger.py"])

def stop_program():
    button1.config(bg='white', activebackground='white')
    global program_process
    if program_process is not None and program_process.poll() is None:
        process = psutil.Process(program_process.pid)
        for child in process.children(recursive=True):
            child.terminate()
        process.terminate()
        program_process = None

window = Tk()
window.geometry("500x200")
window.title("Keylogger")
my_frame = Frame(window)
my_frame.pack(fill=BOTH, expand=True)
my_frame.config(bg='#dfc5fe')
button1 = tkmacosx.Button(my_frame, text = "Start", command=start_program, width=90, bg="white")
button1.place(x=130, y=80)
button2 = tkmacosx.Button(my_frame, text = "Stop", command=stop_program, width=90, bg="white")
button2.place(x=280, y=80)

window.mainloop()
