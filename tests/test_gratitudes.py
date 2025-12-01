from lib.gratitudes import *

"""
Initially, reports empty string, would return "Be grateful for: "
"""
def test_initially_empty():
    gratitudes = Gratitudes() #creates a new instance
    assert gratitudes.format() == "Be grateful for: "

"""
When you add a single string the output is that string
"""
def test_adding_string_outputs_formatted_string():
    gratitudes = Gratitudes()
    gratitudes.add("being healthy")
    assert gratitudes.format() == "Be grateful for: being healthy"

"""
When you add multiple string the output is joined strings
"""
def test_adding_multiple_string_outputs_long_string():
    gratitudes = Gratitudes()
    gratitudes.add("being healthy")
    gratitudes.add("having family")
    assert gratitudes.format() == "Be grateful for: being healthy, having family"
