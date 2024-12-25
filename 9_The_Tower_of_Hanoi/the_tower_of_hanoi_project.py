# Number of disks to move in the Tower of Hanoi problem
NUMBER_OF_DISKS = 5

# Initialize the rods:
# Rod A starts with all the disks (from largest to smallest).
A = list(range(NUMBER_OF_DISKS, 0, -1))  # [5, 4, 3, 2, 1]
B = []  # Auxiliary rod, initially empty.
C = []  # Target rod, initially empty.

def move(n, source, auxiliary, target):
    """
    Recursively solves the Tower of Hanoi problem.

    Args:
    - n: Number of disks to move.
    - source: The rod from which disks are moved.
    - auxiliary: The rod used as an intermediate helper.
    - target: The rod to which disks are moved.
    """
    if n <= 0:
        # Base case: No disks to move; stop the recursion.
        return

    # Step 1: Move n - 1 disks from the source rod to the auxiliary rod,
    # so they are temporarily out of the way.
    move(n - 1, source, target, auxiliary)

    # Step 2: Move the nth (largest remaining) disk from the source rod to the target rod.
    target.append(source.pop())  # Remove from source and add to target.

    # Display the current state of all three rods.
    print(A, B, C, '\n')

    # Step 3: Move the n - 1 disks that were temporarily placed on the auxiliary rod
    # to the target rod.
    move(n - 1, auxiliary, source, target)

# Start the process by moving all disks from rod A to rod C, using rod B as auxiliary.
move(NUMBER_OF_DISKS, A, B, C)
