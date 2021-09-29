"""
Example usage of APyX, to generate a bunch of antipixels
"""

import os
from apyx.templates import twoparts_even, twoparts_even_altcolor, \
    twoparts_even_centered, twoparts_even_centered_altcolor, onepart

here = os.path.dirname(__file__)
output_dir = os.path.join(here, 'output')
default_base = {
    'size': (80, 15),
    'outline': '#000',
    'background': '#fff',
    'font_path': os.path.join(here, 'fonts', 'slkscr.ttf'),
}
antipixels = {
    'debian': twoparts_even_altcolor('DEBIAN', 'LINUX', '#d70751', '#fff'),
    'gentoo': twoparts_even_altcolor('GENTOO', 'LINUX', '#A59DF6', '#fff'),
    'python_27': twoparts_even('PYTHON', '#000', '#FFD536',
                               '2.7', '#fff', '#366F9F'),
    'python_3k': twoparts_even('PYTHON', '#000', '#FFD536',
                               '3k', '#fff', '#366F9F'),
    'javascript': twoparts_even_centered('JAVA', '#000', '#ffbd00',
                                         'SCRIPT', '#000', '#fff'),
    'coffeescript': twoparts_even_centered_altcolor(
        'COFFEE', 'SCRIPT', '#000', '#fff'),
    'html_5': twoparts_even('HTML', '#fff', '#E44D26',
                            '5', '#fff', '#F16529'),
    'css_3': twoparts_even('CSS', '#fff', '#1572B6',
                           '3', '#fff', '#33A9DC'),
    'scss': twoparts_even_altcolor('SCSS', 'SASS', '#CE4DD6', '#fff'),
    'django_14': twoparts_even_altcolor('DJANGO', '1.4', '#092E20', '#fff'),
    'flask': onepart('FLASK', '#fff', '#000'),
    'rabbit_mq': twoparts_even('RABBIT', '#fff', '#ff6600',
                               'MQ', '#fff', '#A9B5AF'),
    'elasticsearch': twoparts_even_centered_altcolor(
        'ELASTIC', 'SEARCH', '#82B64A', '#fff'),
    'zeromq': onepart('ZEROMQ', '#fff', '#f00'),
    'git': twoparts_even('GIT', '#fff', '#F03C2E', 'SCM', '#000', '#fff'),
    'mongodb': twoparts_even('MONGO', '#fff', '#402916',
                             'DB', '#402916', '#F8DBA2'),
    'postgresql': twoparts_even_centered_altcolor(
        'POSTGRE', 'SQL', '#336791', '#fff'),
    'openldap': twoparts_even_centered(
        'OPEN', '#fff', '#000', 'LDAP', '#fff', '#915570'),
}

if __name__ == '__main__':
    from apyx import create_antipixel

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for name, config in antipixels.items():
        if 'base' not in config:
            config['base'] = default_base
        print("Creating antipixel {0}".format(name))
        image = create_antipixel(config)
        image.save(os.path.join(output_dir, '{0}.png'.format(name)))
