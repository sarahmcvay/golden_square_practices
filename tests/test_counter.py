from lib.counter import * # import the function to test

"""
Initially, reports a count of zero
"""
def test_counter_initially_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

"""
Adding a single number is reflected in the final count
"""
def test_counter_adds_single_number_to_counter():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

# we have not tested all the behaviours, e.g. if there are multiple numbers. 

"""
When we add multiple numbers to the counter, 
The Sum of those numbers is the final count
"""
def test_counter_adds_multiple_numbers_to_the_count():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == "Counted to 8 so far."

"""
Could also look at minus numbers. 
"""