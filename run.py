import pyautogui
import keyboard
import time

def main():
    for i in range(5, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)

    while not keyboard.is_pressed("q"):
        pyautogui.click()

main()
