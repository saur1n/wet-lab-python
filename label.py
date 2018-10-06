#!/usr/bin/env python

import sys
import csv

from zebra import zebra

z = zebra('Zebra')

z.setqueue('Zebra_Technologies_ZTC_ZT410-203dpi_ZPL')

z.setup(direct_thermal = None,
        label_height = (100,24),
        label_width = (500))
       
label = """^XA
^LH0,0 ^FO1,20^BY%s
^BCN,30,Y,N,N
^FD%s^FS
^XZ""" %(sys.argv[1],sys.argv[2])

z.output(label)
