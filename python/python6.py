#Write a program that searches a list of numbers for the first value divisible by both 3 and 5, prints 'Found: X' when found and immediately stops, or prints 'Not found' if none exists — using for/else. Then rewrite using a while loop, and explain what happens if you forget to increment the counter.
list=[3,5,7,8,9,10,15]
def search():
    for l in list:
        if l%3==0 and l%5==0:
            print(f'Found: {l}')
            break
    else:
        print(f'Not found')

i=0
def search_while():
    global i
    while i<len(list):
        if list[i]%3==0 and list[i]%5==0:
            print(f'Found: {i}')
            break
        i+=1
    else:
        print(f'Not Found')

search()
search_while()
