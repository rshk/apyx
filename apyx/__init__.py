"""
Antipixels generator script
"""

from __future__ import print_function

import copy

from PIL import Image, ImageFont, ImageDraw


def create_antipixel(cfg):
    font = ImageFont.truetype(cfg['base']['font_path'], size=8)
    width, height = cfg['base']['size']
    avail_space = width - 4  # padding: 2px on each side
    image = Image.new('RGB', cfg['base']['size'])
    draw = ImageDraw.Draw(image)
    parts = copy.deepcopy(cfg['parts'])  # so we can safely alter

    ##--------------------------------------------------
    ## Prepare sizing

    even_parts = []
    for part in parts:
        part['text_width'] = draw.textsize(part['text'], font=font)[0]
        part_sizing = part.get('sizing', 'even')
        if part_sizing == 'even':
            ## Keep track as we'll need later..
            even_parts.append(part)
        elif part_sizing == 'fixed':
            avail_space -= part['width']
        else:
            raise ValueError("Invalid sizing: " + part_sizing)
    avail_space -= len(parts)  # spacing
    all_text_space = sum(x['text_width'] for x in even_parts)
    if all_text_space > avail_space:
        raise ValueError("Not enough space to fit text!")
    for part in even_parts:
        # Give space proportional
        part['sizing'] = 'fixed'
        part['width'] = int(round(1.0 * part['text_width'] *
                                  avail_space / all_text_space))

    ##--------------------------------------------------
    ## Draw background

    draw.rectangle(
        [(0, 0), (image.size[0] - 1, image.size[1] - 1)],
        outline=cfg['base']['outline'],
        fill=cfg['base']['background'])

    ##--------------------------------------------------
    ## Draw rectangles, with text

    # Vertical bounds
    vmin, vmax = 2, image.size[1] - 3
    # Horizontal offset
    offset = 2
    for part in parts:
        draw.rectangle(
            [(offset, vmin), (offset + part['width'], vmax)],
            fill=part['background'])

        text_align = part.get('align', 'center')
        if text_align == 'left':
            text_offset = 1
        elif text_align == 'right':
            text_offset = part['width'] - part['text_width']
        elif text_align == 'center':
            text_offset = round((part['width'] - part['text_width']) / 2.0)
        else:
            raise ValueError("Invalid alignment: " + text_align)

        draw.text((offset + text_offset, vmin + 1),
                  part['text'], fill=part['color'], font=font)

        offset += part['width']
        offset += 1  # space between rectangles

    ##--------------------------------------------------
    ## Draw outline to make sure we clear overflows..

    draw.rectangle(
        [(0, 0), (image.size[0] - 1, image.size[1] - 1)],
        outline=cfg['base']['outline'])
    draw.rectangle(
        [(1, 1), (image.size[0] - 2, image.size[1] - 2)],
        outline=cfg['base']['background'])

    return image
