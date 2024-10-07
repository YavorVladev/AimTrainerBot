import pyautogui
import time
import keyboard
import win32api, win32con


time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


#     rgb(255, 86, 32) center

while not keyboard.is_pressed('q'):
    pic = pyautogui.screenshot(region=(550, 365, 800, 482))
    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))

            if r == 255:
                if (g in range(86, 88)):
                    if (b in range(30, 35)):
                        click(x + 550, y + 365)
                        # time.sleep(0.00001)
                        break
