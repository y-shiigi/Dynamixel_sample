#!/usr/bin/env python

from struct import*

import time
import array
import math
import curses
from seed_command import SeedCommand

ID = 1

#----------- main -----------------#
if __name__ == "__main__":

	seed=SeedCommand(0,57143)

	seed.SEED_DX_SRV(ID,1)

	time.sleep(0.5)

	seed.SEED_DX_MOV(ID,1000,4095*1)
