#!/usr/bin/env python

import sys
import array
import numpy as np

class Reader:

    def __init__(self, channels=8):
        self.data = []
        self.csv = ''
        self.dest = ''
        self.channels = channels

    def open(self, filename, dest):
        f = open(filename, 'rb')
        self.data = np.fromfile(f, dtype=np.int16)
        print self.data
        self.dest = dest
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
                #print 'Record %s' % (counter/self.channels)

            if counter%(1000*self.channels) == 0:
                print 'Record %s' % (counter/self.channels)
                self.saveTo(self.dest)
                self.csv = ''

    def saveTo(self, destination):
        f = open(destination, 'aw')
        f.write(self.csv)
        f.close()

if __name__ == "__main__":
    src = sys.argv[1]
    dest = sys.argv[2]

    if len(sys.argv) == 4:
        read = Reader(sys.argv[3])
    else:
        read = Reader()
    read.open(src, dest)
    read.convert()
