#!/usr/bin/env python

#  credentials - Holds credentials for accessing Network Rail's 
#                Open Signalling data
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

global nr_username
global nr_password

# To get access to the data feeds you must create an account with 
# Network Rail.   You can register for the feeds at:
#
# https://datafeeds.networkrail.co.uk/ntrod/login
# 
# You will have to subscribe to a MOVEMENT feed which covers your
# area.
#
# When you have entered the account information below, save this
# file as credentials.py

# NR Account Information
nr_username = ""
nr_password = ""
