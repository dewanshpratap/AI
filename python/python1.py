#Question:  Given `message = 'Hello World'`, a developer writes `message.replace('World', 'Python')` and later prints `message`, expecting 'Hello Python'. They are also trying to extract just 'World' using slicing and verify its length. Write the corrected code that: (1) properly updates the variable after replacement, (2) correctly slices 'World' from the string using index notation, and (3) uses an f-string to print a greeting in the format 'HELLO PYTHON, welcome!' — explaining why the original replace call failed to produce the expected result.

message='Hello World'
print(message[6:11])
message=message.replace('World','Python')
print(message)
print(f'{message}, welcome!. The original method failed because the replace method returns a new string.')


