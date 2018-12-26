import argparse

from PIL import Image, ImageDraw

LETTER_VERTICES = [(0, 0), (7, 0), (7, 6), (5, 6), (5, 2), (3, 2), (3, 6),
                   (1, 6), (1, 1), (0, 1)]
PERIOD_VERTICES = [(8, 5), (9, 5), (9, 6), (8, 6)]

WIDTH = 9
HEIGHT = 6
ASPECT_RATIO = WIDTH / HEIGHT

COLOR_BLACK = 'black'
COLOR_WHITE = 'white'


def get_target_dimensions(width, height, padding):
    actual_width = width - padding
    actual_height = height - padding
    aspect_ratio = width / height

    target_width = actual_width
    target_height = actual_height

    if aspect_ratio < ASPECT_RATIO:
        target_height = actual_width / ASPECT_RATIO
    else:
        target_width = actual_height * ASPECT_RATIO

    return (target_width, target_height)


def scale_vertices(vertices, scale):
    return list(map(lambda v: (v[0] * scale, v[1] * scale), vertices))


def get_transform_params(width, height, target_width, target_height):
    x_offset = (width - target_width) / 2
    y_offset = (height - target_height) / 2

    return (1, 0, -x_offset, 0, 1, -y_offset)


def generate(width, height, padding, bgcolor, preview=False):
    (target_width, target_height) = get_target_dimensions(
        width, height, padding)

    scale = target_width / WIDTH

    letter_vertices = scale_vertices(LETTER_VERTICES, scale)
    period_vertices = scale_vertices(PERIOD_VERTICES, scale)

    img = Image.new('1', (width, height), color=bgcolor)

    fgcolor = COLOR_WHITE if bgcolor == COLOR_BLACK else COLOR_BLACK

    draw = ImageDraw.Draw(img)
    draw.polygon(letter_vertices, fill=fgcolor)
    draw.polygon(period_vertices, fill=fgcolor)

    transform_params = get_transform_params(width, height, target_width,
                                            target_height)

    img = img.transform(
        img.size, Image.AFFINE, transform_params, fillcolor=bgcolor)

    if preview:
        img.show('N. Logo')
    else:
        img.save('logo.png', format='png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate N. Logo and save to file logo.png')

    parser.add_argument(
        'width', type=int, help='Width of output file in pixels')
    parser.add_argument(
        'height', type=int, help='Height of output file in pixels')
    parser.add_argument(
        '-p',
        '--padding',
        nargs='?',
        default=0,
        type=int,
        help='Padding on all sides in pixels')
    parser.add_argument(
        '-b',
        '--bgcolor',
        nargs='?',
        default='black',
        choices=['black', 'white'],
        help='Background color for logo')
    parser.add_argument(
        '-v',
        '--preview',
        action='store_true',
        help='Preview logo instead of saving to file')

    args = parser.parse_args()

    generate(args.width, args.height, args.padding, args.bgcolor, args.preview)
 