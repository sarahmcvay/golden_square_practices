from lib.report_length import * # import the function to test

def test_report_length_of_string_three_chars():
    result = report_length("cat")
    assert result == "This string was 3 characters long."

def test_report_length_of_string_ten_chars():
    result = report_length("1234567890")
    assert result == "This string was 10 characters long."