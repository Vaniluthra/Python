'''
The Binary number system only uses two digits, 0 and 1 and number system can 
be called binary string. You are required to implement the following function:
int OperationsBinaryString(char* str);
The function accepts a string str as its argument. The string str consists of binary digits 
separated with an alphabet as follows:
• – A denotes AND operation
• – B denotes OR operation
• – C denotes XOR Operation
You are required to calculate the result of the string str, scanning the string to right 
taking one operation at a time, and return the same.
Note:
• No order of priorities of operations is required
• Length of str is odd
• If str is NULL or None (in case of Python), return -1
Input:
str: 1C0C1C1A0B1
Output:
1
Explanation:
The alphabets in str when expanded becomes “1 XOR 0 XOR 1 XOR 1 AND 0 OR 1”, result of 
the expression becomes 1, hence 1 is returned.
'''

def A(x, y):
    return int(x) and int(y)

def B(x, y):
    return int(x) or int(y)

def C(x, y):
    return int(x) ^ int(y)

def evaluate_expression(expression):
    result = expression[0]
    for i in range(1, len(expression), 2):
        operation = expression[i]
        operand = expression[i + 1]
        if operation == 'A':
            result = A(result, operand)
        elif operation == 'B':
            result = B(result, operand)
        elif operation == 'C':
            result = C(result, operand)
    return result

# Example usage
expression = "1C0C1C1A0A1"
print("Result:", evaluate_expression(expression))
