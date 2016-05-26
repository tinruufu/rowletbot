from tempfile import mkstemp
import os
from random import random

from PIL import Image


ROWLET_PATH = os.path.join(os.path.dirname(__file__), 'rowlet.png')


def random_square_within(source_size):
    size = int((0.2 + random() * 0.8) * source_size)
    neutral_padding = (source_size - size)/2

    return (
        neutral_padding, neutral_padding,
        source_size-neutral_padding,
        source_size-neutral_padding,
    )


def _make_avatar():
    bg = '#fff'
    orig = Image.open(ROWLET_PATH)
    assert orig.width == orig.height
    flattened = Image.alpha_composite(Image.new('RGBA', orig.size, bg), orig)

    i = Image.new('RGB', (orig.width * 3, orig.height * 3), bg)
    vertical_offset = int(orig.height + random() * orig.height/2)
    i.paste(flattened, (int(orig.width), vertical_offset))

    i = i.crop(random_square_within(i.width))
    i = i.rotate(random() * 360, Image.BICUBIC)

    # then shrink further, because rotation has edges
    rotation_padding = int(i.width/4)
    i = i.crop((rotation_padding, rotation_padding,
                i.width-rotation_padding, i.width-rotation_padding))

    return i


def make_avatar():
    fd, avatar_path = mkstemp('.jpg')
    img = _make_avatar()

    with os.fdopen(fd, 'wb') as fileobj:
        img.save(fileobj, 'jpeg')

    return avatar_path


if __name__ == '__main__':
    print(make_avatar())
