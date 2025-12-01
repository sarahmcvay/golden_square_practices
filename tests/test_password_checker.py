import pytest
from lib.password_checker import *

"""
If password is over 8 chars, output is True
"""
def test_password_over_eight_is_true():
    password_checker = PasswordChecker()
    result = password_checker.check("123456789")  # assert what the function returns
    assert result == True

""" 
If the string is empty, output is an 
error message "Invalid password, must be 8+ characters."
"""
def test_password_empty_raises_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."


"""
If password is less than 8 chars, output is an
error message "Invalid password, must be 8+ characters."
"""
def test_password_less_than_eight():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("123456")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."

"""
If password is exactly 8 chars, output is True
"""
def test_password_exactly_eight_is_true():
    password_checker = PasswordChecker()
    result = password_checker.check("12345678")  # assert what the function returns
    assert result == True

# class PasswordChecker():
#     def check(self, password):
#         if len(password) >= 8:
#             return True
#         else:
# raise Exception("Invalid password, must be 8+ characters.)