import pyautogui
import pyperclip
import time

# Step 1: Click at whatsapp icon (1018, 740)
pyautogui.click(1018, 740)
time.sleep(0.5)  # Wait for any UI response

# Step 2: Click and Drag from (442, 109) to (1303, 65)
pyautogui.moveTo(442, 109)
pyautogui.mouseDown()
pyautogui.moveTo(1303, 65, duration=0.5)  # Smooth movement
pyautogui.mouseUp()
time.sleep(0.3)

# Step 3: Copy to Clipboard (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Allow time for clipboard to update

# Step 4: Retrieve copied text
copied_text = pyperclip.paste()

print(copied_text)
