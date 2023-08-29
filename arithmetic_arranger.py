def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {
        "top": [],
        "bottom": [],
        "line": [],
        "answer": []
    }

    for problem in problems:
        parts = problem.split()
        operand1, operator, operand2 = parts[0], parts[1], parts[2]

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2

        arranged_problems["top"].append(operand1.rjust(width))
        arranged_problems["bottom"].append(operator + operand2.rjust(width - 1))
        arranged_problems["line"].append('-' * width)

        if operator == '+':
            answer = str(int(operand1) + int(operand2))
        else:
            answer = str(int(operand1) - int(operand2))
        arranged_problems["answer"].append(answer.rjust(width))
    
    arranged_format = []
    for key in arranged_problems.keys():
        arranged_format.append("    ".join(arranged_problems[key]))

    if show_answers:
        return '\n'.join(arranged_format)
    else:
        return '\n'.join(arranged_format[:-1])  # Exclude answer line

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

