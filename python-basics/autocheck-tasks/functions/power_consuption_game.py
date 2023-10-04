def game(terra, power):
    accumulated_power = power
    for level in terra:
        for step in level:
            if accumulated_power >= step:
                accumulated_power += step
            else:
                break
    return accumulated_power

print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1))