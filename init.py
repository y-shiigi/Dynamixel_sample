#!/usr/bin/env python

from struct import*

import time
import array
import math
import curses
from seed_command import SeedCommand

#----------- main -----------------#
if __name__ == "__main__":

	seed=SeedCommand(0,57143)

	ID = seed.SEED_DX_PING()

	if (ID == None):
		print "False"
	else :
		seed.SEED_DX_MODE(ID,4095,4095)
		print "Success!"
