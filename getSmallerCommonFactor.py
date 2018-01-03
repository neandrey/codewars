from nose.tools import assert_equals
#-------------------------------------
def intToList(num):
    L = list()
    while True:
        if num == 0:
            break
        number = num % 10
        L.append(number)
        num = int(num / 10)
        print(number)
    return L
#-----------------------------------------\
def listToInt(num):
    S = str()
    for i in num:
        S += str(i)
    return (int(S))
#------------------------------------------
def Descending_Order(num):
    if num == 0:
        return 0
    L = intToList(num)
    L.sort(reverse=True)
    num = listToInt(L)
    return num
#--------------------------

if __name__ == '__main__':
    #Test.it("Basic tests")
    assert_equals(Descending_Order(0), 0)
    assert_equals(Descending_Order(15), 51)
    assert_equals(Descending_Order(123456789), 987654321)