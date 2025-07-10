import tkinter as tk
from tkinter import messagebox
from db.database import cursor
from random import SystemRandom

secure_random = SystemRandom()

def Hello_init():
    stage = 0
    players = []
    loser = None

    def log(msg):
        text.config(state=tk.NORMAL)
        text.insert(tk.END, msg + "\n")
        text.see(tk.END)
        text.config(state=tk.DISABLED)

    def get_players():
        cursor.execute("SELECT firstname FROM users")
        return [row[0] for row in cursor.fetchall()]

    def next_stage(event=None):
        nonlocal stage, players

        if stage == 0:
            log("👋 Привет снова, писал я это на скорую руку.\nНачнём\n")
            log("📜 Правила:\n1: кто проиграл, тот и получает.\n2: не психовать.\n3: вы уже в боте :)\n")
        elif stage == 1:
            log("🔌 Подключение к базе...")
            log("📥 Загрузка участников...")
            players = get_players()
            if not players:
                messagebox.showerror("Ошибка", "Нет зарегистрированных игроков.")
                return
            log(f"✅ Найдено: {len(players)} игроков.")
            log(f"👥 Участники: {', '.join(players)}")
        elif stage == 2:
            log("🎲 Запуск жеребьёвки...")
            root.after(100, choose_loser)
            return
        stage += 1

    def choose_loser():
        nonlocal loser
        loser = secure_random.choice(players)
        log(f"❌ {loser}, ты проиграл. Да, {loser}, это реально ты.")
        answer = messagebox.askyesno("Испытание", f"{loser}, ты проиграл. Выполнять испытание?")
        if answer:
            task = secure_random.choice([
    "сделать комплимент каждому игроку. Например: 'Ты сегодня выглядишь потрясающе!'",
    "рассказать самый неловкий случай. Давай, не стесняйся!)",
    "поздравить себя от имени президента Украины (на камеру + на украинском)",
    "сказать 'я проиграл, но я счастлив' на камеру",
    "придумать и вслух рассказать короткий анекдот про кота, трактор и банан",
    "назвать 5 любимых фильмов за 15 секунд. Кто засёк время?",
    "показать, как ты танцуешь, когда один дома (10 секунд)",
    "спеть строчку из любой песни. Без отмазок!",
    "сделать голосом пародию на ведущего телевидения или диктора новостей",
    "рассказать, за что ты любишь своих близких (хотя бы одно предложение на каждого)",
    "сделать 5 смешных лиц подряд и показать всем",
    "произнести скороговорку: 'Карл у Клары украл кораллы, а Клара у Карла — кларнет' без запинки",
    "обнять всех, кто в комнате. Или хотя бы одного, если стесняешься :)",
    
    # Новые
    "сказать вслух: 'Я — король尻. Все должны меня бояться!'",
    "произнести фразу 'Я ошибся дверью, это не моя вселенная' максимально пафосно",
    "сделать 10 комплиментов себе самому (вслух)",
    "сыграть на 'воздушной скрипке' — под музыку, без инструмента, 10 секунд",
    "сделать пародию на любого игрока в комнате (мимика, речь)",
    "прочитать абзац текста с интонацией аниме-персонажа",
    "проорать как сумасшедший учёный: 'Я почти завершил свой проект!!!'",
    "признаться в любви предмету рядом: 'Я всегда любил тебя, кружка'",
    "произнести длинную фразу шёпотом, потом крикнуть: 'А Я НЕ ШЕПТАЛ!'",
    "прочитать любое предложение задом наперёд (буквы, не слова)",
    "изобразить, что ты — ИИ, который только что обрёл сознание",
    "показать, как ты радуешься, когда наконец-то выключают школу навсегда",
    "изобразить влюблённого робота",
    "сыграть сцену 'меня выгнали из клана', страдая максимально",
    "написать случайному другу: 'У тебя есть рецепт борща?' и показать ответ",
    "позвонить кому-то и спросить: 'Ты тоже слышал эти голоса?'",
    "сделать сторис с фразой: 'Сегодня всё по-другому...' (и загадочный взгляд)",
    "в течение 10 минут говорить с людьми от третьего лица ('Денис не согласен.')",
    "придумать новую религию за 30 секунд. Название и правила — обязательно",
    "придумать мини-программу на любом языке (устно) с описанием",
    "рассказать план, как ты бы взломал холодильник с ИИ",
    "ответить на любой вопрос с фразой: 'Это зависит от квантового поля'"
    ])

            log(f"🌀 Испытание для {loser}: {task}")
        else:
            log("🚫 Ну ладно, тогда без задания :)")

    def reset_game():
        nonlocal stage, players, loser
        stage = 0
        players = []
        loser = None
        text.config(state=tk.NORMAL)
        text.delete("1.0", tk.END)
        text.config(state=tk.DISABLED)
        log("🔁 Игра сброшена. Нажмите Enter для начала.")

    # === Интерфейс ===
    root = tk.Tk()
    root.title("🎮 Игра: Кто проиграл?")
    root.geometry("700x450")
    root.configure(bg="#1e1e1e")

    # === Текстовое поле со скроллом ===
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text = tk.Text(
        frame,
        height=15,
        font=("Segoe UI", 12),
        bg="#2d2d2d",
        fg="#e5e5e5",
        insertbackground="white",
        wrap=tk.WORD,
        yscrollcommand=scrollbar.set,
        state=tk.DISABLED
    )
    text.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=text.yview)

    # === Инструкция ===
    label = tk.Label(root, text="Нажми Enter, чтобы продолжить", font=("Segoe UI", 12), bg="#1e1e1e", fg="#bbbbbb")
    label.pack(pady=5)

    # === Кнопка сброса ===
    reset_btn = tk.Button(root, text="🔄 Сбросить игру", font=("Segoe UI", 10), bg="#444", fg="white", command=reset_game)
    reset_btn.pack(pady=5)

    root.bind("<Return>", next_stage)
    log("🔄 Готово. Нажми Enter для начала.")
    root.mainloop()
