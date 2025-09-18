import setuptools

setuptools.setup(
    name='tools3nm4',
    version='0.1.0',
    author='Joel',
    description='A Jupyter widgets for solving',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mwelland/ENGPHYS_3NM4',  
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=['tools3nm4'],
    install_requires=[
        'numpy',
        'matplotlib',
        'ipywidgets',
        'IPython',
        'pyppeteer',
        'nbconvert',
        'scipy',
        'plotly'
    ],
)
