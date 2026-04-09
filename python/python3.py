#Question:  You have `list_a = ['Math', 'Science']` and `list_b = list_a`. A developer appends 'Art' to `list_b` and is shocked to find `list_a` also contains 'Art'. Separately, they try `courses_set = {}` and later call `.add('History')` on it, which crashes. They also want to find courses appearing in both `list_a` and a third list `list_c`. Fix all three issues by: (1) explaining the memory aliasing bug and providing a proper copy, (2) fixing the set initialization, and (3) writing the correct operation to find the intersection — and explaining which data structure is most efficient for that lookup and why.

list_a  = ['Math', 'Science']
list_b = list_a
list_b.append('Art')
courses_set=set()   #{} creates a dictionary and set{} creates a set
list_c={'History','CompSci'}
list_a=set(list_a)
print(f'{list_a.union(list_c)} there are the total courses in list a and list c. Set is a good way of storing unordered mutable data structure.')

