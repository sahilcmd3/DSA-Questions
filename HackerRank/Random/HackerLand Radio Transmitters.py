# HackerRank Hackerland Radio Transmitters

"""Hackerland is a one-dimensional city with houses aligned at integral locations along a road. The Mayor wants to install 
radio transmitters on the roofs of the city's houses. Each transmitter has a fixed range meaning it can transmit a signal to 
all houses within that number of units distance away.

Given a map of Hackerland and the transmission range, determine the minimum number of transmitters so that every house is within 
range of at least one transmitter. Each transmitter must be installed on top of an existing house."""


def radio(x, k):
    x.sort()
    n=len(x)
    i=0
    transmitters=0
    
    while i<n:
        # Step 1: Find the farthest house within range k from x[i]
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1

        # Step 2: Place transmitter at the last house within range
        i -= 1
        transmitters += 1

        # Step 3: Skip all houses covered by this transmitter
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1
        
    return transmitters


if __name__ == "__main__":
    print(radio(x=[1,2,3,5,9], k=1))