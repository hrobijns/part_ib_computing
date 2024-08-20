import math as m
import numpy as np

def newton_raphson_ln(number, initial_guess=1.0, tolerance=1e-10, max_iterations=100):
    guess = initial_guess

    for i in range(max_iterations):
        next_guess = guess - (m.e**(guess) - number)/(m.e**(guess))

        # check if the guess is close enough to the actual square root
        if abs(next_guess - guess) < tolerance:
            return next_guess

        guess = next_guess

    # if max_iterations is reached, return the best guess
    return guess

# example usage:
number_to_find_ln = 2
result = newton_raphson_ln(number_to_find_ln)

print(f"The natural logarithm of {number_to_find_ln} is approximately {result}")
