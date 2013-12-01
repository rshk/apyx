"""
Some templates for common antipixel patterns
"""


def twoparts_even(text1, fg1, bg1, text2, fg2, bg2, a1='center', a2='center'):
    return {
        'parts': [
            dict(text=text1, background=bg1, color=fg1, sizing='even',
                 align=a1),
            dict(text=text2, background=bg2, color=fg2, sizing='even',
                 align=a2),
        ],
    }


def twoparts_even_centered(text1, fg1, bg1, text2, fg2, bg2):
    return twoparts_even(text1, fg1, bg1, text2, fg2, bg2, 'right', 'left')


def twoparts_even_altcolor(text1, text2, col1, col2):
    return twoparts_even(text1, col2, col1, text2, col1, col2)


def twoparts_even_centered_altcolor(text1, text2, col1, col2):
    return twoparts_even_centered(text1, col2, col1, text2, col1, col2)


def onepart(text, fg, bg):
    return {
        'parts': [
            dict(text=text, background=bg, color=fg, sizing='even'),
        ],
    }
