# Exception Handling / Error Handling

# try except block - try catch block
# else block, finally block

class NegativeError(Exception):
    pass

try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    # we don't want negative numbers
    if (n < 0 or d < 0):
        raise NegativeError("No negative numbers please")

    q = n / d

    print(q)

except ZeroDivisionError:
    print("Denominator cannot be zero")

except ValueError:
    print("Please input numbers only")

except NegativeError as err:
    print(err)

except Exception:
    print("Something went wrong!!!")

else:
    # whenever try block executes without having any error
    print("I am else block")

finally:
    # this runs at the end whether any error was raised or not
    print("I am finally block")

print("the end of the program")



# try:
    # open a file
    # write something - it may throw error
# except:
    # handle the error
# finally:
    # close the file