import math

def triangle_size(side_a, side_b, angle):
    return math.sqrt(
        side_a ** 2 + side_b ** 2 - 2 * side_a * side_b * math.cos(angle)
    )
