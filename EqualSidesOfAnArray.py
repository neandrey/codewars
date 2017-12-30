from nose.tools import assert_equals


def find_even_index(arr):
    #your code here
    arr_len = len(arr)
    for i in range(arr_len):
        sum_right = 0
        sum_left = 0
        face_right = arr[(i+1):]
        sum_right = sum(face_right)
        face_left = arr[:i]
        sum_left = sum(face_left)
        if sum_right == sum_left:
            return i
    return -1


if __name__ == '__main__':
    assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
    assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
    assert_equals(find_even_index([1,2,3,4,5,6]),-1)
    assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
    assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
    assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
    assert_equals(find_even_index(range(1,100)),-1)
    assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
    assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
    assert_equals(find_even_index(range(-100,-1)),-1)