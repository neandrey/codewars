from nose.tools import assert_equals
#-------------------------------------

def in_array(array1, array2):
    # your code
    L = list()
    for str1 in array1:
        for str2 in array2:
            if str2.find(str1):
                L.append(str1)
                break
    if  L == []:
        return []

    return L

#--------------------------------------
if __name__ == '__main__':
    a1 = ["arp", "live", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ['arp', 'live', 'strong']
    assert_equals(in_array(a1, a2), r)