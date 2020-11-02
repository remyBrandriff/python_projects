
#Task: Write a function that returns True if a input number is odd, and False otherwise
def is_odd(n):
    if n%2==0:
        return False
    else:
        return True

#How do we execute/test this function?
print("7",is_odd(7))
print("4", is_odd(4))

#Contractual Design: Caller and Callee have certain expectations about their interactions.
#    Pre-conditions? number must by an int
#    Invariant? (most useful for iterative solutions)
#    Post-conditions? return value is either True or False

# Implement contractual design via assertions
# assertions give us information about where and how things fail
def is_odd(n):
    try:
        # pre-conditions
        assert isinstance(n,int), "Function input must be a int."
        # main goal of function
        if n%2==0:
            result = False
        else:
            result = True
        # post-conditions
        assert isinstance(result,bool), "Result is incorrect"
        assert result in [True,False]
    except AssertionError as e:
        print(e)
        return False
    #else: #only executed if the except clause is not executed
     #   print("Only executed if no exceptions were raised")
    return result
    #finally: #any clean up activites 
     #   print("Executed whether an exception occurs or not.")
        
        
print(is_odd(-5))
print(is_odd('5'))


#What should we test?
#    Think about the input space and possible outputs.
# Equivlance classes: 
# - input is an int
# - input is not an int
# - odd ints
# - even ints
# - negative ints 
# - postive int
# - any other numbers?

#Select instances of the problem to represent each equivalnce class.

is_odd(5)  # odd number
is_odd('5') # non number 
is_odd(2.4) #not an int
is_odd(6)   # even number
is_odd(-3)  # odd negative number
is_odd(-6)  # even negative number
is_odd(0)   # testing 0, not negative or positive


# How do we know the expected result of each function call?
def test_is_odd():
    assert is_odd(5) == True # odd number
    assert is_odd('5') == False# non number 
    assert is_odd(6) == False  # even number
    assert is_odd(-3) == True  # odd negative number
    assert is_odd(-6) == False # even negative number

test_is_odd() # explicit call to test_* is not needed when using pytest




