def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"
    
    arranged_problems = []
    for problem in problems:
        operands = problem.split()
        if len(operands[0]) > 4 or len(operands[2]) > 4:
            return "Error: Numbers cannot be more than four digits"
        if not operands[0].isdigit() or not operands[2].isdigit():
            return "Error: Numbers must only contain digits"
        if operands[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'"
        
        max_length = max(len(operands[0]), len(operands[2])) + 2
        arranged_problems.append(f"{operands[0]:>{max_length}}")
        arranged_problems.append(f"{operands[1]} {operands[2]:>{max_length-2}}")
        arranged_problems.append("-" * max_length)
        
        if show_answers:
            if operands[1] == '+':
                answer = str(int(operands[0]) + int(operands[2]))
            else:
                answer = str(int(operands[0]) - int(operands[2]))
            arranged_problems.append(f"{answer:>{max_length}}")
    
    return "\n".join(arranged_problems)
