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
from flight_constants import AirportDict, RouteDict, OPENFLIGHTS_NULL_VALUE

import flight_example_data


################################################################################
# Part 2 - Querying the data
################################################################################


################################################################################
# Part 3 - Implementing useful algorithms
################################################################################

def is_direct_flight(RouteDict, source: str, destination: str) -> \
        bool:
    """
    Return True if there exists a direct flight from source_IATA 
    (source airport) to destination_IATA (destination airport) in RouteDict. 
    
    ********************************************************
    handout_routes = {
    'RCM': {'JCK': ['SF3']},
    'TRO': {'GFN': ['SF3'], 'SYD': ['SF3', 'DH4']}
    }
    ********************************************************    
    >>> is_direct_flight(RouteDict, 'RCM', 'JCK')
    True
    >>> is_direct_flight(RouteDict, 'JCK', 'RCM')
    False
    >>> is_direct_flight(RouteDict, 'TRO', 'JCK')
    False
    """
    # Check if source airport exists in RouteDict
    if source not in RouteDict:
        return False
    
    # Check if there is a direct flight from source to destination
    if destination in RouteDict[source]:
        return True
    return False    


def is_valid_flight_sequence(RouteDict, flight_sequence: list[str]) -> bool:
    """    
    Return True if all the sequences of flights are valid routes( 
    a route is valid if there is a direct flight between each adjacent pair 
    of IATA codes in flight_sequence).
    
    Precondition:
        - len(flight_sequence) >= 2
        - IATA code appears in RouteDict
    
    >>> is_valid_sequence(RouteDict, ['RCM','JCK'])
    True
    >>> is_valid_sequence(RouteDict, ['RCM','JCK','TRO'])
    False
    >>> is_valid_sequence(RouteDict, ['RCM','JCK','TRO','GFN'])
    False
    """
    # Checking if the flight sequence contains atleast 2 IATA codes 
    if len(flight_sequence) < 2:
        return False
    
    # Cheking that every IATA code in filght_sequence is also in RouteDict
    for airport_code in flight_sequence:
        if airport_code not in RouteDict:
            return False    
    
    # Iterate over every pair of adjacent IATA codes 
    for i in range(len(flight_sequence) - 1):
        if not is_direct_flight(RouteDict, flight_sequence[i], 
                                flight_sequence[i + 1]):
            return False      
    return True


def summarize_by_timezone(AirportDict) -> dict[str, int]:
    """
    Return a dictionary where the key is a timezone, and the value is the 
    number of airports in the corresponding timezone based on the data 
    in AirportDict. If timezone of an airport is a Null value, ignore it.
    
    >>> summarize_by_timezone(handout_airports)
    {'Australia/Sydney': 1, 'Australia/Brisbane': 1}
    """
    timezone_counts = {}
    # Iterate over each airport in AirportDict
    for info in AirportDict.items():
        timezone = info.get('Tz')
        if timezone is not None:
            timezone_counts[timezone] = timezone_counts.get(timezone, 0) + 1
    return timezone_counts


def find_reachable_destinations(routes: RouteDict, source: str, n: int) -> \
        list[str]:
    """Return the list of IATA airport codes that are reachable from source by
    taking at most n direct flights.

    The list should not contain an IATA airport code more than once. The airport
    codes in the list should appear in lexicographical order (use the
    list.sort method on a list of strings to achieve this).

    Preconditions:
        - n >= 1
        - (source in routes) is True

    >>> example_routes = flight_example_data.create_example_routes()
    >>> find_reachable_destinations(example_routes, 'GFN', 1)
    ['TRO']
    >>> find_reachable_destinations(example_routes, 'GFN', 2)
    ['GFN', 'SYD', 'TRO']
    """        
    visited = []
    reachable_destinations = []

    queue = [(source, 0)]

    # Perform BFS
    while queue:
        airport, hops = queue.pop(0)

        # Continue if airport has already been visited or if the
        # number of hops exceeds the limit
        if airport in visited or hops > n:
            continue

        visited.append(airport)
        reachable_destinations.append(airport)

        # Enqueue neighboring airports
        if airport in routes:
            for neighbor in routes[airport]:
                queue.append((neighbor, hops + 1))

    # check that elements in final list are not repeated
    for i in range(len(reachable_destinations)):
        if reachable_destinations.count(i) > 1:
            reachable_destinations.remove(i)
        elif reachable_destinations.count(i) == 1:
            continue

    # Sorting list in lexicographical order
    reachable_destinations.sort()
    return reachable_destinations


def decomission_plane(routes: RouteDict, plane: str) -> list[tuple[str, str]]:
    """Update routes by removing plane from all source-destination routes that
    use plane. Do not remove the source-destination pair, only the plane.

    In addition, return a sorted list of two-element tuples where the first
    index is source and the second index is destination (use the list.sort
    method on a list of tuples to achieve this). The list includes *all* routes
    that that have no planes that can be used.

    >>> example_routes = flight_example_data.create_example_routes()
    >>> decomission_plane(example_routes, 'DH4')
    []
    >>> example_routes['TRO']['SYD']
    ['SF3']
    >>> example_routes = flight_example_data.create_example_routes()
    >>> decomission_plane(example_routes, 'SF3')
    [('GFN', 'TRO'), ('JCK', 'RCM'), ('RCM', 'JCK'), ('TRO', 'GFN')]
    >>> example_routes['TRO']['SYD']
    ['DH4']
    """
    routes_with_no_planes = []

    # Iterates over each source destination route
    for source, destinations in routes.items():
        for destination, airplanes in destinations.items():
            
            # If the plane is in the list of airplanes for this route, remove it
            if plane in airplanes:
                airplanes.remove(plane)
                
                # If there are no airplanes left for this route, 
                # add it to routes_with_no_planes
                if not airplanes:
                    routes_with_no_planes.append((source, destination))
    # sort the list of tuples
    routes_with_no_planes.sort()
    return routes_with_no_planes


if __name__ == '__main__':
    # On A3 we do not have a separate checker but instead include code that
    # performs the required checks.  This code requires python_ta to be
    # installed.  See the 'Completing the CSC108 Setup' section in the
    # Software Installation page on Quercus for details.

    # Uncomment the 3 lines below to have function type contracts checked
    # # Enable type contract checking for the functions in this file
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    # Check the correctness of the doctest examples
    import doctest
    doctest.testmod()

    # Uncomment the 2 lines below to check your code style with python_ta
    # import python_ta
    # python_ta.check_all(config='pyta/a3_pyta.txt')
