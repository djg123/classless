from setuptools import setup

setup(
    name = "Classless",
    version = "0.0.1",
    author = "David J Gordon",
    author_email = "djyale@gmail.com",
    description = ('Easily curry multiple functions to a given list of'
                   ' arguments without using classes'),
    license = "BSD",
    keywords = "class meta",
    url = "https://github.com/djyale/classless",
    py_modules=['classless'],
    long_description=open('README.rst').read() + '\n\n',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        "Topic :: Utilities",
        'Operating System :: OS Independent',
        'Natural Language :: English',
        "License :: OSI Approved :: BSD License",
    ],
)
