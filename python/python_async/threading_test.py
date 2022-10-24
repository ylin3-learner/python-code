# coding:utf8

import threading
import multiprocessing


def sing():
    for i in range(3):
        print('唱歌中')

if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing, name='sing_thread')
    sing_thread.start()
    print(dir(multiprocessing))