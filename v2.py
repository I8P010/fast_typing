import random
import time
import pyautogui
import json

pyautogui.FAILSAFE = True

def type_with_human_simulation(
    text, target_wpm, wpm_deviation, accuracy, time_sleep
):
  for i in range(time_sleep, 0, -1):
    print(f'Старт через {i}...')
    time.sleep(1)

  print('Печать началась...')

  # Алфавит для генерации случайных «ошибочных» букв при добавлении лишних символов
  typo_chars = 'abcdefghijklmnopqrstuvwxyz'
  res_text = ""

  for char in text:
    if random.random() > accuracy and char.isalpha():
      wrong_char = random.choice(typo_chars)
      res_text += wrong_char
    res_text+=char

  WPM = random.uniform(target_wpm, target_wpm+wpm_deviation)
  pyautogui.write(res_text, interval=60/(WPM*5))

  print('\nГотово! Текст успешно введен с вариативной скоростью и ошибками.')


if __name__ == '__main__':
  sample_text = ""
  with open("text.txt") as f:
    sample_text = f.read()

  settings = None
  with open("settings.json") as s:
    settings = json.load(s)
    
  # Настройки:
  TARGET_WPM = settings["wpm"]  # Средняя скорость
  WPM_DEVIATION = settings["deviation"]  # Разброс скорости
  ACCURACY = settings["accuracy"]  # Точность
  TIME_SLEEP = settings["start_time"]

  type_with_human_simulation(
      sample_text,
      target_wpm=TARGET_WPM,
      wpm_deviation=WPM_DEVIATION,
      accuracy=ACCURACY,
      time_sleep=TIME_SLEEP
  )