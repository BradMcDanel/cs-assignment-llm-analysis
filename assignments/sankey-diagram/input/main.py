import sys
import os
from SimpleGraphics import *
from math import pi, sin

def load_data(file):
    with open(file, 'r') as f:
        title = f.readline().strip()
        source_label = f.readline().strip()
        data = {}
        for line in f:
            parts = line.strip().split(',')
            if len(parts) < 2:
                continue
            destination = parts[0]
            flow = float(parts[1])
            data[destination] = flow
    return title, source_label, data


def interpolate_color(color1, color2, t):
    return tuple(int(c1 + (c2 - c1) * t) for c1, c2 in zip(color1, color2))

def draw_sankey(title, source_label, data):
    total_flow = sum(data.values())
    num_dests = len(data)
    num_available_pixels = 450 - (num_dests - 1) * 10
    num_pixels_per_flow = num_available_pixels / total_flow
    heights = {}
    src_height = total_flow * num_pixels_per_flow
    src_offset = 100
    dst_offset = 50
    y = 0

    # Define colors
    source_color = (200, 200, 200)  # Light gray for source
    destination_colors = [
        (255, 99, 71),   # Tomato
        (50, 205, 50),   # Lime Green
        (30, 144, 255),  # Dodger Blue
        (255, 215, 0),   # Gold
        (138, 43, 226),  # Blue Violet
        (255, 127, 80),  # Coral
        (0, 255, 127),   # Spring Green
        (255, 0, 255),   # Magenta
        (0, 255, 255),   # Cyan
        (255, 165, 0),   # Orange
        (128, 0, 128),   # Purple
        (0, 128, 128),   # Teal
    ]

    for destination, flow in data.items():
        height = flow * num_pixels_per_flow
        heights[destination] = height
        y += height + 10

    setFont("Arial", "12")
    setColor(0, 0, 0)

    # Draw the source bar
    setFill(*source_color)
    rect(100, src_offset, 50, src_height)
    setColor(0, 0, 0)
    midy = src_offset + src_height / 2
    text(95, midy, source_label, align="e")
    
    # Draw the destination bars
    y = dst_offset
    for i, (destination, height) in enumerate(heights.items()):
        color = destination_colors[i % len(destination_colors)]
        setFill(*color)
        rect(500, y, 50, height)
        setColor(0, 0, 0)
        midy = y + height / 2
        text(555, midy, destination, align="w")
        y += height + 10

    # Draw the title
    setFont("Arial", "16")
    text(400, 25, title)

    # Draw gradient connections
    src_y = src_offset
    dst_y = dst_offset
    for i, (destination, height) in enumerate(heights.items()):
        dst_color = destination_colors[i % len(destination_colors)]
        for x in range(150, 501, 5):
            t = (x - 150) / 350
            t = (sin(t * pi - pi/2) + 1) / 2  # Apply sine curve
            color = interpolate_color(source_color, dst_color, t)
            setFill(*color)
            setOutline(*color)
            y1 = src_y + (dst_y - src_y) * t
            y2 = (src_y + height) + ((dst_y + height) - (src_y + height)) * t
            rect(x, y1, 5, y2 - y1)

        dst_y += height + 10
        src_y += height

    # Draw black outlines
    # setColor(0, 0, 0)
    # setFill(None)
    # rect(100, src_offset, 50, src_height)
    # y = dst_offset
    # for height in heights.values():
    #     rect(500, y, 50, height)
    #     y += height + 10
    # line(150, src_offset, 500, dst_offset)
    # line(150, src_offset + src_height, 500, y - 10)



def main():
    if len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit(1)

    if len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        file = input("Enter the file name: ")

    if not os.path.exists(file):
        print("File does not exist")
        sys.exit(1)

    title, source_label, data = load_data(file)
    print(data)
    setWindowTitle(title)
    draw_sankey(title, source_label, data)

main()

