from WordleGraphics import WordleGWindow

def color_boxes(gw, color_map):
    for row in range(len(color_map)):
        for col in range(len(color_map[row])):
            gw.set_square_color(row, col, color_map[row][col])

if __name__ == "__main__":
    gw = WordleGWindow()
    color_map = [[...], [...], ...]  # Define color mapping based on the guess
    color_boxes(gw, color_map)