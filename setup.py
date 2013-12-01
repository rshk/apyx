from setuptools import setup, find_packages


version = '0.1'
install_requires = [
    'pillow',
]

setup(
    name='APyX',
    version=version,
    packages=find_packages(),
    url='http://rshk.github.io/apyx',
    license='Apache License 2.0',
    author='Samuele Santi',
    author_email='samuele@samuelesanti.com',
    description='Simple antipixel generation utility',
    long_description='Simple antipixel generation utility',
    install_requires=install_requires,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
    package_data={'': ['README.md', 'LICENSE']})
