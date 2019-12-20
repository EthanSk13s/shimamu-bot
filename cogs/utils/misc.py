import os
import shutil

import pywal as wal

from PIL import Image
from io import BytesIO

def get_color(image: bytes):
    with open('./tmp/img.png', 'wb') as f:
        for chunk in BytesIO(image):
            f.write(chunk)

    color_map = wal.colors.get('./tmp/img.png', cache_dir='./tmp')

    os.remove('./tmp/img.png')
    shutil.rmtree('./tmp/schemes')
    return color_map['colors']

def generate(image: bytes):
    colors = get_color(image)
    color_list = []
    for color in colors.values():
        rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        color_list.append(rgb)

    im = Image.new('RGB', [16, 1])
    im.putdata(color_list)

    final_buffer = BytesIO()
    im2 = im.resize((400, 400))

    im2.save(final_buffer, 'png')

    final_buffer.seek(0)

    return final_buffer
    