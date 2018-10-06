#!/usr/bin/env python

import sys
import csv

from zebra import zebra

z = zebra('Zebra')

z.setqueue('Zebra_Technologies_ZTC_ZT410-203dpi_ZPL')

z.setup(direct_thermal = None,
        label_height = (100,24),
        label_width = (500))

data = []
with open(sys.argv[2]) as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        data.append(row)
        
for i in range(len(data)):
    label = """^XA
^LH0,0 ^FO1,20^BY%s
^BCN,30,Y,N,N
^FD%s^FS
^XZ""" %(sys.argv[1],data[i][0])
    z.output(label)
