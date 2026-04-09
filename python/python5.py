#Question:  A developer writes `if user = 'admin':` and also writes `if login_list == []:` to check for an empty list, but neither block behaves correctly. Separately, they want a condition that grants access only when a user is 'admin' AND is logged in, OR when the user is a 'superuser' regardless of login status. Fix all three issues, explain the distinction between `=` and `==`, describe why `if login_list == []:` is non-Pythonic compared to `if not login_list:`, and explain the difference between `==` and `is` using a concrete list example.


user=input('Enter user: ')
logged_in=()
if (user == 'admin' and not logged_in) or user == 'superuser':
    print('Access granted')


# '=' is an assignment operator whereas '==' is for checking the value
# every empty list compares to True