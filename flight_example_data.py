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
from io import StringIO

from flight_constants import AirportDict, RouteDict


def create_airport_file() -> StringIO:
    """Return a "dummy file" with airport data to use for docstring examples.

    WARNING: Do NOT change this function.
    """

    s = '''"RCM","Richmond Airport","Richmond","Australia","-20.701900482177734","143.11500549316406","\\N"
    "JCK","Julia Creek Airport","Julia Creek","Australia","-20.66830062866211","141.72300720214844","Australia/Brisbane"
    "TRO","Taree Airport","Taree","Australia","-31.8885993958","152.514007568","Australia/Sydney"
    "SYD","Sydney Kingsford Smith International Airport","Sydney","Australia","-33.94609832763672","151.177001953125","Australia/Sydney"
    "GFN","Grafton Airport","Grafton","Australia","-29.7593994140625","153.02999877929688","Australia/Sydney"'''

    return StringIO(s)


def create_example_airports() -> AirportDict:
    """Return the AirportDict that should be produced when reading the data
    from create_airport_file.

    WARNING: Do NOT change this function.
    """

    return {
        'RCM': {
            'Name': 'Richmond Airport',
            'City': 'Richmond',
            'Country': 'Australia',
            'Latitude': '-20.701900482177734',
            'Longitude': '143.11500549316406',
            'Tz': '\\N'
        },
        'JCK': {
            'Name': 'Julia Creek Airport',
            'City': 'Julia Creek',
            'Country': 'Australia',
            'Latitude': '-20.66830062866211',
            'Longitude': '141.72300720214844',
            'Tz': 'Australia/Brisbane'
        },
        'TRO': {
            'Name': 'Taree Airport',
            'City': 'Taree',
            'Country': 'Australia',
            'Latitude': '-31.8885993958',
            'Longitude': '152.514007568',
            'Tz': 'Australia/Sydney'
        },
        'SYD': {
            'Name': 'Sydney Kingsford Smith International Airport',
            'City': 'Sydney',
            'Country': 'Australia',
            'Latitude': '-33.94609832763672',
            'Longitude': '151.177001953125',
            'Tz': 'Australia/Sydney'
        },
        'GFN': {
            'Name': 'Grafton Airport',
            'City': 'Grafton',
            'Country': 'Australia',
            'Latitude': '-29.7593994140625',
            'Longitude': '153.02999877929688',
            'Tz': 'Australia/Sydney'
        }
    }


def create_route_file() -> StringIO:
    """Return a "dummy file" with route data to use for docstring examples.

    WARNING: Do NOT change this function.
    """

    s = '''SOURCE: GFN
DESTINATIONS BEGIN
TRO SF3
DESTINATIONS END
SOURCE: JCK
DESTINATIONS BEGIN
ISA SF3
RCM SF3
DESTINATIONS END
SOURCE: RCM
DESTINATIONS BEGIN
JCK SF3
DESTINATIONS END
SOURCE: TRO
DESTINATIONS BEGIN
GFN SF3
SYD SF3 DH4
DESTINATIONS END'''

    return StringIO(s)


def create_example_routes() -> RouteDict:
    """Return the RouteDict that should be produced when reading the data
    from create_route_file and including only the airports from
    create_example_airports.

    WARNING: Do NOT change this function.
    """

    return {
        'GFN': {'TRO': ['SF3']},
        'JCK': {'RCM': ['SF3']},
        'RCM': {'JCK': ['SF3']},
        'TRO': {'GFN': ['SF3'], 'SYD': ['SF3', 'DH4']}
    }


def create_handout_airports() -> AirportDict:
    """Return an AirportDict with example values based on handout_airports in
    the handout.

    WARNING: Do NOT change this function.
    """

    return {
        'GFN': {
            'City': 'Grafton',
            'Country': 'Australia',
            'Latitude': '-29.7593994140625',
            'Longitude': '153.02999877929688',
            'Name': 'Grafton Airport',
            'Tz': 'Australia/Sydney'
        },
        'JCK': {
            'City': 'Julia Creek',
            'Country': 'Australia',
            'Latitude': '-20.66830062866211',
            'Longitude': '141.72300720214844',
            'Name': 'Julia Creek Airport',
            'Tz': 'Australia/Brisbane'
        }
    }


def create_handout_routes() -> RouteDict:
    """Return a RouteDict with example values based on handout_routes in the
    handout.

    WARNING: Do NOT change this function.
    """
    return {
        'RCM': {'JCK': ['SF3']},
        'TRO': {'GFN': ['SF3'], 'SYD': ['SF3', 'DH4']}
    }

