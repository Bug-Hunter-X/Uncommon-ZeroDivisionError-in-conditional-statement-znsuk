def function_with_uncommon_error_solution(a, b):
    if b == 0:
        return "Division by zero error"
    elif a == 0 and b != 0:
        return 0  # Handle case where a is zero
    else:
        return a / b

result = function_with_uncommon_error_solution(0, 10)
print(result)
result2 = function_with_uncommon_error_solution(10, 0)
print(result2)
result3 = function_with_uncommon_error_solution(10, 2)
print(result3)