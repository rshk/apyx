# APyX - Simple Python-powered Antipixel generation library

This library provides facilities for generating programmatically
Antipixels from Python.

This is especially useful if you want to quickly generate batches
of antipixels.

## Installation

`pip install .`

## Usage example

In its simplest form, you can call the ``create_antipixel()`` function, passing
a configuration dictionary like this as the only argument:

```python
{
    'base': {
        'size': (80, 15),
        'outline': '#000',
        'background': '#fff',
        'font_path': 'fonts/slkscr.ttf',
    },
    'parts': [
        dict(text='DEBIAN', background='#d70751', color='#fff',
             sizing='even', align='center'),
        dict(text='LINUX', background='#fff', color='#d70751',
             sizing='even', align='center'),
    ],
}
```

..but that's definitely tedious, so we'll automatize things a bit.

```python
here = os.path.dirname(__file__)
output_dir = os.path.join(here, 'output')
default_base = {
    'size': (80, 15),
    'outline': '#000',
    'background': '#fff',
    'font_path': os.path.join(here, 'fonts', 'slkscr.ttf'),
}
antipixels = {
    'debian': {
        'parts': [
            dict(text='DEBIAN', background='#d70751', color='#fff',
                 sizing='even', align='center'),
            dict(text='LINUX', background='#fff', color='#d70751',
                 sizing='even', align='center'),
        ],
    }
}

if __name__ == '__main__':
    from apyx import create_antipixel

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for name, config in antipixels.iteritems():
        if 'base' not in config:
            config['base'] = default_base
        print("Creating antipixel {0}".format(name))
        image = create_antipixel(config)
        image.save(os.path.join(output_dir, '{0}.png'.format(name)))
```

Even better, we can use some "templates" for common patterns!
So, that definition becomes:

```python
from apyx.templates import twoparts_even_altcolor

antipixels = {
    'debian': twoparts_even_altcolor('DEBIAN', 'LINUX', '#d70751', '#fff'),
}
```

For a complete example, have a look at ``apyx_example.py``, in the main
project folder.
