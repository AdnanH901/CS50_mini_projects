from um import count


def test_um_noncap():
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2


def test_um_trick():
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("umumum") == 0


def test_um_misc():
    assert count("um...") == 1

def test_um_cap():
    assert count("Mum") == 0
    assert count("UM") == 1
    assert count("uM") == 1
    assert count("Um") == 1
    assert count("Um I mean um.... um >.<") == 3

