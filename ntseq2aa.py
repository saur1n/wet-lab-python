#!/usr/bin/env python

import sys
from Bio.Seq import Seq
import warnings

warnings.filterwarnings("ignore")

s = Seq(sys.argv[1])

print("")
print(s.reverse_complement())
print("")
print(s.translate())
print("")