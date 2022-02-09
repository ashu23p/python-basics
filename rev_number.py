n = int(input())  # n to be reversed
reversed_number = 0  # initialising to zeo

# reversing n to reversed_number using while loop
while(n > 0):
    rem = n % 10
    reversed_number = (reversed_number*10)+rem
    n = n//10

print("{} is reversed number".format(reversed_number))
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}
