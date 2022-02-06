from MyModule import MyModule

def test_top_n():
    """
    Test whether the top_n function works correctly
    """

    assert MyModule.top_n([1,2,3,4,5,6],3) == [6,5,4], 'Fail'
    assert MyModule.top_n([10,15,3,7,1,22,19,6],5) == [22,19,15,10,7], 'Fail'
    assert MyModule.top_n([6,14,5,3,9,12,7,1,10,11],8) == [14,12,11,10,9,7,6,5], 'Fail'