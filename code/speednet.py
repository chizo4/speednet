'''
--------------------------------------------------------------
FILE:
    code/speednet.py

SPEEDNET:
    Module implementing the Speednet class that performs internet
    speed measurements utilizing the Speedtest API.

AUTHOR:
    Filip J. Cierkosz

VERSION:
    31/12/2023
--------------------------------------------------------------
'''

from speedtest import Speedtest
from math import *

class Speednet:
    '''
    -------------------------
    Speednet class measuring internet speed through the Speedtest API.
    -------------------------
    '''

    def __init__(self: 'Speednet') -> None:
        '''
        Initialize the Speednet class with all essential WiFi-related variables.
        '''
        self.wifi = Speedtest()
        self.download = None
        self.upload = None

    @staticmethod
    def bytes_to_mbps(bytes_size: float) -> float:
        '''
        Convert raw bytes into data transfer rate in Mbps.

            Parameters:
            -------------------------
            bytes_size (float) : Raw bytes speed.

            Returns:
            -------------------------
            float : Data transfer rate in Mbps.
        '''
        i = int(floor(log(bytes_size, 1024)))
        power = pow(1024, i)
        mbps = bytes_size / power
        return mbps
    
    def calc_speed(self: 'Speednet') -> None:
        '''
        Get and calculate the speeds in Mbps.
        '''
        self.download = self.bytes_to_mbps(self.wifi.download())
        self.upload = self.bytes_to_mbps(self.wifi.upload())

    def check_speed(self: 'Speednet') -> None:
        '''
        Perform Wi-Fi speed measurements and display them to the user.
        '''
        self.calc_speed()
        print(self.download)
        print(self.upload)
