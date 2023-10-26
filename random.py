def is_prime (number):
    for i in range(2 , int(number ** 0.5) + 1 ):
        if number % i == 0:
            return False
    return number > 1
 

number = input( 'enter the number you want to check: ' )
number = int(number)
if (number < 0) or (number % 1 != 0):
    print( 'Oops your number is not a natoral number' )
elif is_prime (number):
    print ('Congratulations, your number is a prime number')
else:
    print ('Oops your number is not a prime number')
  
