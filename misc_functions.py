from datetime import datetime
import os
import random
import time

def as_string(board_state):
    return ''.join([str(x) for x in board_state])


def init_board_state(board_size):
    rows = board_size[0]
    cols = board_size[1]
    return [0]*((2*rows*cols) + rows + cols)

def timeNow():
    now = datetime.now()
    currentTime = now.strftime("%HH %MM %SS")
    return currentTime


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 50, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    prefix="Loading: "+str(iteration/total*100)+"%"
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd, flush=True)
    if iteration == total:
        print()

# random.randint(1,end)
def printWait(ende):
    for i in range(1, ende):
        print(".", end="", flush=True)
        time.sleep(1)