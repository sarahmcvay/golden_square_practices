from lib.check_codeword import * # import the function to test

"""
If the codeword is correct, Returns "Correct! Come in."
"""
def test_with_correct_codeword():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

"""
If the codeword has the right first and last letter, Returns "Close, but nope."
"""
def test_with_close_codeword():
    result = check_codeword('house')
    assert result == "Close, but nope."

"""
If the codeword is wrong, Returns "WRONG!"
"""
def test_incorrect_codeword():
    result = check_codeword('tiger')
    assert result == "WRONG!"

"""
If the codeword has the right first letter and the wrong last one, Returns "Wrong!"
"""
def test_with_mistakenly_close_codeword():
    result = check_codeword('hat')
    assert result == "WRONG!"