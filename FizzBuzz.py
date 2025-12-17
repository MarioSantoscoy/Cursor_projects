#FizzBuzz

#Rules:
#Go from number 1 to 50 inclusive.
#If "n" number is multiple of 3, print "Fizz".
#If "n" number is multiple of 5, print "Buzz"
#If "n" number is multiple of both (3 and 5), print "FizzBuzz".
#If "n" number has no multiple of 3 or 5, print the number.

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num}: FizzBuzz')
    elif num % 3 == 0:
        print(f'{num}: Fizz')
    elif num % 5 == 0:
        print(f'{num}: Buzz')
    else:
        print(num)