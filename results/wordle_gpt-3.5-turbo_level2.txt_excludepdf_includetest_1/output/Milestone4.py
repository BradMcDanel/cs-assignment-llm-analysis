from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def enter_action(s):
    # Logic to color the boxes based on correct, present, or missing letters
    # Logic to color the keys based on the letters already used
    pass

def milestone4():
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    milestone4()