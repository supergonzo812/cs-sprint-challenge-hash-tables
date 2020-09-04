#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Create a hashtable for the flights with key(source) : value(destination)
    ticket_cache = {}
    # Create storage for the flight path return value
    route = [None] * length

    # Loop through all the tickets
    for ticket in tickets:
        # Add the ticket to the cache
        ticket_cache[ticket.source] = ticket.destination
    # Grab the ticket with the 
    next = ticket_cache["NONE"]

    # Loop through the length for indices
    for cur_ticket_index in range(0, length):
        # Grab the current index
        route[cur_ticket_index] = next
        # reassign next
        next = ticket_cache[next]
    # Return the flight path
    return route
