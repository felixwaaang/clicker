import pyautogui
import time


# try:
#     while True:
#         x, y = pyautogui.position()
#         print(f"Mouse position: ({x}, {y})")
# except KeyboardInterrupt:
#     print("Program stopped.")




x_list = [-1130]
y_list = [425]

pyautogui.moveTo(x_list[0], y_list[0])
pyautogui.click()
pyautogui.scroll(-50)

for i in range(5):
    x = x_list[0]
    y = y_list[0]

    pyautogui.moveTo(x, y)

    # Perform the click
    pyautogui.click()
    time.sleep(0.5)

    pyautogui.scroll(-50)
