from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("HeLlo") == 0


def test_h():
    assert value("hi") == 20
    assert value("h") == 20
    assert value("how's your day been mate") == 20


def test_other():
    assert value("boi ba ba boi") == 100