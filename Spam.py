#Библиотеки
import keyboard
import time
import random

print("Переключитесь на нужное окно. Отправка начнется через 5 секунд.")
#Через сколько он начнет спам
time.sleep(5)

# Текст, который будет отравляться
message = ("Сообщение")
#Случайные слова
random_message = ("1 вариант","2 вариант","3 вариант") #Что бы добавить больше сообщений просто
                                                        # сделай CTRL + C, CTRL +V одного из вариантов
                                                        #и про запятую не забудь

# Сам скрипт отправки
for i in range(5): #Количество
    keyboard.write(message)
    time.sleep(0.5)
    keyboard.write(random.choice(random_message)) # Скрипт случайных слов
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    # Пауза перед отправкой следующего сообщения
    time.sleep(0.1)
print("Скрипт завершил работу.")