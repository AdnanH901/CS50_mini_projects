from numb3rs import validate


def test_validnums():
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("0.46.72.56") == True
    assert validate("255.255.255.255") == True

def test_invalidname():
    assert validate("cat") == False
    assert validate("1.1.1.f") == False
    assert validate("0.46.72.856") == False
    assert validate("255.-1.255.255") == False
