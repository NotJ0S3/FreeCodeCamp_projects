# Function to calculate the square root of a number using the bisection method
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # If the input is negative, raise an error since the square root of a negative 
    # number is not defined in the set of real numbers.
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    # Handle edge cases: the square root of 1 is 1, and the square root of 0 is 0.
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Initialize the search range for the bisection method
        low = 0  # The lower bound of the search range
        high = max(1, square_target)  # The upper bound, at least 1 or the input number
        root = None  # Initialize the root variable to None
        
        # Iterate up to the maximum number of iterations to refine the estimate
        for _ in range(max_iterations):
            # Calculate the midpoint of the current range
            mid = (low + high) / 2
            square_mid = mid**2  # Square the midpoint to compare with the target

            # Check if the squared midpoint is within the allowed tolerance of the target
            if abs(square_mid - square_target) < tolerance:
                root = mid  # Found the approximate square root
                break

            # If the square of the midpoint is less than the target, move the lower bound up
            elif square_mid < square_target:
                low = mid
            else:
                # If the square of the midpoint is greater, move the upper bound down
                high = mid

        # If the loop completes without finding a root, notify the user
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:
            # Print the final result
            print(f'The square root of {square_target} is approximately {root}')
    
    # Return the calculated root or None if it did not converge
    return root

# Test the function with an example
N = 16  # The number for which we want to find the square root
square_root_bisection(N)
