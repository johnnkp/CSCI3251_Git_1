from lab7 import check_type


def test_check_type():
    assert check_type() == False
    assert check_type('test') == False

    try:
        check_type(123)
    except TypeError:
        assert True
    else:
        assert False

    myname = "john"
    myID = 123456789
    assert check_type(myname, myID) == True

    myID2 = "123456789"
    assert check_type(myname, myID2) == True
