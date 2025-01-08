import pywhatkit # type: ignore
import pyautogui # type: ignore
import time
pywhatkit.sendwhatmsg('+917539966891', "Hello from Ramesh", 13, 30)
time.sleep(60)
pyautogui.press('enter')
print("Successfully Sent!")