'''
--------------------------------------------------------------
FILE:
    code/main.py

SPEEDNET:
    Main module to run Speednet connection testing.

USE:
    python main.py (options)

EXAMPLE (full testing):
    python main.py

OPTIONS:
    -h             : Print this help message.
    -t OPTION : For download only: 'd', 'down', 'download' (ignore case).
                For upload only: 'u', 'up', 'upload' (ignore case).
                Default: no -t required; it implies full testing.

AUTHOR:
    Filip J. Cierkosz

VERSION:
    01/01/2024
--------------------------------------------------------------
'''

import getopt
from speednet import Speednet
import sys

class CommandLine:
    '''
    -------------------------
    CommandLine class handling various options for Speednet measurements.
    -------------------------
    '''

    def __init__(self: 'CommandLine') -> None:
        '''
        Specify the options provided through the command line.
        '''
        self.exit = False
        self.test_opts = []
        # Allowed test options.
        self.DOWN_OPT = {'d', 'down', 'download'}   # Download only.
        self.UP_OPT = {'u', 'up', 'upload'}         # Upload only.
        try:
            opts, _ = getopt.getopt(sys.argv[1:], 'ht:')
            self.opts = dict(opts)
            self.handle_opts()
        except getopt.GetoptError:
            self.exit = True
            print(f'\nERROR: Wrong command line options. Please try again!\n')
            self.help()

    @staticmethod
    def help() -> None:
        '''
        Provide help documentation on how to correctly run the program with options.
        '''
        progname = sys.argv[0].split('/')[-1]
        help = __doc__.replace('<PROGNAME>', progname, 1)
        print(help, file=sys.stderr)

    def handle_opts(self: 'CommandLine') -> None:
        '''
        Process the provided command line options.
        '''
        if '-h' in self.opts:
            self.help()
            # If no other option than help, then assume the program should be stopped.
            if len(self.opts) == 1:
                self.exit = True
        # If no option or empty, then treat as full testing.
        if ('-t' not in self.opts) or self.opts['-t'] == '':
            self.test_opts = ['d', 'u']
        # Check for the download/upload option.
        elif self.opts['-t'].lower() in self.DOWN_OPT:
            self.test_opts.append('d')
        elif self.opts['-t'].lower() in self.UP_OPT:
            self.test_opts.append('u')
        else:
            raise getopt.GetoptError(msg='')

if __name__ == '__main__':
    config = CommandLine()
    # Exit the program if provided with invalid options.
    if config.exit:
        sys.exit(0)
    else:
        speednet = Speednet(test_opts=config.test_opts)
        speednet.check_speed()
