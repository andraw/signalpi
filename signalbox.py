#!/usr/bin/env python

#  signalbox - Holds the configuration for signalpi 
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

global nr_movement_feed
global debug_feed
global signal_area
global early_warn_signal, early_warn_headcode, early_warn_type
global up_distant, up_home, down_distant, down_home

# You will have to subscribe to a MOVEMENT feed which covers your
# area.   Unless you are in Yorkshire then you'll have to change
# it.
nr_movement_feed = "/topic/TD_LNE_NE_SIG_AREA"

# debug_feed allows you to see the data returned by the feed, options
# for this are:
#
# SHOW_FEED_CONSOLE : Writes the feed to the console
# SHOW_FEED_SERIAL  : Writes the feed to the serial port (ttyAMA0, 8N1)
debug_feed = "SHOW_FEED_CONSOLE"

# The feeds tend to be quite large geographically, so we limit the
# trains show to a specific signalling area.  
signal_area = "HU"

# early_warn is used to warn you of an approching train at a further
# away signal than on the fringe of the box - with this enabled you
# can for example warn of a train approching with an optional 
# headcode (which may be handy if you commute).
early_warn_signal = ""
early_warn_headcode = ""

# early_warn_type has the following options:
#
# HEADCODE_AT_SIG : Ring 'Train Approching' when the specified headcode
#                   passes the specified signal.
# ANY_PASS_SIG    : Ring 'Train Approching' when any train passes the
#                   specified signal
# HEADCODE        : Ring 'Train Approching' whenever the headcode passes
#                   any signal in the monitored signal location.
early_warn_type = "HEADCODE_AT_SIG"

# Signal numbers we monitor - you will need to work these out from the 
# feed to acertain the ones local to you.  Set the debug_feed variable
# to SHOW_FEED_CONSOLE to help you with that.
# distant        : Next signal from home
# home           : Signal by your box
# oos            : Signal at the end of your section
up_distant = "0701"
up_home = "0709"
up_oos = "0719"
down_distant = "0720"
down_home = "0716"
down_oos = "0704"

