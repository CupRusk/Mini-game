import tkinter as tk
import threading
from logic.telegram_bot import init_tgBot
from logic.hello import Hello_init

BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
BTN_COLOR = "#3a3a3a"
HOVER_COLOR = "#505050"
FONT = ("Segoe UI", 12)

def run_hello():
    output_label.config(text="🔵 Запуск Hello-интерфейса...")
    Hello_init()

def run_telegram():
    output_label.config(text="🔵 Запуск Telegram-бота...")
    threading.Thread(target=lambda: init_tgBot(['BOT-TOKEN'])).start()

def exit_app():
    output_label.config(text="🚪 Выход...")
    root.after(800, root.destroy)

def on_hover(e):
    e.widget.config(bg=HOVER_COLOR)

def on_leave(e):
    e.widget.config(bg=BTN_COLOR)

# Создание окна
root = tk.Tk()
root.title("Mini-Game App")
root.geometry("400x300")
root.config(bg=BG_COLOR)
root.resizable(False, False)

title = tk.Label(root, text="Выбери действие", font=("Segoe UI", 16), fg=FG_COLOR, bg=BG_COLOR)
title.pack(pady=20)
# Кнопочки, нужно ли коментировать их?
btn_hello = tk.Button(root, text="▶ Hello-игра", font=FONT, bg=BTN_COLOR, fg=FG_COLOR, bd=0, command=run_hello)
btn_telegram = tk.Button(root, text="✉ Telegram-бот", font=FONT, bg=BTN_COLOR, fg=FG_COLOR, bd=0, command=run_telegram)
btn_exit = tk.Button(root, text="❌ Выход", font=FONT, bg=BTN_COLOR, fg=FG_COLOR, bd=0, command=exit_app)

for btn in (btn_hello, btn_telegram, btn_exit):
    btn.pack(pady=5, ipadx=10, ipady=5)
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)

# Лейбл для вывода статуса
output_label = tk.Label(root, text="", font=("Consolas", 11), fg=FG_COLOR, bg=BG_COLOR)
output_label.pack(pady=15)

root.mainloop()
