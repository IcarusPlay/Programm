import tkinter as tk
from tkinter import messagebox
import Spam
import threading

# Глобальная переменная для события остановки, чтобы функция stop() имела к нему доступ
stop_event = None

def start():
    message = message_entry.get()
    random_text = random_entry.get()
    count_str = count_entry.get()
    delay_str = delay_entry.get()

    if not message or not count_str:
        messagebox.showerror("Ошибка", "Поля 'Основное сообщение' и 'Количество сообщений' должны быть заполнены.")
        return

    # Отфильтровываем пустые элементы, чтобы избежать добавления лишних пробелов
    random_messages = [word.strip() for word in random_text.split(',') if word.strip()]

    try:
        count = int(count_str)
        if count <= 0:
            messagebox.showerror("Ошибка", "Количество должно быть положительным числом.")
            return
    except ValueError:
        messagebox.showerror("Ошибка", "Количество должно быть целым числом.")
        return

    try:
        delay = float(delay_str)
        if delay < 0:
            messagebox.showerror("Ошибка", "Задержка не может быть отрицательной.")
            return
    except (ValueError, TypeError):
        messagebox.showerror("Ошибка", "Задержка должна быть числом.")
        return

    # Блокируем кнопку, чтобы избежать повторных нажатий
    global stop_event
    stop_event = threading.Event()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

    def update_status(text):
        """Безопасно обновляет статус из другого потока."""
        status_label.config(text=text)

    def spam_task_wrapper():
        try:
            # Передаем событие и функцию обратного вызова в задачу
            Spam.start_spam(message, random_messages, count, delay, stop_event, lambda text: root.after(0, update_status, text))
        finally:
            # Возвращаем кнопку в активное состояние в основном потоке GUI
            root.after(0, lambda: (
                start_button.config(state=tk.NORMAL),
                stop_button.config(state=tk.DISABLED)
            ))

    # Запускаем задачу в отдельном потоке, чтобы не блокировать интерфейс
    threading.Thread(target=spam_task_wrapper, daemon=True).start()

def stop():
    """Устанавливает событие для остановки спама."""
    if stop_event:
        stop_event.set()

root = tk.Tk()
root.title("Spammer")
root.geometry("400x350")
root.resizable(False, False)

title = tk.Label(root, text="Spam Sender", font=("Arial", 16))
title.pack(pady=10)

tk.Label(root, text="Основное сообщение").pack()
message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

tk.Label(root, text="Рандомные сообщения (через запятую)").pack()
random_entry = tk.Entry(root, width=40)
random_entry.pack(pady=5)

tk.Label(root, text="Количество сообщений").pack()
count_entry = tk.Entry(root, width=10)
count_entry.pack(pady=5)

tk.Label(root, text="Задержка между сообщениями (сек)").pack()
delay_entry = tk.Entry(root, width=10)
delay_entry.insert(0, "0.5") # Значение по умолчанию
delay_entry.pack(pady=5)

start_button = tk.Button(root, text="Начать спам", width=20, command=start)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Остановить", width=20, command=stop, state=tk.DISABLED)
stop_button.pack()

status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=10)

root.mainloop()