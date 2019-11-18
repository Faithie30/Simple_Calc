from Calc import calc

def test_add():
    assert calc.add(0,0) == 0
    assert calc.add(-1,-1) == -2
    assert calc.add(4,5) == 9
    assert calc.add(1,2,3,4) == 10

def test_multiply():
    assert calc.multiply(1,2) == 2
    assert calc.multiply(4,5) == 20
    assert calc.multiply(1,2,3,4) == 24
   


