import mss
import time
from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

BOX_COORD = {'left': 270, 'top': 280, 'width': 50, 'height': 35}

layout_step = 100
layout_width = 2


def gen_filename():
    return 'snap_{}.png'.format(int(time.time()))


def snapshot():
    sct = mss.mss()
    m = sct.monitors[0]
    print(m)

    sct_img = sct.grab(m) #screen
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    draw = ImageDraw.Draw(im=img, mode=img.mode)
    fill = ImageColor.getrgb('red')

    width, height = img.size
    print(f'Screen resolution: X: {width}, Y: {height}')

    for i in range(0, width, layout_step):
        draw.line(xy=((i, 0), (i, height)), fill=fill, width=layout_width)

    for i in range(0, width, layout_step):
        draw.line(xy=((0, i), (width, i)), fill=fill, width=layout_width)

    outline = ImageColor.getrgb('green')

    box_xy = (
        (BOX_COORD['left'], BOX_COORD['top']),
        (BOX_COORD['left'] + BOX_COORD['width'], BOX_COORD['top'] + BOX_COORD['height'])
    )
    draw.rectangle(xy=box_xy, outline=outline, width=6)
    img.save(gen_filename())
    print('Done!')


snapshot()