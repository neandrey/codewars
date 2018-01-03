from nose.tools import assert_equals
#-----------------------------------

def is_kiss(words):
    # Have Fun!
    S = words.split(' ')
    lengthWord = len(S)
    for i in S:
        if len(i) > lengthWord:
            return "Keep It Simple Stupid"
    return "Good work Joe!"

#----------------------------------------
if __name__ == '__main__':
    #test.describe('word count: 5')
    assert_equals(is_kiss('Joe had a bad day'), "Good work Joe!")
    assert_equals(is_kiss('Joe had some bad days'), "Good work Joe!")
    assert_equals(is_kiss('Joe is having no fun'), "Keep It Simple Stupid")
    assert_equals(is_kiss('Sometimes joe cries for hours'), "Keep It Simple Stupid")
