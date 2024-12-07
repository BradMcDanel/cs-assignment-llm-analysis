from WordleGraphics import WordleGWindow

def color_keys(gw, key_color_map):
    for key, color in key_color_map.items():
        gw.set_key_color(key, color)

if __name__ == "__main__":
    gw = WordleGWindow()
    key_color_map = {...}  # Define key-color mapping based on user input
    color_keys(gw, key_color_map)