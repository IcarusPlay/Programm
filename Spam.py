#Библиотеки
import keyboard
import time

print("Переключитесь на нужное окно. Отправка начнется через 5 секунд.")
#Через сколько он начнет спам
time.sleep(5)

# Текст, который будет отравляться
message = ("Сообщение")
# Сам скрипт отправки
for i in range(5):
    keyboard.write(message)
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    # Пауза перед отправкой следующего сообщения
    time.sleep(0.1)
print("Скрипт завершил работу.")