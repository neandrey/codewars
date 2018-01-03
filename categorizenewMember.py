from nose.tools import assert_equals


def openOrSenior(data):
    L =list()
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            L.append('Senior')
        else: L.append('Open')

    return L
#----------------------------------------
if __name__ == '__main__':
    assert_equals(openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]), ['Open', 'Senior', 'Open', 'Senior'])
    assert_equals(openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]), ['Open', 'Open', 'Senior', 'Open'])
