import halli

def test_answer():
    assert halli.func(4) == 5
    assert halli.func(3) == 4


def test_sq():
    assert halli.sq(2) == 4
    assert halli.sq(3) == 9
    