#!/usr/bin/env python

#  block_bell - Code for interpreting the bell code and ringing the 
#               phyical bell
#
#  Copyright (C) 2016 - Andrew Rawlins
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.

import time
import signalbox

def ring ( bell_code ):
	print "Bell code : ", bell_code

	if signalbox.debug_feed == "SHOW_FEED_CONSOLE":
		print "BELL : rang bell code %s " % (bell_code)
	if signalbox.debug_feed == "SHOW_FEED_SERIAL":
		print "BELL : rang bell code %s " % (bell_code)

	
	if len(bell_code) == 1:
		ring_bell(bell_code)

	if len(bell_code) == 3:
		ring_bell(bell_code[0])
		time.sleep(1)
		ring_bell(bell_code[2])
	
	if len(bell_code) == 5:
		ring_bell(bell_code[0])
		time.sleep(1)
		ring_bell(bell_code[2])
		time.sleep(1)
		ring_bell(bell_code[4])

	return

def ring_bell ( rings ):

	num_rings = int(rings)
	for ting in range(0, num_rings):
		print "."
		time.sleep(1)

	return
	
