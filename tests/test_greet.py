from lib.greet import * #import the function to test

def test_greet_person_of_given_name():
    result = greet("Sarah")
    assert result == "Hello, Sarah!"