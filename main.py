from PIL import Image, ImageDraw

LETTER_VERTICES = [(0, 0), (7, 0), (7, 6), (5, 6), (5, 2), (3, 2), (3, 6),
                   (1, 6), (1, 2), (0, 2)]
PERIOD_VERTICES = [(8, 4), (9, 4), (9, 6), (8, 6)]

WIDTH = 9
HEIGHT = 6
ASPECT_RATIO = WIDTH / HEIGHT


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


def generate(width, height, padding=0, bgcolor='black'):
    (target_width, target_height) = get_target_dimensions(
        width, height, padding)

    scale = target_width / WIDTH

    letter_vertices = scale_vertices(LETTER_VERTICES, scale)
    period_vertices = scale_vertices(PERIOD_VERTICES, scale)

    img = Image.new('1', (width, height), color=bgcolor)

    draw = ImageDraw.Draw(img)
    draw.polygon(letter_vertices, fill=FOREGROUND_COLOR)
    draw.polygon(period_vertices, fill=FOREGROUND_COLOR)

    transform_params = get_transform_params(width, height, target_width,
                                            target_height)

    img = img.transform(img.size, Image.AFFINE, transform_params)

    img.show('N Logo')


if __name__ == '__main__':
    generate(460, 460, 50)  # TODO: use argparse
