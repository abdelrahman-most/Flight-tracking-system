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
from typing import TextIO
from flight_constants import AirportDict, RouteDict

import flight_example_data


################################################################################
# Constants: the column number for each feature in the airport data csv file
################################################################################
INDEX_AIRPORTS_IATA = 0
INDEX_AIRPORTS_NAME = 1
INDEX_AIRPORTS_CITY = 2
INDEX_AIRPORTS_COUNTRY = 3
INDEX_AIRPORTS_LATITUDE = 4
INDEX_AIRPORTS_LONGITUDE = 5
INDEX_AIRPORTS_TZ = 6

# An AirportDict is a dictionary that maps IATA airport codes to dictionaries
# that contains more information about the airport (e.g., name, country, etc.)

# A RouteDict is a dictionary that maps IATA airport codes to dictionaries of
# reachable destinations. Each reachable destination in the dictionary is an
# IATA airport code that maps to a list of airplanes that are used for that
# flight.

################################################################################
# Part 1 - Reading the data
################################################################################


def read_airports(airports_data: TextIO) -> AirportDict:
    """Return an airports dictionary based on the data in the open file
    referred to by airports_data.  The airports dictionary maps each IATA
    airport code to its inner dictionary containing information about that
    airport.

    The dictionary containing information about each airport maps string keys
    that identify the information to the respective data found in airports_data.
    The keys in this inner dictionary are:
        'Name', 'City', 'Country', 'Latitude', 'Longitude', and 'Tz'.

    Preconditions:
        - Every IATA airport code in the airports_data is unique
        - The data in airports_data is formatted correctly

    >>> example_airport_file = flight_example_data.create_airport_file()
    >>> actual = read_airports(example_airport_file)
    >>> actual == flight_example_data.create_example_airports()
    True
    """
    airports = {}

    for line in airports_data:
        # Split the line into fields
        fields = line.replace('"', '').strip().split(',')

        iata_code = fields[INDEX_AIRPORTS_IATA]
        airport_name = fields[INDEX_AIRPORTS_NAME]
        city = fields[INDEX_AIRPORTS_CITY]
        country = fields[INDEX_AIRPORTS_COUNTRY]
        latitude = float(fields[INDEX_AIRPORTS_LATITUDE]) 
        # couldn't convrt latitude to float
        longitude = float(fields[INDEX_AIRPORTS_LONGITUDE])
        timezone = fields[INDEX_AIRPORTS_TZ]

        # airport_details is a dictionary containing all the information found
        # in airport_data related to an IATA  
        airport_details = {
            'Name': airport_name,
            'City': city,
            'Country': country,
            'Latitude': latitude,
            'Longitude': longitude,
            'Tz': timezone}
        
        airports[iata_code] = airport_details
    return airports


def read_routes(routes_data: TextIO, airports: AirportDict) -> RouteDict:
    """Return a routes dictionary based on the data in the open file
    referred to by routes_data and given airports dictionary.

    Do not include routes with a source or destination airport codes that are
    not in airports.

    Preconditions:
        - The data in routes_data is formatted correctly

    >>> example_routes_file = flight_example_data.create_route_file()
    >>> example_airports = flight_example_data.create_example_airports()
    >>> actual = read_routes(example_routes_file, example_airports)
    >>> actual == flight_example_data.create_example_routes()
    True
    """
    routes = {}
    source_airport = None
    
    for line in routes_data:
        line = line.strip()

        # If line starts with 'SOURCE:', we have reached a new source airport
        if line.startswith('SOURCE:'):
            source_airport = line.split()[1]
            if source_airport in airports:
                if source_airport not in routes:
                    routes[source_airport] = {}
            else:
                source_airport = None
        
        elif line == 'DESTINATIONS BEGIN':
            continue
        elif line == 'DESTINATIONS END':
            continue
        
        # Otherwise, its a source airport (a line containing 
        # IATA code and plane type)
        elif source_airport:
            destination = line.split()
            airplanes = line.split()
            if destination in airports:
                if destination not in routes[source_airport]:
                    routes[source_airport][destination] = []
                routes[source_airport][destination].append(airplanes)

    return routes    


if __name__ == '__main__':
    # On A3 we do not have a separate checker but instead include code that
    # performs the required checks.  This code requires python_ta to be
    # installed.  See the 'Completing the CSC108 Setup' section in the
    # Software Installation page on Quercus for details.

    # Uncomment the 3 lines below to have function type contracts checked
    # Enable type contract checking for the functions in this file
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()
    
    # Check the correctness of the doctest examples
    import doctest
    doctest.testmod()
    
    # Uncomment the 2 lines below to check your code style with python_ta
    # import python_ta
    # python_ta.check_all(config='pyta/a3_pyta.txt')

    # Uncomment the lines below to open the larger data files and call your
    # functions above
    # airport_file = open('data/airports.csv', encoding='utf8')
    # airports = read_airports(airport_file)
    # airport_file.close()
    # routes_file = open('data/routes.dat', encoding='utf8')
    # routes = read_routes(routes_file, airports)
    # routes_file.close()
