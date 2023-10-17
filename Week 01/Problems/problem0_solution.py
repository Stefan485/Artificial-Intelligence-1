"""
Interviewbit - Yahoo, Google, Meta
Evaluate Expression

Problem Description:
    An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, /. Each string may be an integer or an operator.

Problem Constraints:
    1 <= N <= 10^5
	
Example Input:
    Input 1:
        A = ["2", "1", "+", "3", "*"]
    Input 2:
        A = ["4", "13", "5", "/", "+"]
	
Example Output:
    Output 1:
        9
    Output 2:
        6

"""

# @param A : list of strings
# @return an integer
def evalRPN(A):
	operations = {"+", "-", "*", "/"}
	stack = []
	for el in A:
		if el not in operations:
			number = int(el)
			stack.append(number)
		else:
			number2 = stack.pop()
			number1 = stack.pop()
			result = 0
			if el == "+":
				result = number1 + number2
			elif el == "-":
				result = number1 - number2
			elif el == "*":
				result = number1 * number2
			elif el == "/":
				result = number1 // number2
			stack.append(result)
	return stack.pop()
				
if __name__ == "__main__":
    print(evalRPN(["4", "13", "5", "/", "+"]))             
		            
			