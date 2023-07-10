def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    top_line = []
    bottom_line = []
    separator_line = []
    answer_line = []
    
    for problem in problems:
      parts = problem.split()

      operand1 = parts[0]
      operator = parts[1]
      operand2 = parts[2]

	if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
      
    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

    if len(operand1) > 4 or len(operand2) > 4:
       return "Error: Numbers cannot be more than four digits."

    width = max(len(operand1), len(operand2)) + 2
    top_line.append(operand1.rjust(width))
    bottom_line.append(operator + operand2.rjust(width - 1))
    separator_line.append('-' * width)

    if show_answers:
     if operator == '+':
      answer = str(int(operand1) + int(operand2))
     else:
      answer = str(int(operand1) - int(operand2))
     answer_line.append(answer.rjust(width))
     
    arranged_problems.append('    '.join(top_line))
    arranged_problems.append('    '.join(bottom_line))
    arranged_problems.append('    '.join(separator_line))
    
    if show_answers:
     arranged_problems.append('    '.join(answer_line))

    return '\n'.join(arranged_problems)


