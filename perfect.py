# program which calculates all the perfect numbers up to a limit provided by the user
# perfect number: a positive integer equal to the sum of its proper divisors


# define a function which checks if a number is a perfect number
def perfect_number_check(number):
    total = 0
    for i in range(number-1):
        if number % (i+1) == 0:
            total += i+1

    if total == number:
        return True
    else:
        return False

# define a function which checks for all perfect numbers in a given range
def main():
    limit = int(input("Till what integer do you want to know all the perfect numbers: "))
    for i in range(limit):
        if perfect_number_check(i+1) == True:
            print(i+1)
          
main()
