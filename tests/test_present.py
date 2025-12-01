import pytest
from lib.present import *

"""
When we wrap an object, we get it back when it is unwrapped 
No errors
"""
def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33


"""
If we try to unwrap an object before wrapping, 
We get an error message, "No contents have been wrapped."
"""
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message =str(e.value)
    assert message == "No contents have been wrapped."

"""
If we try to wrap an already wrapped present,
We get an error message, "Contents have already been wrapped."
"""
def test_wrapping_content_already_wrapped_throws_error():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == "Contents have already been wrapped."

"""
If we try to wrap a ready wrapped present the first wrapped value is preserved 
"""
def test_wrapping_content_already_wrapped_value_preserved():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    assert present.unwrap() == 44 #don't forget ()


# class Present():
#     def __init__(self):
#         self.contents = None

#     def wrap(self, contents):
#         if self.contents is not None:
#             raise Exception("A contents has already been wrapped.")
#         self.contents = contents 
    
#     def unwrap(self):
#         if self.contents is None:
#             raise Exception("No contents have been wrapped.")
#         return self.contents