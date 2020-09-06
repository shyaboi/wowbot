import autopy
import random
import time
import pyautogui


autopy.key.tap(autopy.key.Code.TAB, [autopy.key.Modifier.ALT])
print(pyautogui.position())
print(pyautogui.size())
print(pyautogui.onScreen(400, 400))
time.sleep(1)
# pyautogui.press('w')

pyautogui.keyDown('w')
time.sleep(2)
pyautogui.keyUp('w')

pyautogui.keyDown('w')
time.sleep(2)
pyautogui.keyUp('w')
time.sleep(2)
pyautogui.keyUp('a')
time.sleep(2)
pyautogui.keyDown('w')

time.sleep(2)
pyautogui.keyUp('w')

pyautogui.keyDown('d')
pyautogui.keyUp('d')

pyautogui.keyDown('w')

# def mousLoc():
#     print(autopy.mouse.location())
    
# def rightJerk():
#     autopy.mouse.move(1200, 500)
#     mousLoc()
#     autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
#     autopy.mouse.toggle(autopy.mouse.Button.RIGHT, True)
#     autopy.mouse.smooth_move(1270, 500)
#     mousLoc()
#     autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)
#     autopy.mouse.toggle(autopy.mouse.Button.RIGHT, False)
# def leftJerk():
#     autopy.mouse.move(1200, 500)
#     mousLoc()
#     autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
#     autopy.mouse.toggle(autopy.mouse.Button.RIGHT, True)
#     autopy.mouse.smooth_move(1135, 500)
#     mousLoc()
#     autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)
#     autopy.mouse.toggle(autopy.mouse.Button.RIGHT, False)
# def autoRun():
#     autopy.key.tap(autopy.key.Code.UP_ARROW)
# def jumpy():
#     autopy.key.tap(autopy.key.Code.SPACE)



# def wow():
#     # autopy.mouse.move(600, 600)
#     # autopy.mouse.click()
#     autopy.key.tap(autopy.key.Code.TAB, [autopy.key.Modifier.ALT])
#     time.sleep(1)
#     mousLoc()
#     autoRun()
#     time.sleep(3.5)
#     rightJerk()
#     rightJerk()
#     rightJerk()
#     rightJerk()
#     rightJerk()
#     autoRun()
#     time.sleep(1)
#     rightJerk()
#     autoRun()
#     time.sleep(5)
#     leftJerk()
#     leftJerk()
#     leftJerk()
#     autoRun()
#     jumpy()
#     time.sleep(12)
#     rightJerk()
#     autoRun()
#     jumpy()
#     time.sleep(42)
#     leftJerk()
#     leftJerk()
#     leftJerk()
#     autoRun()
#     jumpy()
#     time.sleep(8)
#     leftJerk()
#     leftJerk()
#     autoRun()
#     jumpy()
#     time.sleep(2)
#     leftJerk()
#     leftJerk()
#     autoRun()
#     jumpy()
#     time.sleep(13)
#     leftJerk()
#     leftJerk()
#     autoRun()
#     jumpy()
# wow()