#tasklist | findstr python

import tkinter as tk
from time import strftime
import keyboard

def close_all(event=None):

    try:
        main_root.destroy()
    except tk.TclError:
        pass # 이미 창이 닫힌 경우 오류 무시



main_root = tk.Tk()
main_root.overrideredirect(True)  # 창 테두리, 제목  제거
main_root.wm_attributes("-topmost", 1) # 항상 위에 표시


def time_update():
    try:
        current_time = strftime('%H:%M:%S')
        time_label.config(text=current_time)
        time_label.after(1000, time_update) # 1초마다 업데이트
    except tk.TclError:
        pass 
        
transparent_color = 'black'
main_root.wm_attributes('-transparentcolor', transparent_color)

time_label = tk.Label(main_root, font=('Consolas', 20, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')
main_root.resizable(width=False, height=False)

main_root.bind('<Escape>', close_all)
keyboard.add_hotkey('win+esc', close_all)

time_update()

main_root.update() # 창 업데이트 필요함?
screen_width = main_root.winfo_screenwidth()
window_width = main_root.winfo_width()


# 좌표 고정이 모니터에 맞게 작동안하는거 같음 
x_coordinate = (screen_width // 2) - 100 
y_coordinate = -8
main_root.geometry(f"+{x_coordinate}+{y_coordinate}")



main_root.mainloop()
