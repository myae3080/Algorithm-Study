# math

import math

# input
climb, slip, height = map(int, input().split())

print((math.ceil((height - climb) / (climb - slip))) + 1)
