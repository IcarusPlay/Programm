import keyboard
import time
import random

def start_spam(message, random_messages, count, delay, stop_event, status_callback):
    """
    Основная функция для отправки сообщений.
    :param message: Основной текст сообщения.
    :param random_messages: Список случайных слов для добавления.
    :param count: Количество сообщений для отправки.
    :param delay: Задержка между сообщениями в секундах.
    :param stop_event: threading.Event для прерывания цикла.
    :param status_callback: Функция для отправки обновлений статуса в GUI.
    """
    status_callback("Переключитесь на нужное окно. Отправка начнется через 5 секунд.")
    time.sleep(5)

    if stop_event.is_set():
        status_callback("Отправка отменена до начала.")
        return

    for i in range(count):
        if stop_event.is_set():
            status_callback(f"Отправка остановлена. Отправлено {i} из {count}.")
            return

        status_callback(f"Отправка сообщения {i + 1} из {count}...")
        # пишем основное сообщение
        keyboard.write(message)

        # если есть случайные слова — добавляем
        if random_messages:
            random_word = random.choice(random_messages)
            keyboard.write(" " + random_word)

        keyboard.press_and_release("enter")
        time.sleep(delay) # Пауза между сообщениями

    status_callback(f"Готово! Отправлено {count} сообщений.")