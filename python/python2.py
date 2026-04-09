#Question:  A developer receives user input via `num1 = input('Enter number: ')` and `num2 = input('Enter number: ')`, then attempts `result = num1 + num2`, expecting arithmetic addition. They also want to check if the result is odd using modulo, and round it to 2 decimal places. The code produces wrong output silently without crashing. Identify the type-related bug, write corrected code that performs true addition, verifies odd/even status, and rounds correctly — explaining the exact reason why the original expression behaved differently than expected.

num1 = float(input('Enter number: '))
num2 = float(input('Enter number: '))
x= num1 + num2
if x%2==0:
    print(f'{x} is even')
else:
    print(f'{x} is odd')
print(round(x,2))