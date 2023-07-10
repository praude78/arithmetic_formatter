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

