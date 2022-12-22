# read about string module in python https://docs.python.org/3/library/string.html

import random
import string

def password_gen():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    paswd_len = int(input("Enter the password length: "))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)

    #converts the lists to a string  
    password = ''.join(s[0:paswd_len])
    print(password)


password_gen()
