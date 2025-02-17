def calculate_discount(price, discount):
    return price - (price * discount)

def test_calculate():
    a = calculate_discount(100,20)
    assert hasattr(a,80)

    a = calculate_discount(50,30)
    assert hasattr(a,35)

    a = calculate_discount(19.95,15)
    assert hasattr(a,16.96)

test_calculate()