#LEETCODE (medium)

"""There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
(i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique."""


#GREEDY APPROACH
#Time Complexity: O(n)

def can_complete(gas, cost):

    if sum(gas) < sum(cost):  #check if the solution is possible
        return -1

    current_gas = 0  #Track current gas
    start = 0  #index from which we assume we could potentially complete the circuit

    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]  #updating current gas for each station

        if current_gas < 0:
            current_gas = 0
            start = i + 1
            """If current_gas becomes negative, it means starting from the current start index won’t allow us 
               to complete the circuit.
               When current_gas < 0, we reset current_gas to 0 because we need to start from a new point.
               We then update start to i + 1, as the next station is the new candidate for a starting point.
               This is because any start point before this would also fail,we can safely ignore all stations up to i"""

    return start


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
ans = can_complete(gas, cost)
print(ans)