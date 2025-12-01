from lib.string_builder import * 

"""
Initially, output is an empty string 
"""
def test_string_builder_intially_empty():
    string_builder = StringBuilder() # create a new instance
    assert string_builder.output() == '' #need () otherwise this does not work

"""
When we add a single string, the output is that string
"""
def test_adding_string_outputs_that_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.output() == "Hello"

""" 
When we add multiple strings, the output is concatenated strings
"""

def test_adding_multiple_strings_outputs_concatenated_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" ")
    string_builder.add("World")
    assert string_builder.output() == "Hello World"

""" 
When we add a single string, the size refelects the size of the string
"""
def test_check_size_of_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.size() == 5 

"""
When we add multiple strings, the size is the size of the concatenated strings
"""
def test_adding_multiple_strings_outputs_concatenated_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" ")
    string_builder.add("World")
    assert string_builder.size() == 11

"""
When we have an empty string, the size is zero
"""
def test_empty_size():
    string_builder = StringBuilder()
    assert string_builder.size() == 0