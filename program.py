import random
import time
import pyautogui
import json
import logging

pyautogui.FAILSAFE = True
logging.basicConfig(
	filename="log.txt", 
	format='[%(asctime)s] : %(levelname)s - %(message)s',  # Шаблон строки лога
	datefmt='%d.%m.%Y %H:%M:%S',  # Формат даты и времени
	encoding='utf-8',  # Кодировка для корректного отображения кириллицы
    level=logging.INFO
)

def type_with_human_simulation(
    text, target_wpm, wpm_deviation, accuracy, time_sleep
):
  logging.info(f"Инициализация.")

  # Алфавит для генерации случайных «ошибочных» букв при добавлении лишних символов
  typo_chars = 'abcdefghijklmnopqrstuvwxyz'
  res_text = ""

  for char in text:
    if random.random() > accuracy and char.isalpha():
      wrong_char = random.choice(typo_chars)
      res_text += wrong_char
    res_text+=char
    
  WPM = random.uniform(target_wpm, target_wpm+wpm_deviation)

  logging.info(f"TARGET WPM: {target_wpm} | REAL WPM: {WPM:.3f} | DEVIATION: {wpm_deviation} | ACCURACY: {accuracy*100}%")
  logging.info(f"До старта {time_sleep}с.")

  time.sleep(time_sleep)

  logging.info(f"Печать началась.")

  pyautogui.write(res_text, interval=60/(WPM*5))

  logging.info("Текст успешно введён.")


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
