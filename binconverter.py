#!/usr/bin/env python

import sys
import array
import numpy as np

class Reader:

    def __init__(self):
        self.data = ''
        

    def open(self, filename):
        f = open(filename, 'rb')
        self.data = np.fromfile(f, dtype=np.int16)

    def convert(self):
        print 'c'


if __name__=="__main__":
    name = sys.argv[1]
    read = Reader()
    read.open(name)