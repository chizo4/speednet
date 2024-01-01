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
    01/01/2024
--------------------------------------------------------------
'''

from math import pow, log, floor
import threading
from time import sleep
from speedtest import Speedtest

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
        try:
            self.wifi = Speedtest()
            self.download = None
            self.upload = None
            self.calc_complete = threading.Event()
        except Exception as e:
            print(f'ERROR: Failed to measure the connection speed due to:\n{e}\n\n')

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

    @staticmethod
    def loading_effect(event: threading.Thread) -> None:
        '''
        Display a loading effect in the terminal (e.g. until completing a calculation).

            Parameters:
            -------------------------
            event (threading.Event): An event to signal when the loading should stop.
        '''
        load_msg = '  CHECKING CONNECTION SPEED 🛜'
        print(load_msg, end='', flush=True)
        i = 0
        load_chars = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
        # Loading effect until the parallel computation is done.
        while not event.is_set():
            print(f'\r{load_chars[i % len(load_chars)]}', end='', flush=True)
            i += 1
            sleep(0.1)
        # Clear the line when loading is done.
        print('\r' + ' ' * (len(load_msg) + len(load_chars[-1])), end='\r', flush=True)

    def calc_speed(self: 'Speednet') -> None:
        '''
        Calculate the connection speed in Mbps.
        '''
        self.download = self.bytes_to_mbps(self.wifi.download())
        self.upload = self.bytes_to_mbps(self.wifi.upload())

    def print_speed(self: 'Speednet') -> None:
        '''
        Print the connection speed measurements.
        '''
        print(''.join('-' for _ in range(30)))
        print('|     🛜 CONNECTION SPEED    |')
        down = round(self.download, 1)
        print(f'|   • Download: {str(down):<5} Mbps   |')
        up = round(self.upload, 1)
        print(f'|   • Upload:   {str(up):<5} Mbps   |')
        print(''.join('-' for _ in range(30)))

    def check_speed(self: 'Speednet') -> None:
        '''
        Perform Wi-Fi speed measurements and display them in the terminal.
        '''
        # Start a separate thread for the loading effect.
        loading_thread = threading.Thread(
            target=self.loading_effect, args=(self.calc_complete,)
        )
        loading_thread.start()
        # Start and get the result from the heavy calculation.
        self.calc_speed()
        # Signal that the calculation is complete.
        self.calc_complete.set()
        # Wait for the loading effect to finish.
        loading_thread.join()
        # Finally, provide the results in the terminal.
        self.print_speed()
