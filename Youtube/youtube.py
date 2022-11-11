import pyautogui,time,keyboard



alwaystrue = True

if keyboard.is_pressed("z"):

    alwaystrue = False

while alwaystrue == True:
  time.sleep(1)
  pyautogui.hotkey('Ctrl', 't')
  pyautogui.hotkey('Ctrl', 'l')
  pyautogui.typewrite("https://www.youtube.com/feed/channels")
  pyautogui.press('Enter')
  time.sleep(2)
  pyautogui.moveTo(1549, 226)
  pyautogui.click()
  pyautogui.moveTo(1056, 616)
  pyautogui.click()
  pyautogui.hotkey('Ctrl', 'w')