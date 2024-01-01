'''
--------------------------------------------------------------
FILE:
    code/main.py

SPEEDNET:
    Main module to run internet speed measurements.

AUTHOR:
    Filip J. Cierkosz

VERSION:
    01/01/2024
--------------------------------------------------------------
'''

from speednet import Speednet

if __name__ == '__main__':
    speednet = Speednet()
    speednet.check_speed()
