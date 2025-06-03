import random
import string

a =  string.ascii_lowercase + string.ascii_uppercase+string.digits+string.punctuation
n = int(input("Enter  a n value to get how man digits of password:",))
password = " "
for i in range(n):
    password+= random.choice(a)

print("your random password is:",password)
