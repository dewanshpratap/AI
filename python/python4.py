#Question:  Given `student = {'name': 'Alice', 'age': 21, 'courses': ['Math', 'CS']}`, write code that: (1) safely retrieves the value for key 'phone' without raising an error, returning 'N/A' if absent; (2) updates both 'age' to 22 and adds 'email': 'alice@uni.com' in a single operation; (3) iterates through all key-value pairs and prints them. Then explain why directly accessing `student['phone']` would crash while `student.get('phone')` would not, and describe what happens when you loop over the dictionary directly without calling `.items()`.

student={'name': 'Alice', 'age': 21, 'courses': ['Math', 'CS']}
print(student.get('phone','N/A'))
student.update({'age':22, 'email':'alice@uni.com'})
for i,j in student.items():
    print(i,j)

#student['phone'] will crash and student.get('phone') will not because the get method returns none if the item is not in the dictionary whereas without get you'll get error
#also iterating without .items() will only give you the value of each key-value pair


