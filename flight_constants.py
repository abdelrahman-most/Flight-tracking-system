"""CSC108H1S: Functions for Assignment 3 - Airports and Routes.

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 The CSC108 Team
"""

################################################################################
# Constants
################################################################################
OPENFLIGHTS_NULL_VALUE = '\\N'


################################################################################
# An AirportDict is a dictionary that maps IATA airport codes to dictionaries
# that contains more information about the airport (e.g., name, country, etc.)
################################################################################
AirportDict = dict[str, dict[str, str]]

################################################################################
# A RouteDict is a dictionary that maps IATA airport codes to dictionaries of
# reachable destinations. Each reachable destination in the dictionary is an
# IATA airport code that maps to a list of airplanes that are used for that
# flight.
################################################################################
RouteDict = dict[str, dict[str, list[str]]]
