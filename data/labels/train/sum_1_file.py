import os
import re
from math import floor, log

expression = r'\d\d\d\d\d\d'

for f in sorted(os.listdir(), reverse = True):
    print(f'turning file {f}')
    n = re.search(expression, f)
    if n:
        n = int(n[0])
        n += 1
        padding = (5 - floor(log(n, 10)))*'0'
        os.rename(f, f'frame_{padding}{n}.txt')
        print(f'into frame_{padding}{n}.txt \n')
