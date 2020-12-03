from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='TicTacToeAI',
    url='https://github.com/jladan/package_demo',
    author='Jesse Berkowitz',
    author_email='jberkow@brandeis.edu',
    # Needed to actually package something
    packages=['TicTacGame'],
    # Needed for dependencies
    install_requires=['numpy', 'turtle', 'math', 'random', 'copy', 'deepcopy' ],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A game of tictactoe versus a smart computer',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)

import turtle
import os
import math
import random 
from copy import deepcopy
import numpy as np