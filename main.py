from PIL import Image, ImageDraw

LETTER_VERTICES = [(0, 0), (7, 0), (7, 6), (5, 6), (5, 2), (3, 2), (3, 6),
                   (1, 6), (1, 2), (0, 2)]
PERIOD_VERTICES = [(8, 4), (9, 4), (9, 6), (8, 6)]

WIDTH = 9
HEIGHT = 6
PADDING = 1
SCALE = 100

BACKGROUND_COLOR = 'black'
FOREGROUND_COLOR = 'white'


def translate_vertices(vertices):
    return list(map(lambda v: (v[0] + PADDING, v[1] + PADDING), vertices))


def scale_vertices(vertices):
    return list(map(lambda v: (v[0] * SCALE, v[1] * SCALE), vertices))


def main():
    width = (WIDTH + 2 * PADDING) * SCALE
    height = (HEIGHT + 2 * PADDING) * SCALE
    img = Image.new('1', (width, height), color=BACKGROUND_COLOR)

    draw = ImageDraw.Draw(img)
    letter_vertices = scale_vertices(translate_vertices(LETTER_VERTICES))
    period_vertices = scale_vertices(translate_vertices(PERIOD_VERTICES))
    draw.polygon(letter_vertices, fill=FOREGROUND_COLOR)
    draw.polygon(period_vertices, fill=FOREGROUND_COLOR)

    img.show('N Logo')


if __name__ == '__main__':
    main()