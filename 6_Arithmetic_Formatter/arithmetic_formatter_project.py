def arithmetic_arranger(problems, solve=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_row = []
    second_row = []
    dashes = []
    solutions = []

    for problem in problems:
        parts = problem.split()

        # Check if the problem has valid parts
        if len(parts) != 3:
            return "Error: Invalid problem format."
        operand1, operator, operand2 = parts

        # Validate the operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Validate the operands
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width of the current problem
        width = max(len(operand1), len(operand2)) + 2

        # Format rows
        first_row.append(operand1.rjust(width))
        second_row.append(operator + operand2.rjust(width - 1))
        dashes.append('-' * width)

        # Solve the problem if needed
        if solve:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            solutions.append(result.rjust(width))

    # Combine rows with four spaces in between
    arranged_problems = (
        '    '.join(first_row) + '\n' +
        '    '.join(second_row) + '\n' +
        '    '.join(dashes)
    )
    if solve:
        arranged_problems += '\n' + '    '.join(solutions)

    return arranged_problems

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
