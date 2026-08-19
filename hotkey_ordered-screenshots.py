import pyautogui
import keyboard
from pathlib import Path

# Create folder
output_folder = Path("screenshots")
output_folder.mkdir(exist_ok=True)

counter = 1

def take_screenshot():
    global counter

    filename = output_folder / f"screenshot_{counter:03d}.png"

    pyautogui.screenshot(
        str(filename),
#        region=(x, y, width, height)
    )

    print(f"Saved {filename.name}")

    counter += 1

print("F8 = screenshot")
print("ESC = finish")

keyboard.add_hotkey("f8", take_screenshot)

keyboard.wait("esc")

print("Finished")