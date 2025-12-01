from lib.add_five import * #import the function to test

def test_add_five_returns_eight_for_three(): #create a single test example
    result = add_five(3) #run with example argument 3
    assert result == 8 #assert that this should return 8