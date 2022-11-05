import calculations as c


def test(function, expected):
    if (function == expected):
        return print("pass")
    else:
        return print("fail")


print(c.amplitude(4, 8), c.distance(1, 1, 0),c.angle(4,2))
