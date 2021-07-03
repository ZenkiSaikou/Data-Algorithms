# python3
import sys
n = int(input())

def car_fueling(dist,miles,n,gas_stations):
    dist, num_refill, curr_refill, limit = 0, 0, 0, miles
    while limit < dist:  # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
        # Find the furthest gas station we can reach
        while