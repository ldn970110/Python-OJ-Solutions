def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/' or op == '%':
        return 2
    return 0  

def apply_op(operators, values):

    op = operators.pop()
    right = values.pop()
    left = values.pop()
    if op == '+':
        values.append(left + right)
    elif op == '-':
        values.append(left - right)
    elif op == '*':
        values.append(left * right)
    elif op == '/':
        # 題目保證是整數運算，所以使用整數除法 //
        values.append(left // right)
    elif op == '%':
        values.append(left % right)

def is_number(token):
    """
    用 try-except 的方法，判斷一個字串是不是數字。
    """
    try:
        int(token)

        return True
    except ValueError:
        return False




try:
    while True:
        tokens = input().split()

        values = []
        operators = []

        for token in tokens:
            if is_number(token):
                values.append(int(token))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_op(operators, values)
                if operators: operators.pop()
            else: 
                while (operators and operators[-1] != '(' and
                       precedence(operators[-1]) >= precedence(token)):
                    apply_op(operators, values)
                operators.append(token)

        while operators:
            apply_op(operators, values)

        if values:
            print(values[0])


except :
    pass