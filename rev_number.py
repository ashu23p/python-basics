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
"""  
Explanation -

Let's understand this program step by step.

We initialed a number variable for user input and variable revs_number initial value to null.

First Iteration

Reminder = number %10
Reminder = 12345%10 = 5
Reverse = Reverse *10 + Reminder Initial value of revs_number is null
Reverse = 0 * 10 + 5 = 0 + 5 = 5
Number = Number //10
Number = 1234 //10 = 1234 // Now loop will iterate on this number.
Second Iteration

Now the number is 123, and the revs_number is 5. The while checks its condition and executes for the next iteration.

Reminder = Number % 10
Reminder = 1234 % 10 = 4
Reverse = Reverse *10+ Reminder = 5 * 10 + 4
Reverse = 50 + 4 = 54
Number = Number //10 = 12345 //10
Number = 123
Third Iteration

From the Second Iteration, the values of both Number and Reverse have been changed as: number = 123 and revs_number = 54

Reminder = Number %10
Reminder = 123%10 = 3
Reverse = Reverse *10+ Reminder = 54 * 10 + 3
Reverse = 540 + 3 = 543
Number = Number //10 = 123//10
Number = 12
Fourth Iteration

The modified number is 12 and the revs_number is 543: Now while executes again.

Reminder = Number %10
Reminder = 12 %10 = 2
Reverse = Reverse *10+ Reminder = 543 * 10 + 2
Reverse = 5430 + 2 = 5432
Number = Number //10 = 12//10
Number = 1
Fifth Iteration

Reminder = Number %10
Reminder = 1 %1 0 = 1
Reverse = Reverse *10+ Reminder = 5432 * 10 + 1
Reverse = 54320 + 1 = 54321
while loop is terminated because if found the false as a Boolean result.

You can enter the different number and check the result.Sss
"""
