#!/usr/bin/env python

import sys
import array
import numpy as np

class Reader:

    def __init__(self):
        self.data = []
        self.csv = ''

    def open(self, filename):
        f = open(filename, 'rb')
        self.data = np.fromfile(f, dtype=np.int16)
        print self.data

        f.close()

    def convert(self):
        counter = 0
        print len(self.data)
        for d in self.data:
            self.csv += str(d)
            self.csv += ';'

            counter += 1
            if (counter%8)==0:
                self.csv += '\n'
                print 'Record %s' % (counter/8)

    def saveTo(self, destination):
        f = open(destination, 'w')
        f.write(self.csv)
        f.close()

if __name__=="__main__":
    src = sys.argv[1]
    dest = sys.argv[2]

    read = Reader()
    read.open(src)
    read.convert()
    read.saveTo(dest)
