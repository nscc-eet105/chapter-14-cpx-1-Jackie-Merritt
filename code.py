from adafruit_circuitplayground import cp
#Jackie-Merritt_Chp14-CPX1_7/14/2025


notes = {"A4": 440, "B4": 494, "F5": 698, "G5": 784}

color = {"black": (0, 0, 0), "green": (0, 50, 0), "purple": (50, 0, 50), "yellow": (50, 50, 0), "cyan": (0, 50, 50)}

def fill_pixels(color):
    for num in range(0, 10):
        cp.pixels[num] = color

while True:
    if cp.touch_A1:
        cp.start_tone(notes["A4"])
        fill_pixels(color["green"])
    elif cp.touch_A3:
        cp.start_tone(notes["B4"])
        fill_pixels(color["purple"])
    elif cp.touch_A4:
        cp.start_tone(notes["F5"])
        fill_pixels(color["yellow"])
    elif cp.touch_A6:
        cp.start_tone(notes["G5"])
        fill_pixels(color["cyan"])
    else:
        cp.stop_tone()
        fill_pixels(color["black"])

