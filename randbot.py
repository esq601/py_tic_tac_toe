import numpy as np
import random

def choice():
    row = int(random.randint(0,2))
    col = int(random.randint(0,2))

    choice = [row,col]
    return choice
